#Задача 1. Напишите программу с классом Math. Создайте два атрибута — a и b.
# Напишите методы addition — сложение, multiplication — умножение, division — деление, subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

class Math:
    def __init__(self, a = 31, b = 23 ):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a+self.b)

    def subtraction(self):
        print(self.a - self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)







