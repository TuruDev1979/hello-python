### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35}
print(type(my_other_dict))
print(my_other_dict)

my_dict = {
    "Nombre":"Brais",
    "Apellido":"Moure",
    "Edad":35,
    "Lenguajes":{"Python", "Swift", "Kotlin",},
    1:1.77
}
print(my_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Nombre"])

# realizar busquedas dentro de un diccionario
print("Moure" in my_dict)
print("Mouri" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys())