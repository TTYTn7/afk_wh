# Basic attack has damage, range
from utilities import *
from enum import StrEnum
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Encounter import Encounter


class AttackType(StrEnum):
    physical = 'physical'
    magic = 'magic'
    true = 'true'


class BasicAttack:
    def __init__(
            self,
            damage: int,
            range: int,
            type: AttackType
    ):
        self.damage = damage
        self.range = range
        self.type = type

    def can_hit(self, encounter: 'Encounter') -> bool:
        return self.range >= encounter.range

    def hit(self, encounter: 'Encounter', crit_rate: float, crit_multiplier: int) -> float|None:
        if not self.can_hit(encounter):
            print(f'Can\'t hit, attack range ({self.range}) is less than the distance ({encounter.range}) to target.')
            return None
        # See if the attack lands and how much damage does it do
        # Does it land. For later - stuns should disable dodge
        attack_dodged, dodge_roll = chance_event(encounter.target.dodge)
        if attack_dodged:
            print(f'Attack was dodged, dodge roll: {dodge_roll}, dodge chance: {encounter.target.dodge}%')
            return None

        if self.type == AttackType.physical:
            pre_resist_damage = self.damage - ((self.damage * encounter.target.armor) / 100)
            # TODO make some dict and find way to unify the resist handling of phys res and magic res so we don't repeat the line below
            post_resist_damage = pre_resist_damage - ((pre_resist_damage * encounter.target.physical_resist) / 100)
        elif self.type == AttackType.magic:
            post_resist_damage = self.damage - ((self.damage * encounter.target.magic_resist) / 100)
        elif self.type == AttackType.true:
            post_resist_damage = self.damage
        else:
            raise ValueError(f'Incorrect BasicAttack damage type: {self.type}, must be \'physical\', \'magic\', or \'true\'.')

        crit_strike, crit_roll = chance_event(crit_rate)
        if crit_strike:
            print(f'Attack is a crit, crit roll: {crit_roll}, crit chance: {crit_rate}')
        else:
            crit_multiplier = 100
        return post_resist_damage * (crit_multiplier / 100)

