# Basic attack has damage, range
from utilities import *
from enum import StrEnum
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Encounter import Encounter
from Status import Status


class AttackType(StrEnum):
    physical = 'physical'
    magic = 'magic'
    true = 'true'


class BasicAttack:
    def __init__(
            self,
            damage: int,
            attack_range: int,
            attack_type: AttackType
    ):
        self.damage = damage
        self.attack_range = attack_range
        self.attack_type = attack_type

    def can_hit(self, encounter: 'Encounter') -> bool:
        return self.attack_range >= encounter.range

    def hit(self, encounter: 'Encounter', crit_rate: float, crit_multiplier: int) -> Tuple[float, bool, AttackType]|None:
        if not self.can_hit(encounter):
            print(f'Can\'t hit, attack range ({self.attack_range}) is less than the distance ({encounter.range}) to target.')
            return None

        crit_strike, crit_roll = chance_event(crit_rate)
        if crit_strike:
            print(f'Attack is a crit, crit roll: {crit_roll}, crit chance: {crit_rate}')
        else:
            crit_multiplier = 100
        return self.damage * (crit_multiplier / 100), crit_strike, self.attack_type

