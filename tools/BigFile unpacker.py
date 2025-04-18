from Libraries.codingTools import *
import DBHTypes

def readIDX(idxFile):
    parsedTable = []
    with open(idxFile, "rb") as idx:
        header = idx.read(0x65)
        entries = bunpack.uint(idx.read(4))
        for index in range(entries):
            #Big Endian Multi-Unpack
            Type, AssetCount, ID, Offset, Size, AltSize, PackageID = bmultiunpack.uint(idx.read(28))
            if not os.path.exists(outputDirectory+f"{types.get(Type)}/"):
                os.makedirs(outputDirectory+f"{types.get(Type)}/")
            if PackageID == 0:
                dataFile = f"{packageName}.dat"
            else:
                dataFile = f"{packageName}.d{PackageID:02}"
            with open(dataFile, "rb") as container:
                container.seek(Offset)
                file = container.read(Size) #TO-DO: Figure out what AltSize actually is
                if file.startswith(b'QZIP'):
                    with open(outputDirectory+f"{types.get(Type)}/"+f"{PackageID:02}_{ID:08}.QZIP", "w+b") as outputFile:
                        outputFile.write(file)
                elif file.startswith(b'segs'):
                    with open(outputDirectory+f"{types.get(Type)}/"+f"{PackageID:02}_{ID:08}.segs", "w+b") as outputFile:
                        outputFile.write(file)
                elif file.startswith(b'COM_CONT'):
                    with open(outputDirectory+f"{types.get(Type)}/"+f"{PackageID:02}_{ID:08}.COM_CONT", "w+b") as outputFile:
                        outputFile.write(file)
                else:
                    with open(outputDirectory+f"{types.get(Type)}/"+f"{PackageID:02}_{ID:08}.bin", "w+b") as outputFile:
                        outputFile.write(file)
        print(f"The packages were successfully unpacked.")

#Define all major variables/reused stuff here
rootDirectory = dialogs.folder()
packageName = rootDirectory+"/BigFile_PC"
outputDirectory = os.getcwd()+"/Extracted/"

types = DBHTypes.getTypes()

if not os.path.exists(outputDirectory):
    os.makedirs(outputDirectory)

idxTable = readIDX(packageName+".idx")

