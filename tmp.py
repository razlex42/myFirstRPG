import sys
import termios
import tty
import textwrap
import shutil

def locate(user_string="", x=0, y=0):
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
    print(sz)
    print(sz.columns)
    print(sz.lines)
    locate('+',5,1)
    for i in range(6, sz.columns - 5):
        locate('-',i,1)
    locate('+', sz.columns - 5, 1)


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


#i = 21
#for line in textwrap.wrap("This is a very long piece of text that should wrap a few times", 38):
#    locate(line.ljust(38), 22, i)
#    i += 1

#for counter in range(1,30):
#    locate()
#locate('', 0,30)

DrawBorders()
GetKey()
