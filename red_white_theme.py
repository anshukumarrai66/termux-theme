W#modules

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


#...................................#
# Defining the function for showing #
# loading effect on a terminal      #
#...................................#
#loading effect

def load():
    load = f'{R}.'
    count = 0
    for t in range(20):
             time.sleep(0.3)
             print(f'\r {R}[{W}●{R}] {W}Loading {load}', end='', flush=True)
             count += 1
             if count == 3:
                count = 0
                load += '.'
    print('\n')


#.............................................#
# Defining the fuction for showing the banner #
# containg Tool info and Authour info         #
#.............................................#
# Banner

def banner():
    slowprints(f'''

{R} ████████ ██   ██ ███████ {W}{W} ███    ███ ███████ 
{R}    ██    ██   ██ ██      {W}{W} ████  ████ ██      
{R}    ██    ███████ █████   {W}{W} ██ ████ ██ █████ 
{R}    ██    ██   ██ ██      {W}{W} ██  ██  ██ ██    
{R}    ██    ██   ██ ███████ {W}{W} ██      ██ ███████

{R} ●{W} Author  AnonymousCoder        {Bold_GR} Version 0.0.1
{R} ●{W} YouTube Done4us''')


#...................................#
# Defining the fuction for show the #
# user about tool installation on   #
# his terminal                      #
#...................................#
# Installed Successfully

def inst():
    os.system("clear")
    banner()
    print("")
    print(f"{W} Theme Installed {R}Successfully {W}!")
    print("")
    input(f"{W} [{R}home{W}~{Bold_GR}theme{W}] > ")
    time.sleep(1)
    os.system("exit")
#    print("")

#...........................................#
# Defining the function for asking the user #
# input about username or prompt name for   #
# the skull banner and also execute the     #
# load() and inst() funtion created inside  #
# this script for some purpose              #
#...........................................#
#skull name

