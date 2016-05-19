import random

from utils import *
from encounter import Encounter

class Bounty(Encounter):
    def Start(self):
        print("On your way out of the inn you notice a bouty posted on the wall.")
        print("This seems like just the thing to satiate your need for adventuer.\n")
        print("Grabbing the notice off the wall you venture out into town looking for the wrong doer...")
        PauseAndClear()
        getattr(self, "Variation" + str(random.randrange(1,4)))()

    def Variation1(self):
        print("You find your self standing in front of the inn, wondering where to start.")
        print("Maybe someone at the (m)arket has some information.")
        print("People of questionable morals have been know to hang around the (d)ocks.")
        print("The (s)ewers are more then capable of hiding someone one desperate enough to face the dangers.")
        PauseAndClear()
        print("[Next variation here]")

    def Variation2(self):
        print("After wandering around aimlessly for a bit,")
        print("you decide to look at the poster you hastily tore from the wall.\n")
        print("The poster mentions the wanted one's last know hideout was the old (m)ill on the outskirts of town.")
        print("There is a hand scrawled note at the bottom of the poster,")
        print("mentioning a sighting near the (b)lacksmith's shop")
        print("You have (f)riend at the butcher's shop who always seems to know who's coming and going.")
        PauseAndClear()
        print("[Next variation here]")

    def Variation3(self):
        print("A new pain in your knee is all you have to show for your hours of searching.")
        print("Exhausted and discouraged you start heading back to the inn.\n")
        print("Passing by the guard house you notice someone matching the poster being led away in shackles.")
        Pause()
