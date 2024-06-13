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
        time.sleep(0.0001)

os.system("clear")
time.sleep(1)


#...................................#
# Defining the function for showing #
# loading effect on a terminal      #
#...................................#
#loading effect

def load():
    load = f'{G}.'
    count = 0
    for t in range(20):
             time.sleep(0.3)
             print(f'\r {G}[{W}●{G}] {W}Loading {load}', end='', flush=True)
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

{G} ████████ ██   ██ ███████ {W}{W} ███    ███ ███████ 
{G}    ██    ██   ██ ██      {W}{W} ████  ████ ██      
{G}    ██    ███████ █████   {W}{W} ██ ████ ██ █████ 
{G}    ██    ██   ██ ██      {W}{W} ██  ██  ██ ██    
{G}    ██    ██   ██ ███████ {W}{W} ██      ██ ███████

{G} ●{W} Author    AnonymousCoder      {Bold_GR} Version 0.0.1
{G} ●{W} YouTube   Done4us
{G} ●{W} Instagram @done4us18''')


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
    print(f"{W} Theme Installed {G}Successfully {W}!")
    print("")
    input(f"{W} [{G}home{W}~{Bold_GR}theme{W}] > ")
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
    user = input(f" [{G}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{G}•{W}] Prompt Name : ")
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
        time.sleep(0.0001)

os.system("clear")
time.sleep(1)

def skull(user):
    slowprints(f"""
                      {G}
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
           {W} [{Bg_GR}  Username : {user}  {W}]\\n""")

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
    user = input(f" [{G}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{G}•{W}] Prompt Name : ")
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
        time.sleep(0.0001)

os.system("clear")
time.sleep(1)

def dog(user):
    slowprints(f"""
                            {G}
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
        {W} [{Bg_GR}  Username : {user}  {W}]\\n""")

dog(user)'''
            print(f'user = "{user}"\n', add_text, file=external_file)
            external_file.close()


#...........................................#
# Defining the function for asking the user #
# input about username or prompt name for   #
# the skull banner and also execute the     #
# load() and inst() funtion created inside  #
# this script for some purpose              #
#...........................................#
#anonymous name

def anonymous_name():
    os.system("clear")
    banner()
    print("")
    user = input(f" [{G}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{G}•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    anonymous_copy(user)
    bashrc(prompt)


#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#anonymous

def anonymous():
    anonymous_name()
    move()

#.............................................#
# Defining the function for creating external #
# file for the anonymous banner                  #
#.............................................#
# anonymous_copy

def anonymous_copy(user):
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

D = "}"
E = "{"

#######################################

#module
import os,sys,time

def slowprints(a):
    for b in a + '\\n':
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.0001)

os.system("clear")
time.sleep(1)

def anonymous(user):
    slowprints(f"""
                 {G}
                  .-/+osssso+/-`
             `/sdNMMMMMMMMMMMMMMNds/`
          .odMMMMMMMMMMMMMMMMMMMMMMMMdo.
        :hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh:
      -dMMMNmMMMMMMMNNNNNNNNNNMMMMMMMmNMMMd-
    `sMNNs-oMMMMNNNNNNNNNNNNNNNNNNMMMMo-sNNMs
   `dM+s-:sMMMNNNNNNMMNMNNMNMMNNNNNNMMMs-:s+Md`
  `mho.h/:dMNNMMMNMMNmNoso-dmNMMNMMMNNMd:/d`ohm`
  hs//::oMMNMMMMNMMMMNMmmo+NNMMMMNMMMMNMNo:-+:yh
 /M--y+:hMNNNNNNNMMMNNMMmmMMNMMMMNNNNNNNMh:oy.:M:
 dd+./.hMNMMMMMNMMMNNNNNooNNNNNMMMNMMMMMNMy./.odh
`M-m-/yyMNMMMMMNMMMMNMNdssdNMNMMMMNMMMMMNMyy/-m-N
`M:-ho`NMNNNNNNNNNmho-sN:/Ms-shmNNNNNNNNNMm`sh-/M`
`Mh`+ sdMNMMMMMh`     NMosMN     `dMMMMMNMdo`/`hN
 d/h/.m.MNMMMMM+      yM--My      oMMMMMNM.m`/h/h
 /d`/ss mNNNNNN-      `d.-h`      -NNNNNNd ss/`d:
  hm/`+ d:mNMMN                    NMMNd:h`+`/mh
  `doss/++.mNNh                    hNNm`o//ssod`
   `ds.:+y-:sso                    osy:-y+--sd`
     sMy+/:./+                      +/.:/+yMs
      -dyo/////.```            ```./////ohh-
        :hMhoosss/`            `/sssoohMh:
          .ohysoos.            .soosyh+`
             `/sdN`            `Nds/`
                     `Done4us

{a}...::::[ Powered by Done4us YouTube ]::::...{W}
        {W} [{Bg_GR}  Username : {user}  {W}]\\n""")

