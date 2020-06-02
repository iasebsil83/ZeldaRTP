# -*- coding: cp1252 -*-
import os
import sys
from msvcrt import getch
currentPath = os.getcwd() + "\\_data\\"

maxh = 7
maxl = 21
class Screen:
    screen = ""
class gameCore2D_InConsole:
    def d2D(no,x,y,element):
        x -= 1
        y -= 1
        for a in range(len(element)):
            Screen.screen[y][x] = element[a]
            x += 1
    def show(no):
        for a in range(17):
            print("")
        line = []
        for a in range(maxh):
            line.append("")
        for a in range(maxh):
            for b in range(maxl):
                line[a] += Screen.screen[a][b]
        for a in range(maxh):
            print(line[a])
    def clear(no):
        Screen.screen = [[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]]
    def getKey(no):
        return ord(getch())
core = gameCore2D_InConsole()
def compil():
    saveFile = open(currentPath + "save.txt","w")
    saveFile.write(str(save) + ";" + str(lifeMax) + ";" + str(life) + ";" + str(story) + ";" + str(sword) + ";" + str(bomb) + ";" + str(hookshot) + ";" + str(voidKey) + ";" + str(warp) + ";" + str(HyGoing) + ";" + str(Wx) + ";" + str(Wy))
    saveFile.close()
#decompil
saveFile = open(currentPath + "save.txt","r")
content = saveFile.read().split(";")
global save,lifeMax,life,story,sword,bomb,hookshot,voidKey,warp,HyGoing,Wx,Wy
save = int(content[0])
lifeMax = int(content[1])
life = int(content[2])
story = int(content[3])
sword = int(content[4])
bomb = int(content[5])
hookshot = int(content[6])
voidKey = int(content[7])
warp = int(content[8])
HyGoing = int(content[9])
Wx = int(content[10])
Wy = int(content[11])
saveFile.close()
#
Wx = 0
Wy = 0
if save == 0:
    story = 0
    lifeMax = 3
life = lifeMax
core.clear()
core.d2D(3,2,"Appuyez sur une")
core.d2D(3,3,"touche que vous")
core.d2D(2,4,"n'utiliserez plus")
core.d2D(2,5,"de tout le jeu ...")
core.show()
core.clear()
voidKey = core.getKey()
core.d2D(1,1,"~~~~~~~~~~~~~~~~~~~~~")
core.d2D(1,2,"}The Lengend Of Link{")
core.d2D(1,3,"}Rescue The Princess{")
core.d2D(1,4,"~~~~~~~~~~~~~~~~~~~~~")
core.d2D(1,5,"}   Press any Key   {")
core.d2D(1,6,"}    To Continue    {")
core.d2D(1,7,"~~~~~~~~~~~~~~~~~~~~~")
core.show()
key = voidKey
while key == voidKey:
    key = core.getKey()
label = "theta"
while 1:
    if label == "theta":
        core.d2D(1,1,"~~~~~~~~~~~~~~~~~~~~~")
        core.d2D(1,2,"}Play        [enter]{")
        core.d2D(1,3,"~~~~~~~~~~~~~~~~~~~~~")
        core.d2D(1,4,"}Controls        [C]{")
        core.d2D(2,5,"                   ")
        if save != 0:
            core.d2D(2,5,"Reset           [L]")
        core.d2D(2,6,"Quit        [echap]")
        core.show()
        key = voidKey
        while key != 999:
            key = core.getKey()
            if key == 13:
                key = 999
                label = "S"
            elif key == 99:
                key = 999
                label = "C"
            elif key == 108:
                save = 0
                story = 0
                lifeMax = 3
                life = 3
                core.d2D(2,5,"                   ")
                core.show()
            elif key == 27:
                sys.exit()
            core.clear()
    if label == "C":
        core.d2D(1,1,"~~~~~~~~~~~~~~~~~~~~~")
        core.d2D(1,2,"}     Controls      {")
        core.d2D(1,3,"~~~~~~~~~~~~~~~~~~~~~")
        core.d2D(1,4,"}Inventory  ([I])   {")
        core.d2D(1,5,"}Save       ([L])   {")
        core.d2D(1,6,"}See items(3) [C]   {")
        core.d2D(1,7,"~~~~~~~~~~~~~~~~~~~~~")
        core.show()
        temp = 0
        key = voidKey
        while key != 99:
            key = core.getKey()
            if key == 27:
                key = 99
                label = "theta"
                temp = 1
        if temp == 0:
            core.d2D(1,1,"} Press [enter] to  {")
            core.d2D(1,2,"}  Configure (All)  {")
            core.d2D(1,4,"}1st item      [   ]{")
            core.d2D(1,5,"}2nd item      [   ]{")
            core.d2D(1,6,"}3rd item      [   ]{")
            core.d2D(17,4,str(sword))
            core.d2D(17,5,str(bomb))
            core.d2D(17,6,str(hookshot))
            core.show()
            key = voidKey
            while key != 27:
                key = core.getKey()
                if key == 13:
                    key = core.getKey()
                    sword = key
                    key = core.getKey()
                    bomb = key
                    key = core.getKey()
                    hookshot = key
                    core.d2D(17,4,str(sword))
                    core.d2D(17,5,str(bomb))
                    core.d2D(17,6,str(hookshot))
                    core.show()
            label = "C"
    if label == "S":
        compil()
        if save == 0:
            label = "B"
        elif save == 1:
            execfile(currentPath + "Zelda_KO.py")
        elif save == 2:
            execfile(currentPath + "Zelda_BO.py")
        elif save == 3:
            execfile(currentPath + "Zelda_HY.py")
        elif save == 4:
            execfile(currentPath + "Zelda_MT.py")
        elif save == 5:
            execfile(currentPath + "Zelda_GO.py")
        elif save == 6:
            execfile(currentPath + "Zelda_LA.py")
        elif save == 7:
            execfile(currentPath + "Zelda_ZO.py")
        elif save == 8:
            execfile(currentPath + "Zelda_CH.py")
    if label == "B":
        core.clear()
        core.d2D(1,5,"=======[enter]=======")
        core.d2D(1,6,"Il etait une fois ...")
        core.show()
        key = voidKey
        while key != 13:
            key =core.getKey()
        core.d2D(1,6,"Dans la foret Kokiri,")
        core.d2D(1,7," alors qu'un enfant  ")
        core.show()
        key = voidKey
        while key != 13:
            key = core.getKey()
        core.d2D(7,2,"O{-{")
        core.d2D(6,3,"()-----")
        core.d2D(6,4,"|     |")
        core.d2D(1,6,"dormait paisiblement,")
        core.d2D(1,7,"  un cri retentit :  ")
        core.show()
        key = voidKey
        while key != 13:
            key = core.getKey()
        core.d2D(1,6," `Link! Le venerable ")
        core.d2D(1,7," arbre Mojo est tres ")
        core.show()
        key = voidKey
        while key != 13:
            key = core.getKey()
        core.d2D(1,6,"malade.Il faut que tu")
        core.d2D(1,7," viennes le sauver!`")
        core.show()
        key = voidKey
        while key != 13:
            key = core.getKey()
        core.d2D(9,1,"O")
        core.d2D(6,2,"   { ")
        core.d2D(1,6,"     VIIIITE !!!     ")
        core.d2D(1,7,"                     ")
        core.show()
        key = voidKey
        while key != 13:
            key = core.getKey()
        execfile(currentPath + "Zelda_KO.py")
