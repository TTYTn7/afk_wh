from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Hero import Hero

class Encounter:
    def __init__(
            self,
            range: int,
            target: 'Hero'
    ):
        self.range = range
        self.target = target
