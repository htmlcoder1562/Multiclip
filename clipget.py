import pyperclip

def save(slot):
    if slot>9 or slot<0:
        return "Invalid slot number"
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
def load(slot):
    if slot>9 or slot<0:
        return "Invalid slot number"
    with open("papersave.txt", "r") as file:
        data=file.read()
    data=data.split("\n")
    return data[slot]