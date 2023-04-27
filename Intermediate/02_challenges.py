### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

fizzbuzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""
def is_anagram(first_word, second_word):
    first_word = first_word.lower()
    second_word = second_word.lower()
    if first_word == second_word:
        return False
    else:
        first_word = sorted(first_word)
        second_word = sorted(second_word)
        if first_word == second_word:
            return True
        else:
            return False

result = is_anagram("Perro", "Gato")
print(result)

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci():
    prev = 0
    next = 1
    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

fibonacci()

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
def numeros_primos():
    for number in range(1, 101):
        if number >= 2:
            is_divisible = False
            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(number)

def is_prime(number):
    if number < 2:
        return False
    
    for index in range(2, number):
        if number % index == 0:
            return False
            break
        
    return True

result = is_prime(43)
print(f"¿Es primo? {result}")
numeros_primos()



def reverse(text):
    text_len = len(text)
    reverse_text = ""
    for index in range(0, len(text)):
        reverse_text += text[text_len - index - 1]
    return reverse_text

print(reverse("En un lugar de la Mancha, de cuyo nombre no quiero acordarme."))
