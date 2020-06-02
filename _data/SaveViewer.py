current = ""
while 1:
    saveFile = open("save.txt","r")
    content = saveFile.read()
    saveFile.close()
    if content != current:
        for a in range(25):
            print("")
        current = content
        print(content)
