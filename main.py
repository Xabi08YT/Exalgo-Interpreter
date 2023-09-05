def execfile(path):
    with open(path, mode="rb") as f:
        content = f.readlines()
        f.close()
    
    code = []

    for line in content:
        code.append(line.decode("utf-8")) 
    


if __name__ == "__main__":
    execfile("test.ExAlgo")
    pass