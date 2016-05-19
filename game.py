import os
import random
import kbhit
import gettermsize

from utils import *
from player import Player
from encounter import Encounter
from adventure import Adventure

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
