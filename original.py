#modules

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
GR = "\x1b[37m"

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
    load = '\033[1;91m.'
    count = 0
    for t in range(20):
             time.sleep(0.3)
             print(f'\r \033[1;91m[{W}●\033[1;91m] {W}Loading {load}', end='', flush=True)
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

\033[1;91m ████████ ██   ██ ███████ {W}{W} ███    ███ ███████ 
\033[1;91m    ██    ██   ██ ██      {W}{W} ████  ████ ██      
\033[1;91m    ██    ███████ █████   {W}{W} ██ ████ ██ █████ 
\033[1;91m    ██    ██   ██ ██      {W}{W} ██  ██  ██ ██    
\033[1;91m    ██    ██   ██ ███████ {W}{W} ██      ██ ███████

\033[1;91m ●\033[0m Author  Rs1819             \033[1;90m Version 0.7.2
\033[1;91m ●\033[0m YouTube Done4us''')


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
    print(f"{W} Theme Installed \033[1;92mSuccessfully {W}!")
    print("")
    input(f"{W} [\033[1;91mhome{W}~\033[0;90mtheme{W}] > ")
    time.sleep(1)
    print("")

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
    user = input(f" [\033[1;91m•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [\033[1;91m•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    skull_copy(user)

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
GR = "\\x1b[37m"

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
                      {m}
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
            {W} [\\033[1;41m  Username : {user}  {W}]\\n""")

skull(user)'''
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


#....................................#
# Defining the function for choosing #
# option for user's to choose the    #
# banners according to him           #
#....................................#
# Choose

def choose():
    print("")
    no = input(f"{W} [\033[1;91mhome{W}~\033[0;90mtheme{W}] > ")
    if no == '1' or no == '01':
       skull()
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
    slowprints(f'''\033[91m╔═════════════{W}•─[\033[1;41m LIST THEME {W}]─•\033[91m════════════•
│
├─[{W}1\033[1;91] {W}Skull
\033[1;91m├─────────────────────────[{W}2\033[1;91m] {W}Skull(1)
\033[1;91m├─[{W}3\033[1;91m] {W}Anonymous
\033[1;91m├─────────────────────────[{W}4\033[1;91m] {W}Github
\033[1;91m├─[{W}5\033[1;91m] {W}Dragon
\033[1;91m├─────────────────────────[{W}6\033[1;91m] {W}Dog
\033[1;91m├─[{W}7\033[1;91m] {W}Umbrella
\033[1;91m├─────────────────────────[{W}8\033[1;91m] {W}Geometric
\033[1;91m│
├─[{W}9\033[1;91m] {W}Support Me On \033[1;41m YouTube {W}
\033[1;91m└─[{W}0\033[1;91m] {W}Exit''')
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
    password = input(f"""{W}╔══════════⟨ \033[1;41m L O G I N  T O O L S {W} ⟩══════════•
│
└─⟩ """)
    if password == 'done4us':
       time.sleep(2)
       print("")
       print(f"\033[1;92m✓ {W}Login Success")
       time.sleep(1)
       print("")
       os.system("clear")
       time.sleep(0.8)
       menu()
    else:
       time.sleep(2)
       print("")
       print("\033[1;91mX {W}Login Failed")
       time.sleep(2)
       os.system("python original.py")

#.....................#
# calling the defined #
# fuction's for start #
# working this tools  #
#.....................#
login()
