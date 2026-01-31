from Encounter import Encounter
from examples.example_heroes import heroes

hero1 = heroes['hero1']
hero2 = heroes['hero2']
example_encounter1 = Encounter(12, hero2)
example_encounter2 = Encounter(12, hero1)
encounters = {'one': (hero1, example_encounter1), 'two': (hero2, example_encounter2)}

attack_types = ['Basic', 'Skill']

for number in encounters:
    print(f'Round: {number}')
    attacker = encounters[number][0]
    encounter = encounters[number][1]
    defender = encounter.target
    for attack in attack_types:
        print(f'{attack} attack')
        attack_outcome = None
        if attack == 'Basic':
            attack_outcome = attacker.use_attack(encounter)
        elif attack == 'Skill':
            attack_outcome = attacker.use_skill(encounter)
            defender.take_affliction(attacker.skill.affliction, attacker.skill.damage_type)
        if attack_outcome:
            dmg, crit, dmg_type = attack_outcome
            print(f'Damage: {dmg}, Crit: {crit}, Type: {dmg_type}')
            defender.take_damage(dmg, crit, dmg_type)

print(hero1)
print(hero2)
