from Encounter import Encounter
from examples.example_heroes import heroes

attacker = heroes['attacker']
defender = heroes['defender']

example_encounter = Encounter(12, defender)

dmg, crit, dmg_type = attacker.attack(example_encounter)
print(f'Damage: {dmg}, Crit: {crit}, Type: {dmg_type}')
defender.take_damage(dmg, crit, dmg_type)
print(defender)

