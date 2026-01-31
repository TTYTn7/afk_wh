from afk_wh.status_effects.Status import Status
from afk_wh.status_effects.Buff import Buff
from afk_wh.status_effects.Debuff import Debuff

class Affliction:
    def __init__(
            self,
            name: str,
            duration: int,
            status: Status=Status.normal,
            buff: Buff=Buff(),
            debuff: Debuff=Debuff()
    ):
        self.name = name
        self.duration = duration
        self.status = status
        self.buff = buff
        self.debuff = debuff


