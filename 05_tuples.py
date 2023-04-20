#### Tuples ####
# Son lista estaticas de elementos

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
print(my_tuple)
print(type(my_tuple))

print(my_tuple.count("Brais"))
print(my_tuple.index("Moure"))

#my_tuple[1] = 1.80    # ERROR. Una tupla no es modificable una vez definida inicialmente.
#print(my_tuple)

# para poder modificar el contenido de una tupla hay primero que pasarla a lista, se modifica y luego se vuelve a pasar a tupla.
my_tuple = list(my_tuple)
print(type(my_tuple))
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))