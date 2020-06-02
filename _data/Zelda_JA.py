# -*- coding: cp1252 -*-
import os
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
    saveFile = open("_data/save.txt","w")
    saveFile.write(str(save) + ";" + str(lifeMax) + ";" + str(life) + ";" + str(story) + ";" + str(sword) + ";" + str(bomb) + ";" + str(hookshot) + ";" + str(voidKey) + ";" + str(warp) + ";" + str(HyGoing) + ";" + str(Wx) + ";" + str(Wy))
    saveFile.close()
#decompil
saveFile = open("_data/save.txt","r")
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
x,y,hookOk,hookX,hookY,Bcnt,Bpos,Blife,unlocked = 2,7,0,0,0,0,21,5,0
if Wx != 0:
	x = Wx
	y = Wy
right = True
core.clear()
core.d2D(1,1,"Vie:")
key = 1
while key != 105:
    if key != voidKey:
        for b in range(lifeMax):
            core.d2D(b+5,1,".")
        for b in range(life):
            core.d2D(b+5,1,"@")
        core.d2D(1,2,"   [                 ")
        core.d2D(1,3,"   [                 ")
        core.d2D(1,4,"   [                 ")
        core.d2D(1,5,"   [                 ")
        core.d2D(1,6,"   [                 ")
        core.d2D(1,7,"(~~~~§~~~~~~~~~~~~~~~")
    if hookOk == 1:
        if key == 113 and hookX > 1 and hookX > x-5:
            hookX -= 1
        if key == 100 and hookX < 21 and hookX < x+5:
            hookX += 1
        if key == 122 and hookY > 1 and hookY > y-5:
            hookY -= 1
        if key == 115 and hookY < 7 and hookY < y+5:
            hookY += 1
        core.d2D(hookX,hookY,"+")
        if key == 13:
            hookOk = 0
            if hookX == 6 and hookY == 7:
                x = 6
                y = 7
                unlocked = 1
            if hookX == Bpos and hookY > 4:
                Blife -= 1
    else:
        if key == 113:
            right = False
            x -= 1
        if key == 100 and x < 21:
            right = True
            x += 1
        if key == sword and x != 1 and x != 21:
            core.d2D(x-1+(2*int(right)),7,"-")
    if key == hookshot and hookOk == 0:
        hookOk = 1
        hookX = x
        hookY = y
    if x == 4:
        if unlocked == 0:
            x = 3
        else:
            x = 5
    if x == 1:
        Wx = 0
        Wy = 0
        compil()
        execfile(currentPath + "Zelda_LA.py")
    if unlocked == 1:
        Bcnt += 1
    if Bcnt == 4:
        if x < Bpos:
            Bpos -= 1
        if x > Bpos:
            Bpos += 1
        if x == Bpos:
            life -= 1
        Bcnt = 0
    if Blife == 0:
        Wx = 0
        Wy = 0
        save = 7
        story = 7
        life = 6
        lifeMax = 6
        core.clear()
        core.d2D(5,3,"Party saved !")
        core.show()
        key = voidKey
        while key != 13:
            key = core.getKey()
        compil()
        execfile(currentPath + "Zelda_LA.py")
    if life == 0:
        Wx = 0
        Wy = 0
        save = 7
        compil()
        execfile(currentPath + "Zelda_0.py")
    if key == 111:
        core.clear()
        core.d2D(4,3,"Can't save here!")
        core.d2D(4,3,"                ")
        core.d2D(1,1,"Vie:")
        core.show()
        key = voidKey
        while key != 13:
            key = core.getKey()
    core.d2D(Bpos,5,"v")
    core.d2D(Bpos,6,"O")
    core.d2D(Bpos,7,"^")
    core.d2D(x,y-1,"0")
    if right == False:
        core.d2D(x,y,"}")
    else:
        core.d2D(x,y,"{")
    if key != voidKey:
        core.show()
    key = core.getKey()
warp = 10
Wx = x
Wy = y
compil()
execfile(currentPath + "Zelda_M.py")

