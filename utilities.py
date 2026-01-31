import numpy as np
from typing import TYPE_CHECKING, Tuple


def chance_event(event_rate: float) -> Tuple[bool,np.array]:
    # Multiplying both the roll and the rate by 100 to have 2 digit floating point precision for crit rate
    roll = np.random.randint(1, 10001, 1)
    return roll <= event_rate * 100, roll / 100
