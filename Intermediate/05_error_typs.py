### Error Types ###

# SystaxError
#print "¡Hola comunidad!" # Descomentar para Error
print ("¡Hola comunidad!")

# NameError
language = "Spanish" # Comentar para error
print(language)

# IndexError
my_list = ["Cobol", "Python", "Swift", "Kotlin", "JavaScrip", "PHP"]
#print(my_list[8]) # Descomentar para Error
print(my_list[4])

# ModuleNotFoundError
#import maths # Descomentar para Error
import math

# AttributeError
# print(math.PI) # Descomentar para Error
print(math.pi)

# KeyError
my_dict = {
    "Nombre":"Brais",
    "Apellido":"Moure",
    "Edad":35,
    "Lenguajes":{"Python", "Swift", "Kotlin",},
    1:1.77
}

#print(my_dict["Edads"]) # Descomentar para Error
print(my_dict["Edad"])

# TypeError
#print(my_list["0"]) # Descomentar para Error
print(my_list[1])

# ImportError
#from math import PI # Descomentar para Error
from math import pi
print(pi)

# ValueError
my_int = int("10")
#my_int = int("10 Años") # Descomentar para Error
print(type(my_int))

#ZeroDivisionError
#print(5 / 0) # Descomentar para Error
print(5 / 2)