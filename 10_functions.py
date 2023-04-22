### Functions ###

def my_function():
    print("Esto es una función")

my_function()

# Función que opera pero no retorna nada
def sum_two_values(first_number, second_number):
    print("Primer numero:", first_number)
    print("Segundo numero:", second_number)
    suma = first_number + second_number
    print(suma)
    
sum_two_values(5, 7)

# Funcion que devuelve un resutaldo
def sum_two_values_with_return (first_value, second_value):
    print("Primer numero:", first_value)
    print("Segundo numero:", second_value)
    suma = first_value + second_value
    return suma

resultado = sum_two_values_with_return(10, 5)
print(resultado)

#
def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Moure", name="Brais")

#
def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure", "MoureDev")
print_name_with_default("Brais", "Moure")

#
def print_texts(*texts):
    for text in texts:
        print(text.upper())

print_texts("Hola", "Python", "MoureDev")
print_texts("Hola")