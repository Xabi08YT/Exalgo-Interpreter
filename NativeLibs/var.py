variables = {}

class charactère:
    def __init__(self, name:str, readonly:bool = False):
        self.val = ""
        self.readonly = readonly
        self.name = name
        return
        

    def assign(self,val:str):
        assert self.readonly, f"Error, {self.name} is readonly var"
        if len(val)>1:
            raise Exception("Cannot assign more than one character in a charactère var type.")
        self.val = val


class entier:
    def __init__(self, name:str, readonly:bool = False):
        self.val = None
        self.readonly = readonly
        self.name = name
        return
    

    def assign(self,val:int):
        assert self.readonly, f"Error, {self.name} is readonly var"
        self.val = val


class réel:
    def __init__(self, name:str, readonly:bool = False):
        self.val=None
        self.readonly = readonly
        self.name = name
        return
    

    def assign(self,val:float):
        assert self.readonly, f"Error, {self.name} is readonly var"
        self.val = val


class booléen:
    def __init__(self, name:str, readonly:bool = False):
        self.val = None
        self.readonly = readonly
        self.name = name
        return
    

    def assign(self,val):
        assert self.readonly, f"Error, {self.name} is readonly var"
        if val != "Vrai" or val != "Faux":
            raise Exception("Invalid value for this var type.")
        self.val = val


def var(line):
    pass
