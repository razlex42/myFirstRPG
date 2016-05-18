import os
import random

def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def Pause():
    input("\nPaused ")

def PauseAndClear():
    Pause()
    ClearScreen()

class Player:
    name = ""

class Encounter(object):
    def factory(encounterType):
        return eval(encounterType + "()")
    factory = staticmethod(factory)

class DarkStranger(Encounter):
    def Start(self):
        print("You encounter a dark stranger...")

class AbandonMine(Encounter):
    def Start(self):
        print("You come across an abandon mine...")

class TreasureMap(Encounter):
    def Start(self):
        print("You find a old treasure map...\n\n")
        print("")

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

class Adventure:
    def __init__(self):
        self.encounterId = 1 #random.randrange(1,101)
        if(self.encounterId > 64):
            self.encounter = Encounter.factory("DarkStranger")
        elif(self.encounterId > 49 < 75):
            self.encounter = Encounter.factory("AbandonMine")
        elif(self.encounterId > 24 < 50):
            self.encounter = Encounter.factory("TreasureMap")
        else:
            self.encounter = Encounter.factory("Bounty")

    def Start(self):
        self.encounter.Start()

class Game:
    def __init__(self):
        self.gameRunning = False
        self.player = Player()

    def QuitGame(self):
        self.gameRunning = False

    def Adventure(self):
        adventure = Adventure()
        adventure.Start()

    def LookForAdventure(self):
        print("Looking for adventure...\n")
        #if(random.randrange(1,101) > 75):
        if(True):
            self.Adventure()
        else:
            print("It's quiet for now.\n")
        print("You head back to the inn to reflect on the days events...")
        Pause()

    def RequestFood(self):
        print("Looking for food...\n")
        if(random.randrange(1,101) > 25):
            print("Your in luck, the cook just finished a great feast.\n")
        else:
            print("The fire is cold right now, come back later.\n")
        Pause()

    def GetRoomForTheNight(self):
        print("Looking for an open room...\n")
        if(random.randrange(1,101) > 50):
            print("Helga grabs a key off the wall and point you upstairs.\n")
        else:
            print("I'm sorry my friend, were full for the night, there might be space in the barn.\n")
        Pause()

    def Loop(self):
        while self.gameRunning:
            ClearScreen()
            print("What brings you this way, are you looking for (a)dventure, or maybe some (f)ood perhaps?")
            print ("If you need a place to (r)est then Helga can set you up with a room.")
            choice = input("\nWhat would you like to do? ")
            ClearScreen()
            if(choice == 'q'):
                self.QuitGame()
            elif(choice == 'a'):
                self.LookForAdventure()
            elif(choice == 'f'):
                self.RequestFood()
            elif(choice == 'r'):
                self.GetRoomForTheNight()
            else:
                print("I didn't catch that...")

    def Start(self):
        print ("Welcome to The Sleeping Dragon Inn adventurer.\n")
        self.player.name = input("I haven't see you around here before, what do they call you? ")
        print ("\nWell met {}, I'm Hagard, this here is my Inn.\n".format(self.player.name))
        PauseAndClear()
        self.gameRunning = True
        self.Loop()

if __name__ == '__main__':
    ClearScreen()
    game = Game()
    game.Start()
