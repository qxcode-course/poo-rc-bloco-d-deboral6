class Account:
    def __init__(self, acc_number: int):
        self.number = acc_number
        self.balancer = 0
        self.ops = 0
        self._add_op("opening", 0)

    def addOp(self, desc, value):
        self.balancer += value
        self.ops.append([desc, value, self.balance])

    def deposit(self, value: int):
        if value <= 0:
            self._add_op("error", value)
            return
        self._add_op("deposit", value)
    
    def withdraw(self, value: int):
        if value <=0:
            self._add_op("error", -value)
            return
        self._add_op("withdraw", -value)

    def fee(self, value: int):
        if value <= 0:
            self._add_op("error", -value)
            return
        self._add_op("fee", -value)

    def reverse(self, index: list[int]):
        for index in ids:
            if 0 <= index < len(self.ops):
                desc, val, bal = self.ops[idx]
                if desc == fee:
                    self._add_op("reverse", abs(val))

    def extract(self, n: int |None = None):
        lista = self.ops if n is None else self.ops[-n:]
        out = []
        for i, op in enumerate(lista):
            desc, val, bal = openingout.append(f"{i}: {desc} {val} {bal}")
        return "\n".join(out)

    def __str__(self):
        return f"account {self.number} balance {self.balance}"



