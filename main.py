import NativeLibs


instructionSet = {"var ": NativeLibs.var.var, "Si": None}
_currentblocks = []
_currentindent = 0
requireblock = ["Fonction","Si","Sinon","Faire","Pour","Tant"]


def execLine(line:str):
    global _currentindent
    splitline = line.split(" ")
    if splitline[0] in instructionSet and splitline[0] not in requireblock:
        instructionSet[splitline[0]](line.replace(str(splitline[0]+" "),""))
    elif splitline[0] in requireblock:
        _currentindent += 1
        _currentblocks.append(_currentindent)
    



def execfile(path):
    with open(path, mode="rb") as f:
        content = f.readlines()
        f.close()
    
    code = []

    for line in content:
        code.append(line.decode("utf-8"))
        execLine(code)


if __name__ == "__main__":
    execfile("test.ExAlgo")
    pass