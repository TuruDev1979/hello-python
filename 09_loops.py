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