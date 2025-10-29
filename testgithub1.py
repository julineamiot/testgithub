class Calculatrice():
    def __init__(self):
        pass

    def addition(self, a, b):
        return a + b

    def soustraction(self, a, b):
        return a - b

    def valeur_absolue(self, a):
        if a >= 0:
            return a
        else:
            return -a

    def multiplication(self, a, b):
        resultat = 0
        for n in range(b):
            resultat = self.addition(resultat, a)
        return resultat

    def puissance(self, a, b):
        if b == 0:
            return 1  # par convention tout nb à la puissance 0 vaut 1
        if b < 0:
            raise ValueError("L'exposant doit être positif")
        resultat = 1
        for i in range(b):
            resultat = self.multiplication(resultat,a)  # c'est le même principe que la multiplication (avec l'addition) mais cette fois-ci on le fait pour la puissance (avec la multiplication)
        return resultat

    def est_premier(self, n):
        if n <= 1:
            return False
        i = 2
        while i < n:
            quotient, reste = self.division(n, i)
            if reste == 0:
                return False
            i = self.addition(i, 1)
        return True



elif choix == "2":
    a = int(input("Entrez le premier nombre : "))
    b = int(input("Entrez le second nombre : "))
    print("Résultat :", calc.soustraction(a, b))
    print()

elif choix == "3":
           a = int(input("Entrez le nombre : "))
           print("Résultat :", calc.valeur_absolue(a))
           print()

elif choix == "4":
    a = int(input("Entrez le premier nombre : "))
    b = int(input("Entrez le second nombre : "))
    print("Résultat :", calc.multiplication(a, b))
    print()

elif choix == "5":
    a = int(input("Entrez le premier nombre : "))
    b = int(input("Entrez le second nombre : "))
    q, r = calc.division(a, b)
    print(f"Quotient : {q}, reste : {r}")
    print()

elif choix == "6":
    n = int(input("Entrez n pour Fibonacci : "))
    print(f"F({n}) =", calc.fibonacci(n))
    print()

elif choix == "7":
    a = int(input("Entrez la base a : "))
    b = int(input("Entrez l'exposant b : "))
    print(f"{a}^{b} =", calc.puissance(a, b))
    print()

elif choix == "8":
    n = int(input("Entrez le nombre à tester : "))
    if calc.est_premier(n):
        print(n, "est premier")
    else:
        print(n, "n'est pas premier")
    print()

else:
    print("Choix invalide, réessayez")
