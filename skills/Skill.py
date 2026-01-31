from afk_wh.utilities import chance_event
from afk_wh.status_effects.Affliction import Affliction
from typing import TYPE_CHECKING, Tuple
if TYPE_CHECKING:
    from afk_wh.DamageType import DamageType
    from afk_wh.Encounter import Encounter

import logging
logger = logging.getLogger(__name__)

class Skill:
    def __init__(
            self,
            name: str,
            skill_range: int,
            damage: int,
            damage_type: 'DamageType',
            cooldown: int,
            affliction: Affliction,
            energy_gain: int

    ):
        self.name = name
        self.skill_range = skill_range
        self.damage = damage
        self.damage_type = damage_type
        self.cooldown = cooldown
        self.affliction = affliction
        self.energy_gain = energy_gain

    def can_hit(self, encounter: 'Encounter') -> bool:
        return self.skill_range >= encounter.range

    def hit(self, encounter: 'Encounter', crit_rate: float, crit_multiplier: int) -> Tuple[float, bool, 'DamageType']|None:
        if not self.can_hit(encounter):
            logger.debug(f'Can\'t hit, attack range ({self.skill_range}) is less than the distance ({encounter.range}) to target.')
            return None

        crit_strike, crit_roll = chance_event(crit_rate)
        if crit_strike:
            logger.debug(f'Attack is a crit, crit roll: {crit_roll}, crit chance: {crit_rate}')
        else:
            crit_multiplier = 100
        return self.damage * (crit_multiplier / 100), crit_strike, self.damage_type
