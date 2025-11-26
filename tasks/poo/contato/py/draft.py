class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number

    def getId(self):
        return self.id

    def getNumber(self):
        return self.number

    def __str__(self):
        return f"{self.id}: {self.number}"

class Contact:
    def __init__(self, name: str):
        self.name = name
        self.favorited: bool = False
        self.fones: list(Fone) = []

    def getFones(self):
        return self.fones

    def getName(self):
        return self.name

    def addFone(self, fone: Fone);
        self.fones.append(fone)
       
    def removeFone(self, valor: int):
        if 0 <= valor < len(self.fones):
            self.fones.pop(valor)
        else:
            print("indice inválido")
    
    def ifFavorited(self):
        return self.favorited


