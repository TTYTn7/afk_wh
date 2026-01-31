from afk_wh.utilities import chance_event
from typing import TYPE_CHECKING, Tuple
if TYPE_CHECKING:
    from afk_wh.Encounter import Encounter
    from afk_wh.DamageType import DamageType

class BasicAttack:
    def __init__(
            self,
            damage: int,
            attack_range: int,
            damage_type: 'DamageType'
    ):
        self.damage = damage
        self.attack_range = attack_range
        self.damage_type = damage_type

    def can_hit(self, encounter: 'Encounter') -> bool:
        return self.attack_range >= encounter.range

    def hit(self, encounter: 'Encounter', crit_rate: float, crit_multiplier: int) -> Tuple[float, bool, 'DamageType']|None:
        if not self.can_hit(encounter):
            print(f'Can\'t hit, attack range ({self.attack_range}) is less than the distance ({encounter.range}) to target.')
            return None

        crit_strike, crit_roll = chance_event(crit_rate)
        if crit_strike:
            print(f'Attack is a crit, crit roll: {crit_roll}, crit chance: {crit_rate}')
        else:
            crit_multiplier = 100
        return self.damage * (crit_multiplier / 100), crit_strike, self.damage_type

