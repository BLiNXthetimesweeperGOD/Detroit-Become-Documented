#(Lots of reusable code is in my codingTools script)
from Libraries.codingTools import *

path = "decompressed/"
createPath(path) #Checks if the path exists or not and creates it if needed

files = dialogs.files()

def decompressSeg(file):
    with open(file, "rb") as f:
        #This is where the decompressed data will go
        fullData = b''

        #Parse the header and check if this is a valid segs file
        signature = f.read(4)
        if signature == b'segs':
            unknown = f.read(2)
            entries = lunpack.ushort(f.read(2))-1

            #If the entries are odd, there's 8 extra bytes of padding.
            if entries & 1 == 0:
                baseOffset = ((entries+2)*0x8)+0x10
                entries+=1
            else:
                baseOffset = ((entries+1)*0x8)+0x10
                entries+=1
            
            decompressedSize = lunpack.uint(f.read(4))
            compressedSize = lunpack.uint(f.read(4))
            
            for entry in range(entries):
                #Get size and offset of chunk
                size = lunpack.uint(f.read(4))
                offset = lunpack.uint(f.read(4))-1

                #Save position in file for later
                savedPosition = f.tell()

                #Go to the offset obtained earlier and read/decompress the data
                f.seek(offset+baseOffset)
                data = f.read(size)
                decompressed = fileTools.decompress(data)

                #Append decompressed data to fullData
                fullData+=decompressed

                #Go back to the saved position
                f.seek(savedPosition)
        return fullData

for file in files:
    #Decompress the seg
    try:
        data = decompressSeg(file)
        if len(data) > 0 and not os.path.exists(path+f"{fileTools.nameNoExt(file)}_Decompressed.bin"):
            #Save the decompressed contents
            with open(path+f"{fileTools.nameNoExt(file)}_Decompressed.bin", "w+b") as s:
                s.write(data)
    except:
        ""


