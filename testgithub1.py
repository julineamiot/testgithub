class Calculatrice():
    def __init__(self):
        pass

    def addition(self, a, b):
        return a + b + 3b

    def soustraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        resultat = 0
        for n in range(b):
            resultat = self.addition(resultat, a)
        return resultat

    def division(self, a, b):
        if b == 0:
            return "division par zéro impossible"
        else :
             

    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

calculatrice = Calculatrice()
print(calculatrice.multiplication(2,6))
print(calculatrice.division(2,6))

    def premier(self, n):
        pass
