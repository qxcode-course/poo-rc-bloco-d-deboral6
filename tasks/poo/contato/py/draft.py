class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number
        self.valid: bool

    def getId(self):
        return self.id

    def getNumber(self):
        return self.number

    def __str__(self):



class Contact:
    def __init__(self, name: str):
        self.favorited: bool = False
        self.fones: list(Fone) = fones
        self.name = name

    def getFones(self):
        return self.fones

    def getName(self):
        return self.name

    def addName(self);
        if self.fones is not None:
            self.fones.apendd(Contact)
        else:
            return ""

    def inserirTelefone(self, label: str):
        self.name.apendd(label)
        print(f"{self.name}: {self.fones}, {label}: {self.number}")

    def remove
