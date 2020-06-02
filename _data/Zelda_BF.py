# -*- coding: cp1252 -*-
import os
currentPath = "/storage/emulated/0/qpython/projects/ZeldaRTP[1.3.2]/_data/"
cP = "/storage/emulated/0/qpython/projects/ZeldaRTP[1.3.2]/"

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
core.d2D(4,2,"Tiends donc ! Je")
core.d2D(2,3,"t'attendais vermine")
core.show()
key = voidKey
while key != 13:
    key = core.getKey()
core.clear()
x,y,bombCnt,bCooX,hookX,hookY,hookOk,Blife,Bcnt,Bpos,Bstate,BstateCnt,sCooX = 21,6,0,0,0,0,0,4,0,1,0,0,0
Bright = True
if Wx != 0:
	x = Wx
	y = Wy
right = True
core.d2D(1,1,"Vie:")
core.d2D(1,7,"`````````````````````")
key = 1
while key != 105:
    if key != voidKey:
        for b in range(lifeMax):
            core.d2D(b+5,1,".")
        for b in range(life):
            core.d2D(b+5,1,"@")
        core.d2D(1,5,"                     ")
        core.d2D(1,6,"                     ")
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
            if hookX == Bpos and hookY > 5 and Bstate == 0:
                Bstate = 1
    else:
        if key == 113 and x > 1:
            right = False
            x -= 1
        if key == 100 and x < 21:
            right = True
            x += 1
        if key == sword and x != 1 and x != 21:
            sCooX = x-1+2*int(right)
            if sCooX == Bpos and Bstate == 2:
                BstateCnt = 0
                Bstate = 0
                Bcnt = 0
                Blife -= 1
            core.d2D(sCooX,6,"-")
        if key == bomb and bombCnt == 0 and x != 1 and x != 21:
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
            if x > bCooX-2 and x < bCooX+2:
                life -= 1
            if Bpos > bCooX-2 and Bpos < bCooX+2 and Bstate == 1:
                BstateCnt = 0
                Bstate = 2
    if key == hookshot and hookOk == 0:
        hookOk = 1
        hookX = x
        hookY = y
    if Bstate == 0:
        Bcnt += 1
    if Bcnt == 5:
        if x < Bpos:
            Bright = False
            Bpos -= 1
        if x > Bpos:
            Bright = True
            Bpos += 1
        if x == Bpos:
            life -= 1
        Bcnt = 0
    if Bstate != 0:
        BstateCnt += 1
    if BstateCnt == 12:
        Bstate = 0
        BstateCnt = 0
    if Blife == 0:
        save = 8
        Wx = 0
        Wy = 0
        story = 8
        compil()
        x = 1
        y = 1
        while y < 8:
            core.d2D(x,y,"*")
            core.show()
            x += 1
            if x > 21:
                x = 1
                y += 1
            for a in range(200000):
                a = 0
        core.d2D(7,4,"THE**END")
        core.show()
        key = voidKey
        while key != 13:
            key = core.getKey()
        execfile(cP + "ZeldaRTP.py")
    if life == 0:
        Wx = 0
        Wy = 0
        save = 8
        compil()
        execfile(currentPath + "Zelda_0.py")
    if key == 111:
        core.clear()
        core.d2D(4,3,"Can't save here!")
        core.show()
        key = voidKey
        while key != 13:
            key = core.getKey()
        core.d2D(4,3,"                ")
        core.d2D(1,1,"Vie:")
        core.d2D(1,7,"`````````````````````")
    if Bstate == 2:
        core.d2D(Bpos,6,"G")
    else:
        core.d2D(Bpos,5,"G")
        if Bstate == 1:
            if Bright == False:
                core.d2D(Bpos,6,")")
            else:
                core.d2D(Bpos,6,"(")
        else:
            if Bright == False:
                core.d2D(Bpos,6,"]")
            else:
                core.d2D(Bpos,6,"[")
    core.d2D(x,y-1,"0")
    if right == False:
        core.d2D(x,y,"}")
    else:
        core.d2D(x,y,"{")
    if key != voidKey:
        core.show()
    key = core.getKey()
warp = 11
Wx = x
Wy = y
compil()
execfile(currentPath + "Zelda_M.py")
