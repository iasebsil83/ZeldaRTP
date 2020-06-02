# -*- coding: cp1252 -*-
import os
import sys
currentPath = "/storage/emulated/0/qpython/projects/ZeldaRTP[1.3.2]/"

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
core.d2D(1,1,"~~~~~~~~~~~~~~~~~~~~~")
core.d2D(1,2,"=====Game===Over=====")
core.d2D(1,3,"~~~~~~~~~~~~~~~~~~~~~")
core.d2D(1,4,"}Try again   [enter]{")
core.d2D(1,5,"~~~~~~~~~~~~~~~~~~~~~")
core.d2D(1,6,"}Quit          [esc]{")
core.d2D(1,7,"~~~~~~~~~~~~~~~~~~~~~")
core.show()
key = 1
while key != 27:
    if key == 13:
        life = lifeMax
        Wx = 0
        Wy = 0
        compil()
        execfile(currentPath + "ZeldaRTP.py")
    key = core.getKey()
sys.exit()
