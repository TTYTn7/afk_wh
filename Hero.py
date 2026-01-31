# Hero bas basic attacks, a skill, an ultimate, and a passive
# basic stats - health, crit rate, dodge rate, armor, magic resist, stun resist, energy generation

from utilities import chance_event
from typing import TYPE_CHECKING, Tuple
if TYPE_CHECKING:
    from Encounter import Encounter
from BasicAttack import BasicAttack, AttackType
from Skill import Skill
from Ultimate import Ultimate
from Passive import Passive
from Status import Status


class Hero:
    def __init__(
            self,
            name: str,
            starting_health: int,
            armor: int,
            dodge_rating: float,
            physical_resist: float,
            magic_resist: float,
            stun_resist: float,
            energy_generation_attack: int,
            energy_generation_defense: int,
            energy_cap: int,
            attack_speed: float,
            crit_rate: float,
            crit_multiplier: int,
            basic_attack: BasicAttack,
            skill: Skill,
            ultimate: Ultimate,
            passive: Passive,
            status: Status
    ):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.armor = armor # Armor should later transition into physical resistance via some formula. ATM it is physical resist
        self.dodge_rating = dodge_rating # Same for dodge
        self.physical_resist = physical_resist
        self.magic_resist = magic_resist
        self.stun_resist = stun_resist
        self.energy_generation_attack = energy_generation_attack
        self.energy_generation_defense = energy_generation_defense
        self.energy_cap = energy_cap
        self.current_energy = 0
        self.attack_speed = attack_speed
        self.crit_rate = crit_rate
        self.crit_multiplier = crit_multiplier
        self.basic_attack = basic_attack
        self.skill = skill
        self.ultimate = ultimate
        self.passive = passive
        self.status = status

    def __str__(self):
        return f'Name: {self.name}, Health: {self.current_health}/{self.starting_health}, Energy: {self.current_energy}/{self.energy_cap}, Status: {self.status}'

    def increment_energy(self, energy_generation: int, crit: bool):
        crit_bonus = (energy_generation * 0.1) * crit
        self.current_energy += (energy_generation + crit_bonus)
        if self.current_energy > self.energy_cap:
            self.current_energy = self.energy_cap

    def dodge(self) -> bool:
        if self.status not in [Status.stunned, Status.asleep]: # Stuns and sleep disable dodge
            attack_dodged, dodge_roll = chance_event(self.dodge_rating)
            if attack_dodged:
                print(f'Attack was dodged, dodge roll: {dodge_roll}, dodge chance: {self.dodge_rating}%')
                return True
        return False

    def attack(self, encounter: 'Encounter') -> Tuple[float, bool, AttackType]|None:
        attack_outcome = self.basic_attack.hit(encounter, self.crit_rate, self.crit_multiplier)
        if attack_outcome:
            self.increment_energy(self.energy_generation_attack, attack_outcome[1])
        return attack_outcome

    def apply_defenses(self, damage: int, damage_type: AttackType) -> int|None:
        if self.dodge():
            return None
        if damage_type == AttackType.physical:
            pre_resist_damage = damage - ((damage * self.armor) / 100)
            post_resist_damage = pre_resist_damage - ((pre_resist_damage * self.physical_resist) / 100)
        elif damage_type == AttackType.magic:
            post_resist_damage = damage - ((damage * self.magic_resist) / 100)
        elif damage_type == AttackType.true:
            post_resist_damage = damage
        else:
            raise ValueError(
                f'Incorrect BasicAttack damage type: {damage_type}, must be \'physical\', \'magic\', or \'true\'.')
        print(f'Original damage {damage} reduced to {post_resist_damage} after applying {damage_type} resists.')
        return post_resist_damage



    def take_damage(self, damage: int, crit: bool, damage_type: AttackType):
        post_resist_damage = self.apply_defenses(damage, damage_type)
        if post_resist_damage:
            self.current_health -= post_resist_damage
            if self.current_health < 1:
                print(f'{self.name} dies tragically!')
                self.status = Status.dead
            else:
                self.increment_energy(self.energy_generation_defense, crit)
