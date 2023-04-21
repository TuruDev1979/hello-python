### Conditionals ###

my_condition = False

if my_condition:
    print("Se ejecuta la condición del if")

my_condition = 5 * 2 - 1

if my_condition == 10 or my_condition < 10:
    print("Se ejecuta la condición del segundo if")
elif my_condition > 10:   
    print("Es mayor que 10")
else:   
    print("No se cumple")

print("La ejecución continúa")