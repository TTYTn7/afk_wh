# Hero bas basic attacks, a skill, an ultimate, and a passive
# basic stats - health, crit rate, dodge rate, armor, magic resist, stun resist, energy generation


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Encounter import Encounter
from BasicAttack import BasicAttack
from Skill import Skill
from Ultimate import Ultimate
from Passive import Passive
from Status import Status


class Hero:
    def __init__(
            self,
            starting_health: int,
            armor: int,
            dodge: float,
            physical_resist: float,
            magic_resist: float,
            stun_resist: float,
            energy_generation: int,
            attack_speed: float,
            crit_rate: float,
            crit_multiplier: int,
            basic_attack: BasicAttack,
            skill: Skill,
            ultimate: Ultimate,
            passive: Passive,
            status: Status
    ):
        self.starting_health = starting_health
        self.current_health = starting_health
        self.armor = armor # Armor should later transition into physical resistance via some formula. ATM it is physical resist
        self.dodge = dodge # Same for dodge
        self.physical_resist = physical_resist
        self.magic_resist = magic_resist
        self.stun_resist = stun_resist
        self.energy_generation = energy_generation
        self.attack_speed = attack_speed
        self.crit_rate = crit_rate
        self.crit_multiplier = crit_multiplier
        self.basic_attack = basic_attack
        self.skill = skill
        self.ultimate = ultimate
        self.passive = passive
        self.status = status


    def attack(self, encounter: 'Encounter'):
        return self.basic_attack.hit(encounter, self.crit_rate, self.crit_multiplier)

