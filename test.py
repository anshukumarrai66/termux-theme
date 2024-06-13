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
#butterfly name

def butterfly_name():
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
    butterfly_copy(user)
#    bashrc(prompt)


#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#butterfly

def butterfly():
    butterfly_name()
#    move()

#.............................................#
# Defining the function for creating external #
# file for the butterfly banner                  #
#.............................................#
# butterfly_copy

def butterfly_copy(user):
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

def butterfly(user):
    slowprints(f"""
                 {G}

                `         '
;,,,             `       '             ,,,;
`Y888888bo.       :     :       .od888888Y'
  8888888888b.     :   :     .d8888888888
  88888Y'  `Y8b.   `   '   .d8Y'  `Y88888
 j88888  .db.  Yb. '   ' .dY  .db.  88888k
   `888  Y88Y    `b ( ) d'    Y88Y  888'
    888b  '\"        ,',        \"'  d888
   j888888bd8gf\"'   ':'   `\"?g8bd888888k
     'Y'   .8'     d' 'b     '8.   'Y'
      !   .8' db  d'; ;`b  db '8.   !
         d88  `'  8 ; ; 8  `'  88b
        d888b   .g8 ',' 8g.   d888b
       :888888888Y'     'Y888888888:
       '! 8888888'       `8888888 !'
          '8Y  `Y         Y'  Y8'
           Y                   Y
           !     `Done4us      !

{a}...::::[ Powered by Done4us YouTube ]::::...{W}
        {W} [{Bg_GR}  Username : {user}  {W}]\\n""")

butterfly(user)'''
            print(f'user = "{user}"\n', add_text, file=external_file)
            external_file.close()



#...........................................#
# Defining the function for asking the user #
# input about username or prompt name for   #
# the skull banner and also execute the     #
# load() and inst() funtion created inside  #
# this script for some purpose              #
#...........................................#
#butterfly2 name

def butterfly2_name():
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
    butterfly2_copy(user)
#    bashrc(prompt)


#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#butterfly2

def butterfly2():
     butterfly2_name()
#    move()

#.............................................#
# Defining the function for creating external #
# file for the butterfly2 banner                  #
#.............................................#
# butterfly2_copy

def butterfly2_copy(user):
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

def butterfly2(user):
    slowprints(f"""
                {G}
.==-.                   .-==.
  \\()8`-._  `.   .'  _.-'8()/
  (88\"   ::.  \\./  .::   \"88)
   \\_.'`-::::.(#).::::-'`._/
     `._... .q(_)p. ..._.'
       \"\"-..-'|=|`-..-\"\"
       .\"\"' .'|=|`. `\"\".
     ,':8(o)./|=|\\.(o)8:`.
    (O :8 ::/ \\_/ \\:: 8: O)
     \\O `::/       \\::' O/
      \"\"--'         `--\"\"
           `Done4us

{a}...::::[ Powered by Done4us YouTube ]::::...{W}
        {W} [{Bg_GR}  Username : {user}  {W}]\\n""")

butterfly2(user)'''
            print(f'user = "{user}"\n', add_text, file=external_file)
            external_file.close()




def butterflys_choose():
    print("")
    no = input(f"{W} [{G}home{W}~{Bold_GR}theme{W}] > ")
    if no == '1' or no == '01':
        butterfly()
    elif no == '2' or no == '02':
        butterfly2()
    else :
        butterflys()

def butterflys():
    os.system("clear")
#    banner()
    slowprints(f'''{G}╔═════════════{W}•─[{Bg_GR} ButterflyS THEMES {W}]─•{G}════════════•
│
├─────────────────[{W}1{G}] {W}Butterfly (1)
{G}├─────────────────[{W}2{G}] {W}Butterfly (2)
{G}│
{G}└───[{W}0{G}] {W}Back to Menu''')
    butterflys_choose()

butterflys()
