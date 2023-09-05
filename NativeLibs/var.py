class charactère:
    def __init__(self):
        self.val = ""
        return
        

    def assign(self,val:str):
        if len(val)>1:
            raise Exception("Cannot assign more than one character in a charactère var type.")
        self.val = val


class entier:
    def __init__(self):
        self.val = None
        return
    

    def assign(self,val:int):
        self.val = val


def var(line):
    pass
