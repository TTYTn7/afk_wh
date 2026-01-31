from afk_wh.skills.Skill import Skill
from afk_wh.DamageType import DamageType
from afk_wh.examples.example_afflicions import afflictions

skills = {
    'example_skill': Skill(
        'skill1', 12, 200, DamageType.physical,9, afflictions['example_affliction'], 300
    )
}
