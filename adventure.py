from dark_stranger import DarkStranger
from abandon_mine import AbandonMine
from treasure_map import TreasureMap
from bounty import Bounty

class Adventure:
    def __init__(self):
        self.encounterId = 1 #random.randrange(1,101)
        if(self.encounterId > 64):
            self.encounter = DarkStranger()
        elif(self.encounterId > 49 < 75):
            self.encounter = AbandonMine()
        elif(self.encounterId > 24 < 50):
            self.encounter = TreasureMap()
        else:
            self.encounter = Bounty()

    def Start(self):
        self.encounter.Start()
