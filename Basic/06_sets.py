### Sets ###
# Son listas no ordenadas
# Son listas que no admiten repetidos

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))

print(len(my_other_set))  # Imprimimos el numero de elementos.

my_other_set.add("MoureDev")
print(my_other_set)

# realizar busquedas dentro de un set
print("Moure" in my_other_set)
print("Mouri" in my_other_set)

my_other_set.remove("Moure")
print(my_other_set)

my_other_set.clear() # Elimina el contenido del set
print(my_other_set)

del my_other_set # Elimina el la variable.
print(my_other_set)