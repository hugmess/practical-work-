#Задача 2. Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
# По умолчанию name = Ivan, age = 18, groupNumber = 10A. Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber.
# Метод getName нужен для получения данных об имени конкретного студента, метод getAge нужен для получения данных о возрасте конкретного студента,
# vетод setGroupNumberнужен для получения данных о номере группы конкретного студента.
# Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber позволяет изменить номер группы установленный по умолчанию.
# В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.

class Student():
    def __init__(self, name = 'Ivan', age = 18, groupNumber = '10A' ):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def info(self):
        return \
            f" === {self.name} ===\n" \
            f" Возраст: {self.age}\n " \
            f"Группа: {self.groupNumber}\n "

    def getName(self):
        return \
             f'{self.name}\n'

    def getAge(self):
        return \
             f'{self.age}\n'

    def getGroupNumber(self):
        return \
             f'{self.groupNumber}\n'

    def setGroupNumber(self,groupNumber):
        self.groupNumber = input('создайте группу')



Ivan = Student()
Max = Student(name = 'Max', age = 15, groupNumber = '9V')
Yoru = Student(name = 'Yoru', age = 13, groupNumber = '7А')
Anne = Student(name = 'Anne', age = 14, groupNumber = '7D')
Jett = Student(name = 'Jett',age = 16, groupNumber = '10B')