anonymous(user)'''
            print(f'user = "{user}"\n', add_text, file=external_file)
            external_file.close()




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
    banner()
    print("")
    user = input(f" [{G}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{G}•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    github_copy(user)
    bashrc(prompt)


#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#github

def github():
    github_name()
    move()

#.............................................#
# Defining the function for creating external #
# file for the github banner                  #
#.............................................#
# github_copy

def github_copy(user):
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

D = "}"
E = "{"

#######################################

#module
import os,sys,time

def slowprints(a):
    for b in a + '\\n':
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.0001)

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





#...........................................#
# Defining the function for asking the user #
# input about username or prompt name for   #
# the skull banner and also execute the     #
# load() and inst() funtion created inside  #
# this script for some purpose              #
#...........................................#
#dragon name

def dragon_name():
    os.system("clear")
    banner()
    print("")
    user = input(f" [{G}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{G}•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    dragon_copy(user)
    bashrc(prompt)


#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#dragon

def dragon():
    dragon_name()
    move()

#.............................................#
# Defining the function for creating external #
# file for the dragon banner                  #
#.............................................#
# dragon_copy

def dragon_copy(user):
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

D = "{D, {"

#######################################

#module
import os,sys,time

def slowprints(a):
    for b in a + '\\n':
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.0001)

os.system("clear")
time.sleep(1)

def dragon(user):
    slowprints(f"""
                {G}
            ______________
      ,===:'.,            \`-._
           \`:.\`---.__         \`-._
             \`:.     \`--.         \`.
               \\.        \`.         \`.
       (,,(,    \\.         \`.   ____,-\`.,
    (,'     \`/   \\.   ,--.___\`.'
,  ,'  ,--.  \`,   \\.;'         \`
 \`{D  }    \\  :    \\;
   V,,'    /  /    //    \`Done4us
   j;;    /  ,' ,-//.    ,---.      ,
   \\;'   /  ,' /  _  \\  /  _  \\   ,'/
         \\   \`'  / \\  \`'  / \\  \`.' /
          \`.___,'   \`.__,'   \`.__,'
{a}...::::[ Powered by Done4us YouTube ]::::...{W}
        {W} [{Bg_GR}  Username : {user}  {W}]\\n""")

dragon(user)'''
            print(f'user = "{user}"\n', add_text, file=external_file)
            external_file.close()



#...........................................#
# Defining the function for asking the user #
# input about username or prompt name for   #
# the skull banner and also execute the     #
# load() and inst() funtion created inside  #
# this script for some purpose              #
#...........................................#
#dragon2 name

