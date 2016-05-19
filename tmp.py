import sys
import termios
import tty
import textwrap
import shutil
import os

def locate(user_string="", x=0, y=0, length=0):
    # Don't allow any user errors. Python's own error detection will check for
    # syntax and concatination, etc, etc, errors.
    x=int(x)
    y=int(y)
    if x>=255: x=255
    if y>=255: y=255
    if x<=0: x=0
    if y<=0: y=0
    HORIZ=str(x)
    VERT=str(y)
    # Plot the user_string at the starting at position HORIZ, VERT...
    print("\033["+VERT+";"+HORIZ+"f"+user_string)

def DrawBorders():
    sz = shutil.get_terminal_size()
    DrawBorder(3, 5, sz.lines-5, sz.columns - 5)
    DrawHorizontalLine(5, sz.columns - 5, sz.lines - 10)
    DrawVerticalLine(3, sz.lines-10, sz.columns - 50)

def DrawBorder(top, left, bottom, right):
    locate('+', left, top)
    for i in range(left + 1, right):
        locate('-', i, top)
    locate('+', right, top)

    for i in range(top + 1, bottom):
        locate('|', left, i)
        locate('|', right, i)

    locate('+', left, bottom)
    for i in range(left + 1, right):
        locate('-', i, bottom)
    locate('+', right, bottom)

def DrawVerticalLine(top, bottom, x):
    locate('+', x, top)
    for i in range(top + 1, bottom):
        locate('|', x, i)
    locate('+', x, bottom)
    pass

def DrawHorizontalLine(left, right, y):
    locate('+', left, y)
    for i in range(left + 1, right):
        locate('-', i, y)
    locate('+', right, y)



#locate('|                                        | Int: 14         |', 1, 2)
#locate('|                                        | Str: 16         |', 1, 3)
#locate('|          This is a test                | Con: 18         |', 1, 4)
#locate('|                                        |                 |', 1, 5)
#locate('|                                        |                 |', 1, 6)
#locate('+----------------------------------------+-----------------+', 1, 7)

def GetKey():
    stdinFileDesc = sys.stdin.fileno() #store stdin's file descriptor
    oldStdinTtyAttr = termios.tcgetattr(stdinFileDesc) #save stdin's tty attributes so I can reset it later
    try:
        tty.setraw(stdinFileDesc) #set the input mode of stdin so that it gets added to char by char rather than line by line
        key = sys.stdin.read(1) #read 1 byte from stdin (indicating that a key has been pressed)
    finally:
        termios.tcsetattr(stdinFileDesc, termios.TCSADRAIN, oldStdinTtyAttr)
    return key

def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
#i = 21
#for line in textwrap.wrap("This is a very long piece of text that should wrap a few times", 38):
#    locate(line.ljust(38), 22, i)
#    i += 1

#for counter in range(1,30):
#    locate()
#locate('', 0,30)

ClearScreen()
DrawBorders()
GetKey()
