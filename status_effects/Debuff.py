from typing import Set

class Debuff:
    def __init__(
            self,
            name: str='N/A',
            stats: Set[str]={}
    ):
        self.name = name
        self.stats = stats
