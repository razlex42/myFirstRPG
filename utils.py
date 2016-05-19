import os

def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def Pause():
    input("\nPaused ")

def PauseAndClear():
    Pause()
    ClearScreen()
