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
core.clear()
x,y,bombCnt,bCooX = 2,6,0,0
if Wx != 0:
    x = Wx
    y = Wy
right = True
core.d2D(1,1,"Vie:")
core.d2D(1,7,"-----")
key = 1
while key != 105:
    if key != voidKey:
        for b in range(lifeMax):
            core.d2D(b+5,1,".")
        for b in range(life):
            core.d2D(b+5,1,"@")
        core.d2D(14,1,"        ")
        core.d2D(11,2,"          )")
        core.d2D(8,3,"       ,------")
        core.d2D(5,4,"       ,--      )")
        core.d2D(1,5,"        ,------------")
        core.d2D(1,6,"(    ,--")
    if key == 113:
        right = False
        x -= 1
        if (x == 5 and y == 5) or (x == 8 and y == 4) or (x == 11 and y == 3) or (x == 14 and y == 2):
            y += 1
    if key == 100:
        right = True
        x += 1
        if (x == 6 and y == 6) or (x == 9 and y == 5) or (x == 12 and y == 4) or (x == 15 and y == 3):
            y -= 1
    if key == sword and x != 1 and x != 21:
        core.d2D(x-1+(2*int(right)),6,"-")
    if key == bomb and bombCnt == 0 and x != 1 and x != 21 and story >= 3:
        bCooX = x-1+2*int(right)
        bombCnt = 5
    if bombCnt > 0:
        bombCnt -= 1
        core.d2D(bCooX,6,"O")
    if bombCnt == 1:
        core.d2D(bCooX,6,"X")
        if bCooX-1 != 0:
            core.d2D(bCooX-1,6,"X")
        if bCooX+1 != 22:
            core.d2D(bCooX+1,6,"X")
        if x == bCooX-1 or x == bCooX or x == bCooX+1:
            life -= 1
    if life == 0:
        Wx = 0
        Wy = 0
        save = 4
        compil()
        execfile(currentPath + "Zelda_0.py")
    if key == 111:
        save = 4
        compil()
        core.clear()
        core.d2D(4,3,"Party saved !")
        core.show()
        core.d2D(4,3,"             ")
        core.d2D(1,1,"Vie:")
        core.d2D(1,7,"-----")
        key = voidKey
        while key != 13:
            key = core.getKey()
    if key == 115 and x == 12:
        y += 1
    if story != 3:
        if x > 19 and y == 4:
            x = 19
        core.d2D(20,4,"(")
    if x < 2:
        HyGoing = 5
        Wx = 0
        Wy = 0
        compil()
        execfile(currentPath + "Zelda_HY.py")
    if x > 20:
        Wx = 0
        Wy = 0
        compil()
        if y == 4:
            execfile(currentPath + "Zelda_DO.py")
        elif y == 2:
            execfile(currentPath + "Zelda_GO.py")
    core.d2D(x,y-1,"0")
    if right == False:
        core.d2D(x,y,"}")
    else:
        core.d2D(x,y,"{")
    if key != voidKey:
        core.show()
    key = core.getKey()
warp = 5
Wx = x
Wy = y
compil()
execfile(currentPath + "Zelda_M.py")
