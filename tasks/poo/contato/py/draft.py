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

def main():
    contact: Contact | None = None

    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "init":
            contact = Contact(args[1])

        elif args[0] == "show":
            print(contact)

        elif args[0] == "add":
            contact.addFone(args[1], args[2])

        elif args[0] == "rm":
            contact.removeFone(int(args[1]))

        elif args[0] == "tfav":
           contact.toggleFav()

main()