def skull_name():
    os.system("clear")
    banner()
    print("")
    user = input(f" [{R}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{R}•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    skull_copy(user)
    bashrc(prompt)

#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#skull

def skull():
    skull_name()
    move()

#.............................................#
# Defining the function for creating external #
# file for the skull banner                   #
#.............................................#
# skull_copy

def skull_copy(user):
        with open("done4us","w") as external_file:
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

def skull(user):
    slowprints(f"""
                      {R}
                     uuuuu
                uu$$$$$$$$$$$uu
             uu$$$$$$$$$$$$$$$$$uu
            u$$$$$$$$$$$$$$$$$$$$$u
           u$$$$$$$$$$$$$$$$$$$$$$$u
          u$$$$$$$$$$$$$$$$$$$$$$$$$u
          u$$$$$$$$$$$$$$$$$$$$$$$$$u
          u$$$$$$“   “$$$“   “$$$$$$u
          “$$$$“      u$u       $$$$“
           $$$u       u$u       u$$$
           $$$u      u$$$u      u$$$
            “$$$$uu$$$   $$$uu$$$$“
             “$$$$$$$“   “$$$$$$$“
               u$$$$$$$u$$$$$$$u
                u$“$“$“$“$“$“$u
     uuu        $$u$ $ $ $ $u$$       uuu
    u$$$$        $$$$$u$u$u$$$       u$$$$
     $$$$$uu      “$$$$$$$$$“     uu$$$$$$
   u$$$$$$$$$$$uu    “““““    uuuu$$$$$$$$$$
   $$$$“““$$$$$$$$$$uuu   uu$$$$$$$$$“““$$$“
    “““      ““$$$$$$$$$$$uu ““$“““
              uuuu ““$$$$$$$$$$uuu
     u$$$uuu$$$$$$$$$uu ““$$$$$$$$$$$uuu$$$
     $$$$$$$$$$““““           ““$$$$$$$$$$$“
      “$$$$$“                      ““$$$$““
        $$$“                         $$$$“
   {a}...::::[ Powered by Done4us YouTube ]::::...{W}
         {W} [{Bg_R}  Username : {user}  {W}]\\n""")

skull(user)'''
            print(f'user = "{user}"\n', add_text, file=external_file)
            external_file.close()

#...........................................#
# Defining the function for asking the user #
# input about username or prompt name for   #
# the skull banner and also execute the     #
# load() and inst() funtion created inside  #
# this script for some purpose              #
#...........................................#
#dog name

def dog_name():
    os.system("clear")
    banner()
    print("")
    user = input(f" [{R}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{R}•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    dog_copy(user)
    bashrc(prompt)

#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#dog

def dog():
    dog_name()
    move()

#.............................................#
# Defining the function for creating external #
# file for the dog banner                     #
#.............................................#
# dog_copy

def dog_copy(user):
        with open("done4us","w") as external_file:
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

def dog(user):
    slowprints(f"""
                            {R}
                            _
                         ,:'/   _..._
                        // ( `""-.._.'
                       \\| /    6\\___
                       |     6      4
                       |            /
                       \\_       .--'
                       (_'---'`)
                       / `'---`()
                     ,'        |
     ,            .'`          |
     )\\       _.-'             ;
    / |    .'`   _            /
  /` /   .'       '.        , |
 /  /   /           \\   ;   | |
 |  \\  |            |  .|   | |
  \\  `"|           /.-' |   | |
   '-..-\\       _.;.._  |   |.;-.
         \\    <`.._  )) |  .;-. ))
         (__.  `  ))-'  \\_    ))'
             `'--"`       `“““`
{a}...::::[ Powered by Done4us YouTube ]::::...{W}
      {W} [{Bg_R}  Username : {user}  {W}]\\n""")

dog(user)'''
            print(f'user = "{user}"\n', add_text, file=external_file)
            external_file.close()


#..................................#
# Defining the function for        #
# Moving the created external file #
# to the $PREFIX/etc for easy call #
# of this file from bash.bashrc    #
#..................................#
# moving file to $PREFIX/etc

def move():
    os.system("mv done4us $PREFIX/etc")
    os.system("mv bash.bashrc $PREFIX/etc")




def bashrc(prompt):
        with open("bash.bashrc","w") as external_file:
            add_text ='''\n

######################################

# Command history tweaks:
# - Append history instead of overwriting
#   when shell exits.
# - When using history substitution, do not
#   exec command immediately.
# - Do not save to history commands starting
#   with space.
# - Do not save duplicated commands.
shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

# Default command line prompt.
#PROMPT_DIRTRIM=2
#PS1='\\[\\e[0;32m\\]\\w\\[\\e[0m\\] \\[\\e[0;97m\\]\\$\\[\\e[0m\\] '

# Handles nonexistent commands.
# If user has entered command which invokes non-available
# utility, command-not-found will give a package suggestions.
if [ -x @TERMUX_PREFIX@/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                @TERMUX_PREFIX@/libexec/termux/command-not-found "$1"
        }
fi

clear

python $PREFIX/etc/done4us


PS1='\\033[1;34m\\]╭───\\[\\033[1;31m\\]≼\\[\\033[1;33m\\]$prompt\\[\\033[1;34m\\]•\\[\\033[1;30m\\]\\w\\[\\033[1;31m\\]≽
\\[\\033[1;34m\\]╰──╼\\[\\033[1;31m\\]✠\\[\\033[0m\\] '


alias a=alias
alias c=clear
alias py=python
alias ba=bash

'''
            print(f'prompt="{prompt}"\n', add_text, file=external_file)
            external_file.close()


#....................................#
# Defining the function for choosing #
# option for user's to choose the    #
# banners according to him           #
#....................................#
# Choose

def choose():
    print("")
    no = input(f"{W} [{R}home{W}~{Bold_GR}theme{W}] > ")
    if no == '1' or no == '01':
       skull()
    elif no == '2' or no == '02':
        dog()
    else:
       menu()

#.......................................#
# Defining the function for the options #
# for user's to see the suitable        #
# banners for his/her terminal          #
#.......................................#
# Tool Menu

def menu():
    os.system("clear")
    banner()
    slowprints(f'''{R}╔═════════════{W}•─[{Bg_R} LIST THEME {W}]─•{R}════════════•
│
├─[{W}1{R}] {W}Skull
{R}├─────────────────────────[{W}2{R}] {W}Dog
{R}├─[{W}3{R}] {W}Anonymous
{R}├─────────────────────────[{W}4{R}] {W}Github
{R}├─[{W}5{R}] {W}Dragon
{R}├─────────────────────────[{W}6{R}] {W}Skull(1)
{R}├─[{W}7{R}] {W}Umbrella
{R}├─────────────────────────[{W}8{R}] {W}Geometric
{R}│
├─[{W}9{R}] {W}Support Me On {Bg_R} YouTube {W}
{R}└─[{W}0{R}] {W}Exit''')
    choose()

#................................#
# Defining the fuction for login #
# credential for verifying that  #
# he know's the usage of this    #
# tools on his/her terminal      #
#................................#
# login function

def login():
    banner()
    password = input(f"""{W}╔══════════⟨ {Bg_R} L O G I N  T O O L S {W} ⟩══════════•
│
└─⟩{R} """)
    if password == 'done4us':
       time.sleep(2)
       print("")
       print(f"{G}✓ {W}Login Success")
       time.sleep(1)
       print("")
       os.system("clear")
       time.sleep(0.8)
       menu()
    else:
       time.sleep(2)
       print("")
       print(f"{R}X {W}Login Failed")
       time.sleep(2)
       os.system("python red_white_theme.py")

#.....................#
# calling the defined #
# fuction's for start #
# working this tools  #
#.....................#
login()
