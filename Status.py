from enum import StrEnum


class Status(StrEnum):
    normal = 'normal'
    stunned = 'stunned'
    asleep = 'asleep' # Damage wakes it up
    dead = 'dead'
    untargetable = 'untargetable' # Cannot be targeted
    hidden = 'hidden' # Not on the field, temporary condition
    invulnerable = 'invulnerable' # Can be controlled, cannot be damaged
    spell_immune = 'spell_immune' # Cannot be controlled, can be damaged
