# -*- coding: cp1252 -*-
import os
currentPath = "/storage/emulated/0/qpython/projects/ZeldaRTP[1.3.2]/_data/"

i = 105
z = 122
q = 113
s = 115
d = 100
sauver = 111
k = 107
l = 108
m = 109
e = 13
esc = 27

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
        try:
            return input()
        except:
            return 0
core = gameCore2D_InConsole()
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
core.clear()
core.d2D(1,1,"~~~~~~~~Start~~~~~~~~")
for a in range(2,8):
    core.d2D(1,a,"}[")
    core.d2D(20,a,"]{")
if story >= 1:
    core.d2D(3,2,"Kokiri sword")
    core.d2D(3,3,"linked at :[   ]")
    core.d2D(15,3,str(sword))
if story >= 3:
    core.d2D(3,4,"Gorons bombs")
    core.d2D(3,5,"linked at :[   ]")
    core.d2D(15,5,str(bomb))
if story >= 6:
    core.d2D(3,6,"Hookshot")
    core.d2D(3,7,"linked at :[   ]")
    core.d2D(15,7,str(hookshot))
core.show()
key = voidKey
while key != 27:
    key = core.getKey()
if warp == 1:
    execfile(currentPath + "Zelda_KO.py")
if warp == 2:
    execfile(currentPath + "Zelda_BO.py")
if warp == 3:
    execfile(currentPath + "Zelda_AR.py")
if warp == 4:
    execfile(currentPath + "Zelda_HY.py")
if warp == 5:
    execfile(currentPath + "Zelda_MT.py")
if warp == 6:
    execfile(currentPath + "Zelda_GO.py")
if warp == 7:
    execfile(currentPath + "Zelda_DO.py")
if warp == 8:
    execfile(currentPath + "Zelda_LA.py")
if warp == 9:
    execfile(currentPath + "Zelda_ZO.py")
if warp == 10:
    execfile(currentPath + "Zelda_JA.py")
if warp == 11:
    execfile(currentPath + "Zelda_CH.py")
if warp == 12:
    execfile(currentPath + "Zelda_BF.py")
