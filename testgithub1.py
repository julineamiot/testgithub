#Projet calculatrice
print("AMIOT Juline et DESMOTTES Henri")


print()
print()
print("Vous allez effectuer des calculs à l'aide d'une calculatrice.")
print("Commençons par rappeler quelques règles de calculs.")
print("Vous ne pouvez pas diviser par 0.")
print("Notre calculatrice ne peut pas avoir comme exposant un nombre négatif.")
print("La suite de Fibonacci se calcule que pour des entiers naturels.")
print("Un nombre premier est forcément un entier naturel.")
print("Enfin, la règle la plus importante à respecter pour utiliser notre calculatrice est qu'elle n'accepte que les entiers.")
print()


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

    def division(self, a, b):
        # on gère le cas de la division par 0
        if b == 0:
            raise ZeroDivisionError("division par 0 impossible")

        signe = 1
        if a < 0:
            a = self.valeur_absolue(a)
            signe *= -1

        if b < 0:
            b = self.valeur_absolue(b)
            signe *= -1

        quotient = 0  # quotient : le résultat final qu’on va calculer (10/3, quotient = 3)
        reste = a  # reste : ce qu'il reste à diviser au fur et à mesure (10/3, reste au début = 10)

        while self.valeur_absolue(reste) >= b:  # combien de fois on peut enlever b à a avant de tomber en dessous de b => tant que le reste est plus grand ou égal à b, on continue
            reste = self.soustraction(reste, b)
            quotient = self.addition(quotient, 1)  # à chaque étape réussie, le quotient augmente de 1

        quotient *= signe
        if signe < 0:
            reste = -reste

        return quotient, reste

    def puissance(self, a, b):
        if b == 0:
            return 1  # par convention tout nb à la puissance 0 vaut 1
        if b < 0:
            raise ValueError("L'exposant doit être positif")
        resultat = 1
        for i in range(b):
            resultat = self.multiplication(resultat,a)  # c'est le même principe que la multiplication (avec l'addition) mais cette fois-ci on le fait pour la puissance (avec la multiplication)
        return resultat

    def fibonacci(self, n):
        # chaque terme = somme des 2 précédents : 0, 1, 1, 2, 3, 5, 8, ...
        if n == 0 or n == 1:  # si n = 0 ou 1, alors on retourne 0 ou 1, c'est les seuls termes de la suite égaux à eux-mêmes
            return n
        if n < 0:
            raise ValueError("La suite de Fibonacci ne fonctionne que pour des entiers positifs")
        a = 0  # premier nombre de la suite
        b = 1  # deuxième nombre de la suite, on va utiliser ces deux nombres pour calculer les suivants
        for i in range(
                n - 1):  # a et b contiennent déjà les 2 premiers termes et on veut calculer le terme n, donc il suffit de faire n-1 tours pour atteindre n
            somme = self.addition(a, b)  # on calcule la somme des deux précédents nombres
            a = b  # a prend la valeur de b et b prend la valeur de la somme => on décale tout d'un cran
            b = somme
        return b  # on veut le terme final donc on retourne b


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

#Interface console
calc = Calculatrice()
#on crée une fonction menu() pour afficher le menu à l’écran, pour ne pas répéter le même code plusieurs fois
def menu():
    print("Choississez une opération à effectuer :")
    print("1 : Addition")
    print("2 : Soustraction")
    print("3 : valeur absolue")
    print("4 : Multiplication")
    print("5 : Division")
    print("6 : Fibonacci")
    print("7 : Puissance")
    print("8 : Vérifier nombre premier")
    print("0 : Quitter")

while True: #boucle infinie
    menu()
    choix = input("Entrez votre choix : ")

    try:
        if choix == "0":
            print("Au revoir")
            break

        elif choix == "1":
            a = int(input("Entrez le premier nombre : "))
            b = int(input("Entrez le second nombre : "))
            print("Résultat :", calc.addition(a, b))
            print()

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

    except ValueError as e:
        print("Erreur :", e)
    except ZeroDivisionError as e:
        print("Erreur :", e)
