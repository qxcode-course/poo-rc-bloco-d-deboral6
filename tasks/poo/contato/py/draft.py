class Fone:
    validos = "0123456789()."

    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number

    def getId(self):
        return self.id

    def getNumber(self):
        return self.number

    def validar(self, number):
        for n in number:
            if n not in self.validos: 
                return False
        return True

    def __str__(self):
        return f"{self.id}: {self.number}"


class Contact:
    def __init__(self, name: str):
        self.name = name
        self.favorited: bool = False
        self.fones: list[Fone] = []

    def getFones(self):
        return self.fones

    def getName(self):
        return self.name

    def addFone(self, fone: Fone):
        if fone.validar(fone.number): 
            self.fones.append(fone)
        else:
            print("numero invalido")

    def removeFone(self, valor: int):
        if 0 <= valor < len(self.fones):
            self.fones.pop(valor)
        else:
            print("indice inválido")
    
    def ifFavorited(self):
        self.favorited = True
    
    def desfavoritar(self):
        self.favorited = False

    def __str__(self):
        if self.favorited:
            prefixo = "@"
        else:
            prefixo = "-"
        fones_str = ""
        for i in range(len(self.fones)):
            fone = self.fones[i]
            fones_str += f"{i}:{fone.id}:{fone.number}"
            if i < len(self.fones) - 1:
                fones_str += ", "
        return f"{prefixo} {self.name} [{fones_str}]"

def main():
    contact = None

    while True:
        try:
            line = input()
        except EOFError:
            break

        if not line:
            continue

        args = line.split()

        # Comando init, add, rm, tfav, end → ecoa $ antes
        if args[0] in ["init", "add", "rm", "tfav", "end"]:
            print(f"${line}")

        if args[0] == "init":
            contact = Contact(args[1])
            print(contact)

        elif args[0] == "show":
            print(contact)  # NÃO imprime $show

        elif args[0] == "add":
            contact.addFone(Fone(args[1], args[2]))
            print(contact)

        elif args[0] == "rm":
            contact.removeFone(int(args[1]))
            print(contact)

        elif args[0] == "tfav":
            if contact.favorited:
                contact.desfavoritar()
            else:
                contact.ifFavorited()
            print(contact)

        elif args[0] == "end":
            print(f"${line}")
            break
