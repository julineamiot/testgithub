class Calculatrice():
    def __init__(self):
        pass

    def addition(self, a, b):
        return a + b + 2b

    def soustraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return "division par zéro impossible"
        return a / b

    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
