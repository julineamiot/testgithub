#nous allons faire des calculs, additions, soustractions, multiplications, divisions,
#savoir c'est un nombre premier et calculer une suite de fibonacci
#vous allez devoir taper 1 pour une addition, 2 pour la soustraction, 3 pour la multiplication,
#4 pour la division, 5 pour savoir si c'est un nombre premier et 6 pour calculer la suite de fibonacci

choix = input("Vous pouvez donner votre choix de calcul : ")

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

    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    def premier(self, n):
        pass

calculatrice = Calculatrice()
print(calculatrice.multiplication(2,6))
print(calculatrice.division(2,6))