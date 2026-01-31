from Hero import Hero
from BasicAttack import BasicAttack, AttackType
from Encounter import Encounter
from Skill import Skill
from Ultimate import Ultimate
from Passive import Passive
from Status import Status


example_basic_attack = BasicAttack(50, 15, AttackType.true)
example_basic_skill = Skill('one')
example_basic_ultimate = Ultimate('one')
example_basic_passive = Passive('one')
attacker = Hero(
    100, 20, 15, 20, 25, 10, 40,
    1.3, 23.8, 200, example_basic_attack, example_basic_skill, example_basic_ultimate,
    example_basic_passive, Status.normal
)
defender = Hero(
    100, 20, 15, 20, 25, 10, 40,
    1.3, 23.8, 200, example_basic_attack, example_basic_skill, example_basic_ultimate,
    example_basic_passive, Status.normal
)

example_encounter = Encounter(12, defender)

print(attacker.attack(example_encounter))

