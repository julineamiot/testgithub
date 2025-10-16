class Calculatrice():
    def __init__(self):
        pass

    def addition(self, a, b):
        return a + b + 2a

    def soustraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        for n in range(b-1):
            print (self.addition(a, a))

    def division(self, a, b):
        if b == 0:
            return "division par zéro impossible"
        return a / b

    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

calculatrice = Calculatrice()
calculatrice.multiplication(1,6)