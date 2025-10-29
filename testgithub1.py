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

# test ?