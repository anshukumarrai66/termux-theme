import os,sys,time

#....................................#
# defining the colours for terminals #
#....................................#

g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"


W = "\x1b[0m"
W = "\x1b[0m"
R = "\x1b[31m"
G = "\x1b[1;32m"
O = "\x1b[33m"
B = "\x1b[34m"
P = "\x1b[35m"
C = "\x1b[36m"
W1 = "\x1b[37m"
Bold_GR = "\x1b[1;30m"
GR = "\x1b[0;90m"
Bg_R = "\x1b[1;41m"
Bg_GR = "\x1b[1;42m"

#........................................#
# Definig the function for slow printing #
# the text on a terminal                 #
#........................................#

def slowprints(a):
    for b in a + '\n':
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.001)

os.system("clear")
time.sleep(1)

#...........................................#
# Defining the function for asking the user #
# input about username or prompt name for   #
# the skull banner and also execute the     #
# load() and inst() funtion created inside  #
# this script for some purpose              #
#...........................................#
#github name

def github_name():
    os.system("clear")
#    banner()
    print("")
    user = input(f" [{G}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{G}•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
#    load()
#    inst()
    github_copy(user)
#    bashrc(prompt)


#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#github

def github():
    github_name()
#    move()

#.............................................#
# Defining the function for creating external #
# file for the github banner                  #
#.............................................#
# github_copy

def github_copy(user):
        with open("done4us1","w") as external_file:
            add_text ='''\n

######################################

#....................................#
# defining the colours for terminals #
#....................................#

g = "\\033[32;1m"
gt = "\\033[0;32m"
bt = "\\033[34;1m"
b = "\\033[36;1m"
m = "\\033[31;1m"
c = "\\033[0m"
p = "\\033[37;1m"
u = "\\033[35;1m"
M = "\\033[3;1m"
k = "\\033[33;1m"
kt = "\\033[0;33m"
a = "\\033[30;1m"


W = "\\x1b[0m"
R = "\\x1b[31m"
G = "\\x1b[1;32m"
O = "\\x1b[33m"
B = "\\x1b[34m"
P = "\\x1b[35m"
C = "\\x1b[36m"
W1 = "\\x1b[37m"
Bold_GR = "\\x1b[1;30m"
GR = "\\x1b[0;90m"
Bg_R = "\\x1b[1;41m"
Bg_GR = "\\x1b[1;42m"

D = "}"
E = "{"

#######################################

#module
import os,sys,time

def slowprints(a):
    for b in a + '\\n':
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.001)

os.system("clear")
time.sleep(1)

def github(user):
    slowprints(f"""
                 {G}
              .:+o+:-..````..-:+o+:.
           `:o+-`                `:+o:`
         `/o:`                      `:o/`
        -s/`  .-..`            `..--` `/s-
       /o.   `:.`.-:----------:-.``:-   .o/
      /o`    .:`    `              --    `o/
     -s.     .:`                   --     .s-
     o/     .:`                     --     +o
    .s-     :.                      `:`    -s`
    .s.     :.       `Done4us       `:`    .s.
    .s-     --                      .:     -s.
     o/     `-.                    `-.     /o
     -s.     `--`                `.-`     .s-
      /o` ----``..--..`    `...--.`      `o/
       /o. `----`  `-.      `-.         .o/
        -o:  -.......        ..       `:o-
         `:o:``....--        ..     `:o:`
           `:+/-`  `-        ..  `-/+:`
              `-/+///..````..://+/-`
                  `.-::////::-.`

{a}...::::[ Powered by Done4us YouTube ]::::...{W}
        {W} [{Bg_GR}  Username : {user}  {W}]\\n""")

github(user)'''
            print(f'user = "{user}"\n', add_text, file=external_file)
            external_file.close()



github()
