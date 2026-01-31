from Encounter import Encounter
from examples.example_heroes import heroes

import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',  # Logs go to this file
    filemode='w'  # 'a' to append, 'w' to overwrite
)
logger = logging.getLogger(__name__)
logger.debug('Log Start')

hero1 = heroes['hero1']
hero2 = heroes['hero2']
example_encounter1 = Encounter(12, hero2)
example_encounter2 = Encounter(12, hero1)
sides = {'first': (hero1, example_encounter1), 'second': (hero2, example_encounter2)}

attack_types = ['Basic', 'Skill']

def full_round(sides):
    for number in sides:
        logger.debug(f'Side: {number}')
        attacker = sides[number][0]
        encounter = sides[number][1]
        defender = encounter.target
        for attack in attack_types:
            logger.debug(f'{attack} attack')
            attack_outcome = None
            if attack == 'Basic':
                attack_outcome = attacker.use_attack(encounter)
            elif attack == 'Skill':
                attack_outcome = attacker.use_skill(encounter)
                defender.take_affliction(attacker.skill.affliction, attacker.skill.damage_type)
            if attack_outcome:
                dmg, crit, dmg_type = attack_outcome
                logger.debug(f'Damage: {dmg}, Crit: {crit}, Type: {dmg_type}')
                defender.take_damage(dmg, crit, dmg_type)

for i in range(50):
    logger.debug('-----------------------------------------------------------------')
    logger.debug(f'------------------------- Round {i+1} --------------------------')
    logger.debug('-----------------------------------------------------------------')
    full_round(sides)

logger.debug(hero1)
logger.debug(hero2)
