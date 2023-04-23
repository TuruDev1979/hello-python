### Loops ###

# While
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    print(my_condition)
    if my_condition == 15:
        print("Mi condición es 15")  
        break
    print("Mi condición es menor que 20")

print("La ejecución continúa")

# For
my_list = [35, 24, 62, 52, 30, 30, 17]
my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_set = {"Brais", "Moure", 35}
my_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35}

print("listas")
for element in my_list:
    print(element)

print("tuplas")
for element in my_tuple:
    print(element)

print("set")
for element in my_set:
    print(element)

print("diccionarios")
for element in my_dict.values():
    print(element)
    if element == "Moure":
        break
else:     # Cunado se ejecuta el Break no se ejecuta el else
    print("El bucle for para mi diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict.values():
    print(element)
    if element == "Moure":
        continue
else:     # Cunado se ejecuta el continue si se ejecuta el else
    print("El bucle for para mi diccionario ha finalizado")

print("La ejecución continúa")