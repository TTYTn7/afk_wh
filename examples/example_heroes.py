from afk_wh.Hero import Hero
from afk_wh.status_effects.Status import Status
from afk_wh.examples.example_basic_attacks import basic_attacks
from afk_wh.examples.example_skills import skills
from afk_wh.examples.example_ultimates import ultimates
from afk_wh.examples.example_passives import passives


heroes = {
    'hero1': Hero(
        'attacker', 10000, 20, 35, 20, 25, 10,
        100, 10, 1000,
        1.3, 23.8, 200,
        basic_attacks['example_basic_attack'], skills['example_skill'],
        ultimates['example_ultimate'], passives['example_passive'], Status.normal
    ),
    'hero2': Hero(
        'defender', 10000, 20, 35, 20, 25, 10,
        100, 10, 1000,
        1.3, 23.8, 200,
        basic_attacks['example_basic_attack'], skills['example_skill'],
        ultimates['example_ultimate'], passives['example_passive'], Status.normal
    )
}