def dragon2_name():
    os.system("clear")
    banner()
    print("")
    user = input(f" [{G}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{G}•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    dragon2_copy(user)
    bashrc(prompt)


#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#dragon2

def dragon2():
     dragon2_name()
     move()

#.............................................#
# Defining the function for creating external #
# file for the dragon2 banner                  #
#.............................................#
# dragon2_copy

def dragon2_copy(user):
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

D = "{D, {"


#######################################

#module
import os,sys,time

def slowprints(a):
    for b in a + '\\n':
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.0001)

os.system("clear")
time.sleep(1)

def dragon2(user):
    slowprints(f"""
                {G}
             \\                  /
    _________))                ((__________
   /.-------./\\\\\\\\    \\    /    //\\.--------.\\\\
  //#######//##\\\\\\\\   ))  ((   //##\\\\\\\\########\\\\\\\\
 //#######//###((  ((    ))  ))###\\\\\\\\########\\\\\\\\
((#######((#####\\\\\\\\  \\\\\\\\  //  //#####))########))
 \\##' `###\\######\\\\  \\)(/  //######/####' \`##/
  )'    ``#)'  `##\\\`->oo<-'/##'  `(#''     `(
          (       ``\\\`..'/''       )
                     \\\\\"\"(
                      `- )
                      / /     `Done4us
                     ( /\\\\
                     /\\| \\\\
                    (  \\\\
                        )
                       /
                      (
                      `
{a}...::::[ Powered by Done4us YouTube ]::::...{W}
        {W} [{Bg_GR}  Username : {user}  {W}]\\n""")

dragon2(user)'''
            print(f'user = "{user}"\n', add_text, file=external_file)
            external_file.close()




#...........................................#
# Defining the function for asking the user #
# input about username or prompt name for   #
# the skull banner and also execute the     #
# load() and inst() funtion created inside  #
# this script for some purpose              #
#...........................................#
#dragon3 name

def dragon3_name():
    os.system("clear")
    banner()
    print("")
    user = input(f" [{G}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{G}•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    dragon3_copy(user)
    bashrc(prompt)


#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#dragon3

def dragon3():
     dragon3_name()
     move()


#.............................................#
# Defining the function for creating external #
# file for the dragon3 banner                  #
#.............................................#
# dragon3_copy

def dragon3_copy(user):
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
        time.sleep(0.0001)

os.system("clear")
time.sleep(1)

def dragon3(user):
    slowprints(f"""
                {G}
                 ___====-_  _-====___
           _--^^^#####//      \\\\\\\\#####^^^--_
        _-^##########// (    ) \\\\\\\\##########^-_
       -############//  |\\^^/|  \\\\\\\\############-
     _/############//   (@::@)   \\\\\\\\############\\_
    /#############((     \\\\\\\\//     ))#############\\\\
   -###############\\\\\\\\    (oo)    //###############-
  -#################\\\\\\\\  / VV \\  //#################-
 -###################\\\\\\\\/      \\//###################-
_#/|##########/\\######(   /\\   )######/\\##########|\\#_
|/ |#/\\#/\\#/\\/  \\#/\\##\\  |  |  /##/\\#/  \\/\\#/\\#/\\#| \\|
`  |/  V  V  `   V  \\#\\| |  | |/#/  V   '  V  V  \\|  '
   `   `  `      `   / | |  | | \\   '      '  '   '
                    (  | |  | |  )
                   __\\ | |  | | /__   \`Done4us
                  (vvv(VVV)(VVV)vvv)

 {a}...::::[ Powered by Done4us YouTube ]::::...{W}
         {W} [{Bg_GR}  Username : {user}  {W}]\\n""")

dragon3(user)'''
            print(f'user = "{user}"\n', add_text, file=external_file)
            external_file.close()




#...........................................#
# Defining the function for asking the user #
# input about username or prompt name for   #
# the skull banner and also execute the     #
# load() and inst() funtion created inside  #
# this script for some purpose              #
#...........................................#
#dragon4 name

