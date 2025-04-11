#A custom library I wrote to cut down on the time needed to write scripts.
#We mainly just use it for file handling, the byte string scanner and lunpack (Little Endian Unpack).
from Libraries.codingTools import *
path = "decompressed/converted/"
createPath(path) #Checks if the path exists or not and creates it if needed
scanBytes = b'PHYMSD__'
files = dialogs.files()
for file in files:
    try:
        check, offset = fileTools.scanForBytes(file, scanBytes)
        if check == True:
            with open(path+f"{fileTools.nameNoExt(file)}.obj", "w+") as o:
                with open(file, "rb") as f:
                    f.seek(offset+0xC)
                    
                    count = lunpack.uint(f.read(4))
                    if count == 1297696848:
                        f.seek(8, 1)
                    for vert in range(count):
                        X = lunpack.float(f.read(4))
                        Y = lunpack.float(f.read(4))
                        Z = lunpack.float(f.read(4))
                        P = lunpack.float(f.read(4))
                        objLine = f'v {X} {Y} {Z}\n'
                        o.write(objLine)
                    count = lunpack.uint(f.read(4))//3
                    for face in range(count):
                        i1 = lunpack.uint(f.read(4))+1
                        i2 = lunpack.uint(f.read(4))+1
                        i3 = lunpack.uint(f.read(4))+1
                        objLine = f'f {i1} {i2} {i3}\n'
                        o.write(objLine)
    except:
        ""
