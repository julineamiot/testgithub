class Calculatrice():
    def __init__(self):
        pass

    def addition(self, a, b):
        return a + b

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
            resultat2 = 0
            for n in range(b):
                resultat2 = self.multiplication(resultat2, a)
        return resultat2

    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

calculatrice = Calculatrice()
print(calculatrice.multiplication(2,6))
print(calculatrice.division(2,6))

#faire une interface console au lieu de faire une interface graphique : ex : demander à l'utilisateur de taper un chiffre => si il tape 1, alors il fera une addition, etc...