def dragon4_name():
    os.system("clear")
    banner()
    print("")
    user = input(f" [{G}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{G}•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    dragon4_copy(user)
    bashrc(prompt)


#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#dragon4

def dragon4():
     dragon4_name()
     move()


#.............................................#
# Defining the function for creating external #
# file for the dragon4 banner                  #
#.............................................#
# dragon4_copy

def dragon4_copy(user):
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
        time.sleep(0.0001)

os.system("clear")
time.sleep(1)

def dragon4(user):
    slowprints(f"""
                {G}
                 /|         |\\\\
               _/ |         | \\_
             _/_  | (    )  |  _\\_
           _/_/ | / |\\^^/|  \\ | \\_\\_
         _/_/   |/  (>::<)   ||   \\_\\_
       _/_/   | ||   \\\\\\\\//    || |   \\_\\_
      /_/   | |||\\  /   \\  __/||| |   \\_\\\\
     //     ||||| \\/     \\/   |||||     \\\\\\\\
    // __ | ||||\\             /|||| | __ \\\\\\\\
   //_/  \\|||||\\/\\           /\\/|||||/  \\_\\\\\\\\
  ///     \\\\\\\\\\\\\\\\/  | `Done4us |  \\////      \\\\\\\\\\\\\\

 |/        \\/    \\          /   \\/          \\|
                  \\        /
                  /_|  | |_|
                 ///_| |_| |\\\\\\\\
                 |//|||| |\\/\\|
                  / \\/|||/||
                   /|/\\| \\/
                     \\/  |

{a}...::::[ Powered by Done4us YouTube ]::::...{W}
        {W} [{Bg_GR}  Username : {user}  {W}]\\n""")

dragon4(user)'''
            print(f'user = "{user}"\n', add_text, file=external_file)
            external_file.close()




def dragons_choose():
    print("")
    no = input(f"{W} [{G}home{W}~{Bold_GR}theme{W}] > ")
    if no == '1' or no == '01':
        dragon()
    elif no == '2' or no == '02':
        dragon2()
    elif no == '3' or no == '03':
        dragon3()
    elif no == '4' or no == '04':
        dragon4()
    elif no == '0' or no == '00':
        menu()
    else :
        dragons()

def dragons():
    os.system("clear")
    banner()
    slowprints(f'''{G}╔═════════════{W}•─[{Bg_GR} DRAGONS THEMES {W}]─•{G}════════════•
│
├─────────────────[{W}1{G}] {W}Dragon (1)
{G}├─────────────────[{W}2{G}] {W}Dragon (2)
{G}├─────────────────[{W}3{G}] {W}Dragon (3)
{G}├─────────────────[{W}4{G}] {W}Dragon (4)
{G}│
{G}└───[{W}0{G}] {W}Back to Main Menu''')
    dragons_choose()




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
    banner()
    print("")
    user = input(f" [{G}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{G}•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    butterfly_copy(user)
    bashrc(prompt)

#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#butterfly

def butterfly():
    butterfly_name()
    move()

#.............................................#
# Defining the function for creating external #
# file for the butterfly banner                  #
#.............................................#
# butterfly_copy

def butterfly_copy(user):
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

D = "}"
E = "{"

#######################################

#module
import os,sys,time

def slowprints(a):
    for b in a + '\\n':
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.0001)

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
    banner()
    print("")
    user = input(f" [{G}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{G}•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    butterfly2_copy(user)
    bashrc(prompt)


#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#butterfly2

def butterfly2():
     butterfly2_name()
     move()

#.............................................#
# Defining the function for creating external #
# file for the butterfly2 banner                  #
#.............................................#
# butterfly2_copy

def butterfly2_copy(user):
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

D = "}"
E = "{"

#######################################

#module
import os,sys,time

def slowprints(a):
    for b in a + '\\n':
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.0001)

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
    banner()
    slowprints(f'''{G}╔═════════════{W}•─[{Bg_GR} ButterflyS THEMES {W}]─•{G}════════════•
│
├─────────────────[{W}1{G}] {W}Butterfly (1)
{G}├─────────────────[{W}2{G}] {W}Butterfly (2)
{G}│
{G}└───[{W}0{G}] {W}Back to Menu''')
    butterflys_choose()





#...........................................#
# Defining the function for asking the user #
# input about username or prompt name for   #
# the skull banner and also execute the     #
# load() and inst() funtion created inside  #
# this script for some purpose              #
#...........................................#
#alien name

def alien_name():
    os.system("clear")
    banner()
    print("")
    user = input(f" [{G}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{G}•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    alien_copy(user)
    bashrc(prompt)


#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#alien

def alien():
    alien_name()
    move()

#.............................................#
# Defining the function for creating external #
# file for the alien banner                  #
#.............................................#
# alien_copy

def alien_copy(user):
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

D = "}"
E = "{"

#######################################

#module
import os,sys,time

def slowprints(a):
    for b in a + '\\n':
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.0001)

def alien(user):
    slowprints(f"""
                 {G}
                 _____
             ,-\"     \"-.
            / o       o \\\\
           /   \\     /   \\\\
          /     )-\"-(     \\\\
         /     ( 6 6 )     \\\\
        /       \\ \" /       \\\\
       /         )=(         \\\\
      /   o   .--\"-\"--.   o   \\\\
     /    I  /  -   -  \\  I    \\\\
 .--(    (_{D}y/\\       /\\y{E}_)    )--.
(    \".___l\\/__\\_____/__\\/l___,\"    )
 \\                                 /
  \"-._      o O o O o O o      _,-\"
      `--Y--.___________.--Y--'
         |==.___________.==|
         `==.___________.=='
              `Done4us

{a}...::::[ Powered by Done4us YouTube ]::::...{W}
        {W} [{Bg_GR}  Username : {user}  {W}]\\n""")

alien(user)'''
            print(f'user = "{user}"\n', add_text, file=external_file)
            external_file.close()



#...........................................#
# Defining the function for asking the user #
# input about username or prompt name for   #
# the skull banner and also execute the     #
# load() and inst() funtion created inside  #
# this script for some purpose              #
#...........................................#
#alien2 name

def alien2_name():
    os.system("clear")
    banner()
    print("")
    user = input(f" [{G}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{G}•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    alien2_copy(user)
    bashrc(prompt)


#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#alien2

def alien2():
     alien2_name()
     move()

#.............................................#
# Defining the function for creating external #
# file for the alien2 banner                  #
#.............................................#
# alien2_copy

def alien2_copy(user):
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

D = "}"
E = "{"

#######################################

#module
import os,sys,time

def slowprints(a):
    for b in a + '\\n':
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.0001)

os.system("clear")
time.sleep(1)

def alien2(user):
    slowprints(f"""
                {G}

                  o   o
                   )-(
                  (O O)
                   \\=/
                  .-\"-.
                 //\\ /\\\\\\\\
               _// / \\ \\\\_
              =./ {E},-.{D} \\.=
                  || ||
                  || ||
                __|| ||__  `Done4us
               `---\" \"---'
{a}...::::[ Powered by Done4us YouTube ]::::...{W}
        {W} [{Bg_GR}  Username : {user}  {W}]\\n""")

alien2(user)'''
            print(f'user = "{user}"\n', add_text, file=external_file)
            external_file.close()




#...........................................#
# Defining the function for asking the user #
# input about username or prompt name for   #
# the skull banner and also execute the     #
# load() and inst() funtion created inside  #
# this script for some purpose              #
#...........................................#
#alien3 name

def alien3_name():
    os.system("clear")
    banner()
    print("")
    user = input(f" [{G}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{G}•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    alien3_copy(user)
    bashrc(prompt)


#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#alien3

def alien3():
     alien3_name()
     move()


#.............................................#
# Defining the function for creating external #
# file for the alien3 banner                  #
#.............................................#
# alien3_copy

def alien3_copy(user):
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
        time.sleep(0.0001)

os.system("clear")
time.sleep(1)

def alien3(user):
    slowprints(f"""
                {G}
      _                      _______                      _
   _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
  dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
  V      ~\"Mb          dOOOOOOOOOOOOOOOOOb          dM\"~      V
           `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
            `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
       __     `YMMM| OP'~\"YOOOOOOOOOOOP\"~`YO |MMMP'     __
     ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
  _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._
 <MMP'     `~YMMa_   YOOo   @  OOO  @   oOOP   _adMP~'      `YMM>
              `YMMMM\\`OOOo     OOO     oOOO'/MMMMP'
      ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
    ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
   ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
   MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
   YMb           ~YMMMM\\`OOOOI`````IOOOOO'/MMMMP~           dMP
    `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
      `'                  `OObNNNNNdOO'                   `'
                            `~OOOOO~'

 {a}...::::[ Powered by Done4us YouTube ]::::...{W}
         {W} [{Bg_GR}  Username : {user}  {W}]\\n""")

alien3(user)'''
            print(f'user = "{user}"\n', add_text, file=external_file)
            external_file.close()




def aliens_choose():
    print("")
    no = input(f"{W} [{G}home{W}~{Bold_GR}theme{W}] > ")
    if no == '1' or no == '01':
        alien()
    elif no == '2' or no == '02':
        alien2()
    elif no == '3' or no == '03':
        alien3()
    else :
        aliens()

def aliens():
    os.system("clear")
    banner()
    slowprints(f'''{G}╔═════════════{W}•─[{Bg_GR} alienS THEMES {W}]─•{G}════════════•
│
├─────────────────[{W}1{G}] {W}Alien (1)
{G}├─────────────────[{W}2{G}] {W}Alien (2)
{G}├─────────────────[{W}3{G}] {W}Alien (3)
{G}│
{G}└───[{W}0{G}] {W}Back to Menu''')
    aliens_choose()




#...........................................#
# Defining the function for asking the user #
# input about username or prompt name for   #
# the skull banner and also execute the     #
# load() and inst() funtion created inside  #
# this script for some purpose              #
#...........................................#
#geometric name

def geometric_name():
    os.system("clear")
    banner()
    print("")
    user = input(f" [{G}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{G}•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    geometric_copy(user)
    bashrc(prompt)


#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#geometric

def geometric():
    geometric_name()
    move()

#.............................................#
# Defining the function for creating external #
# file for the geometric banner                     #
#.............................................#
# geometric_copy

def geometric_copy(user):
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
        time.sleep(0.0001)

os.system("clear")
time.sleep(1)

def geometric(user):
    slowprints(f"""
                  {G}
                 ______
                /     /\\\\
               /     /##\\\\
              /     /####\\\\
             /     /######\\\\
            /     /########\\\\
           /     /##########\\\\
          /     /#####/\\#####\\\\
         /     /#####/++\\#####\\\\
        /     /#####/++++\\#####\\\\
       /     /#####/\\+++++\\#####\\\\
      /     /#####/  \\+++++\\#####\\\\
     /     /#####/    \\+++++\\#####\\\\
    /     /#####/      \\+++++\\#####\\\\
   /     /#####/        \\+++++\\#####\\\\
  /     /#####/__________\\+++++\\#####\\\\
 /            `Done4us    \\+++++\\#####\\\\
/__________________________\\+++++\\####/
\\+++++++++++++++++++++++++++++++++\\##/
 \\+++++++++++++++++++++++++++++++++\\/
  ``````````````````````````````````
{a}...::::[ Powered by Done4us YouTube ]::::...{W}
        {W} [{Bg_GR}  Username : {user}  {W}]\\n""")

geometric(user)'''
            print(f'user = "{user}"\n', add_text, file=external_file)
            external_file.close()







#...........................................#
# Defining the function for asking the user #
# input about username or prompt name for   #
# the skull banner and also execute the     #
# load() and inst() funtion created inside  #
# this script for some purpose              #
#...........................................#
#gun name

def gun_name():
    os.system("clear")
    banner()
    print("")
    user = input(f" [{G}•{W}] Username    : ")
    time.sleep(0.3)
    prompt = input(f" [{G}•{W}] Prompt Name : ")
    print("")
    time.sleep(1)
    load()
    inst()
    gun_copy(user)
    bashrc(prompt)


#...........................#
# Defining the function for #
# executing the skull_name  #
# function created above    #
#...........................#
#gun

def gun():
    gun_name()
    move()

#.............................................#
# Defining the function for creating external #
# file for the gun banner                     #
#.............................................#
# gun_copy

def gun_copy(user):
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
        time.sleep(0.0001)

os.system("clear")
time.sleep(1)

def gun(user):
    slowprints(f"""
                {G}
	   _=__________________________-
	  /  ////  (____)\`Done4us ____ |
	 _|_////_________________(____|
	    )/  o  /) /  )/
	   (/     /)__\\_))
	  (/     /)
	 (/     /)
	(/_ o _/)
	--------
{a}...::::[ Powered by Done4us YouTube ]::::...{W}
        {W} [{Bg_GR}  Username : {user}  {W}]\\n""")

gun(user)'''
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


PS1='\\033[1;34m\\]╭───\\[\\033[1;32m\\]≼\\[\\033[1;33m\\]$prompt\\[\\033[1;34m\\]•\\[\\033[1;30m\\]\\w\\[\\033[1;32m\\]≽
\\[\\033[1;34m\\]╰──╼\\[\\033[1;32m\\]✠\\[\\033[0m\\] '


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
    no = input(f"{W} [{G}home{W}~{Bold_GR}theme{W}] > ")
    if no == '1' or no == '01':
       skull()
    elif no == '2' or no == '02':
        dog()
    elif no == '3' or no == '03':
        anonymous()
    elif no == '4' or no == '03':
        github()
    elif no == '5' or no == '05':
        dragons()
    elif no == '6' or no == '06':
        butterflys()
    elif no == '7' or no == '07':
        aliens()
    elif no == '8' or no == '08':
        geometric()
    elif no == '9' or no == '09':
        gun()
    elif no == '99':
        os.system("xdg-open https://www.youtube.com/channel/UC4479WTD05jcnlA0jxnqclg")
        time.sleep(1)
        menu()
    elif no == '0' or no == '00':
        os.system("exit")
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
    slowprints(f'''{G}╔═════════════{W}•─[{Bg_GR} LIST THEME {W}]─•{G}════════════•
│
├──────────────────[{W}1{G}] {W}Skull
{G}├──────────────────[{W}2{G}] {W}Dog
{G}├──────────────────[{W}3{G}] {W}Anonymous
{G}├──────────────────[{W}4{G}] {W}Github
{G}├──────────────────[{W}5{G}] {W}Dragons
{G}├──────────────────[{W}6{G}] {W}Butterflys
{G}├──────────────────[{W}7{G}] {W}Aliens
{G}├──────────────────[{W}8{G}] {W}Geometric
{G}├──────────────────[{W}9{G}] {W}Gun
{G}│
{G}│
├────[{W}99{G}] {W}Support Me On {Bg_R} YouTube {W}
{G}└─────[{W}0{G}] {W}Exit''')
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
    password = input(f"""{W}╔══════════⟨ {Bg_GR} L O G I N  T O O L S {W} ⟩══════════•
│
└─⟩{G} """)
    if password == 'done4us' or password == 'Done4us' or password == 'DONE4US':
       time.sleep(1.5)
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
       os.system("python green_white_theme.py")

#.....................#
# calling the defined #
# fuction's for start #
# working this tools  #
#.....................#
login()
