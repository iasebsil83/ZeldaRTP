# -*- coding: cp1252 -*-
import os
from random import randint
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
core.clear()
x,sCooX,Bcnt,Blife,Bpos,unlocked = 2,2,0,10,21,0
if Wx != 0:
    x = Wx
    y = Wy
right = True
core.d2D(1,1,"Vie:")
for a in range(1,5):
    core.d2D(10,a,"!")
core.d2D(1,7,"---------------------")
key = 1
while key != 105:
    if key != voidKey or Bcnt == 2:
        for b in range(lifeMax):
            core.d2D(b+5,1,".")
        for b in range(life):
            core.d2D(b+5,1,"@")
        core.d2D(1,5,"                     ")
        core.d2D(1,6,"(  #  y              ")
    if key == 113:
        right = False
        x -= 1
    if key == 100 and x < 21:
        right = True
        x+= 1
    if x == 1:
        Wx = 0
        Wy = 0
        compil()
        execfile(currentPath + "Zelda_KO.py")
    if x > 9 and unlocked == 0:
        x = 9
    if x < 11 and unlocked == 2:
        x = 11
    if x == 22:
        x = 21
    if key == sword:
        sCooX = x
        if right == False and x > 1:
            sCooX -= 1
        if right == True and x < 21:
            sCooX += 1
        core.d2D(sCooX,6,"-")
        if sCooX == Bpos:
            Blife -= 1
        if sCooX == 4:
            life += 1
        if sCooX == 7:
            core.d2D(10,6," ")
            unlocked = 1
    if Blife == 0:
        lifeMax = 4
        life = 4
        story = 2
        Wx = 0
        Wy = 0
        save = 1
        core.clear()
        core.d2D(5,3,"Party saved !")
        core.show()
        key = voidKey
        while key != 13:
            key = core.getKey()
        compil()
        execfile(currentPath + "Zelda_KO.py")
    if unlocked == 1 and x > 10:
        unlocked = 2
    if unlocked == 2:
        Bcnt += 1
    if Bcnt == 3:
        Bcnt = randint(0,1)
        if Bcnt == 0 and Bpos > 11:
            Bpos -= 1
        if Bcnt == 1 and Bpos < 21:
            Bpos += 1
        Bcnt = 0
        if Bpos == x:
            life -= 1
    if life == 0:
        Wx = 0
        Wy = 0
        save = 1
        compil()
        execfile(currentPath + "Zelda_0.py")
    if life > lifeMax:
        life = lifeMax
    if x == 10 and unlocked != 1:
        if unlocked == 0:
            x = 9
        else:
            x = 11
    if key == 111:
        core.clear()
        core.d2D(4,3,"Can't save here!")
        core.show()
        core.d2D(4,3,"                ")
        core.d2D(1,7,"---------------------")
        core.d2D(1,1,"Vie:")
        key = voidKey
        while key != 13:
            key = core.getKey()
    if unlocked != 1:
        core.d2D(10,6,"!")
    core.d2D(Bpos,5,"é")
    core.d2D(Bpos,6,"/")
    core.d2D(x,y-1,"0")
    if right == False:
        core.d2D(x,y,"}")
    else:
        core.d2D(x,y,"{")
    if key != voidKey or Bcnt == 2:
        core.show()
    key = core.getKey()
warp = 3
Wx = x
Wy = y
compil()
execfile(currentPath + "Zelda_M.py")
