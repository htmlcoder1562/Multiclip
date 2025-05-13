import pyperclip

def save(slot):
    data=pyperclip.paste()
    with open("papersave.txt", "r") as file:
        filedata=file.read()
        filedata_newline=filedata.split("\n")
    filedata_newline[int(slot)]=data
    with open("papersave.txt", "w") as file:
        filedata=""
        y=0
        for x in filedata_newline:
            filedata=filedata+filedata_newline[y]
            if x!=filedata_newline[9]:
                filedata+="\n"
            y+=1
        filedata.rstrip("\n")
        file.write(filedata)