class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number 

    def validar(self) -> bool:
        validos = "0123456789()-."
        for n in self.number:
            if n not in validos:
                return False
        return True

    def __str__(self) -> str:
        return f"{self.id}:{self.number}"

class Contact:
    def __init__(self, name: str):
        self.name = name
        self.favorited = False
        self.fones: list[Fone] = []

    def addFone(self, id: str, number: str) -> None:
        fone = Fone(id, number)
        if fone.validar():
            self.fones.append(fone)
        else:
            print("fail: invalid number")

    def removeFone(self, index: int) -> None:
        if 0 <= index < len(self.fones):
            self.fones.pop(index)
        else:
            print("fail: indice invalido")

    def isFavorited(self) -> bool:
        return self.favorited

    def toggleFav(self) -> None:
        self.favorited = not self.favorited

    def __str__(self):
        fav = "@" if self.favorited else "-"
        fones_str = ", ".join(str(f) for f in self.fones)
        return f"{fav} {self.name} [{fones_str}]"
    
class Agenda:
    def __init__(self):
        self.contacts: list[Contact] = []

    def findPosByName(self, name: str) -> int:
        for i, c in enumerate(self.contacts):
            if c.name == name:
                return i
        return -1

    def addContact(self, name: str, fones: list[tuple[str, str]]): 
        pos = self.findPosByName(name)

        if pos != -1:
            contato = self.contacts[pos]

        else:
            contato = Contact(name)
            self.contacts.append(contato)

        for id_, num in fones:
            contato.addFone(id_, num)
        self.contacts.sort(key=lambda c: c.name.lower()) 
 
    def getContact(self, name: str) -> Contact | None:
        pos = self.findPosByName(name)
        if pos == -1:
            return None
        return self.contacts[pos]

    def rmContact(self, name: str):
        pos = self.findPosByName(name)
        if pos != -1:
            self.contacts.pop(pos)    
        else: 
            print("fail: contato inexistente")

    def search(self, pattern: str) -> list[Contact]:
        return [c for c in self.contacts if pattern in str(c)]

    def getFavorited(self) -> list[Contact]:
        favs = []
        for contato in self.contacts:
            if contato.isFavorited():
                favs.append(contato)
        return favs

    def getContacts(self) -> list[Contact]:
        return self.contacts

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
            name = args[1]
            fones = []
            for par in args[2:]:
                id_, num = par.split(":")
                fones.append((id_, num))
            agenda.addContact(name, fones)

        elif args[0] == "rm":
            agenda.rmContact(args[1])

        elif args[0] == "search":
            result = agenda.search(args[1])
            for c in result:
                print(c)

        elif args[0] == "tfav":
            contato = agenda.getContact(args[1])
            if contato:
                contato.toggleFav()
            else:
                print("fail: contato inexistente")

main()