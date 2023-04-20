### STRING ###

name, surname, age = "Brais", "Moure", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetando de caracteres
language = "Python"
a,b,c,d,e,f = language
print(a)
print(e)

# Funciones
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print(language.lower())