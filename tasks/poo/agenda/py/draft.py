class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number
    
    def isValid(self) -> bool:
        valido = "0123456789()-."
        for i in self.number:
            if i not in valido:
                return False
        return True

    def getId(self) -> str:
        return self.id
    def getNumber(self) -> str:
        return self.number
    
    def __str__(self) -> str:
        return f"{self.id}:{self.number}"

class Contact:
    def __init__(self, name: str, fones: list[Fone]):
        self.name = name
        self.favorited = False
        self.fones: list[Fone] = fones[:] 

    def addFone(self, id: str, number: str) -> None:
        fone = Fone(id, number)
        if fone.isValid():
            self.fones.append(fone)
        else:
            print("fail: invalid number")

    def rmFone(self, index: int) -> None:
        if 0 <= index < len(self.fones):
            self.fones.pop(index)
        else:
            print("fail: indice invalido")
    
    def toogleFavorited(self) -> None:
        self.favorited = not self.favorited
    
    def isFavorited(self) -> bool:
        return self.favorited
    
    def getFones(self) -> list:
        return self.fones
    def getName(self) -> str:
        return self.name
    def setName(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        fav = "@" if self.favorited else "-"
        fones_str = ", ".join(str(f) for f in self.fones)
        return f"{fav} {self.name} [{fones_str}]"

class Agenda:
    def __init__(self):
        self.contacts: list[Contact] = []
    
    def findPosByName(self, name: str) -> int:
        for i, contact in enumerate(self.contacts):
            if contact.getName() == name:
                return i
        return -1

    def addContact(self, name: str, fones: list[Fone]):
        pos = self.findPosByName(name)
        if pos == -1:
            nv = Contact(name, [])
            for f in fones:
                nv.addFone(f.id, f.number)
            self.contacts.append(nv)
        else:
            for f in fones:
                self.contacts[pos].addFone(f.id, f.number)
        self.contacts = sorted(self.contacts, key=lambda x: x.name)

    def getContact(self, name: str) -> Contact | None:
        pos = self.findPosByName(name)
        if pos == -1:
            return None
        return self.contacts[pos]

    def rmContact(self, name: str):
        pos = self.findPosByName(name)
        if pos == -1:
            print("fail: contato nao existe")
        else:
            self.contacts.pop(pos)

    def getFavorited(self) -> list[Contact]:
        return [f for f in self.contacts if f.isFavorited()]
    
    def search(self, pattern: str) -> list[Contact]:
        resultado = []
        for c in self.contacts:
            if pattern in c.getName():
                resultado.append(c)
                continue
            for f in c.getFones():
                if pattern in f.getId() or pattern in f.getNumber():
                    resultado.append(c)
                    break
        return resultado
    
    def favs(self) -> str:
        return "\n".join(str(c) for c in self.contacts if c.isFavorited())
    
    def getContacts(self) -> list[Contact]:
        return self.contacts[:]

    def __str__(self) -> str:
        return "\n".join(str(c) for c in self.contacts)

def main():
    agenda = Agenda()
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            agenda = Agenda()
        elif args[0] == "show":
            print(agenda)
        elif args[0] == "add":
            name = args[1].strip()
            fones = []
            for raw in args[2:]:
                if ":" in raw:
                    id, number = raw.split(":")
                    fones.append(Fone(id, number))
            agenda.addContact(name, fones)
        elif args[0] == "rm":
            agenda.rmContact(args[1])
        elif args[0] == "rmFone":
            name = args[1]
            index = int(args[2])
            contato = agenda.getContact(name)
            if contato:
                contato.rmFone(index)
            else:
                print("fail: contato nao existe")
        elif args[0] in ("fav", "tfav"):
            contato = agenda.getContact(args[1])
            if contato:
                contato.toogleFavorited()
            else:
                print("fail: contato nao existe")
        elif args[0] == "search":
            pattern = args[1]
            res = agenda.search(pattern)
            for c in res:
                print(c)
        elif args[0] == "showFavs":
            for c in agenda.getFavorited():
                print(c)
        elif args[0] == "favs":
            print(agenda.favs())

main()