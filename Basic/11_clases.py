### Classes ###

class Person:
    def __init__(self, name, surname, alias = "Sin alias") -> None:
        self.full_name = f"{name} {surname} ({alias})"
        self.__name = name
        self.__surname = surname

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando.")

my_person = Person("Brais", "Moure")
print(my_person.full_name)
print(f"Estoy aqui....... {my_person.get_name()}")
my_person.walk()

my_other_person = Person("Juanjo", "González", "MoureDev")
print(my_other_person.full_name)

my_other_person.walk()

my_other_person.full_name = "Juan José (turudev)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)