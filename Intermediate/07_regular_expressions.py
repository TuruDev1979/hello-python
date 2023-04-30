### Regular Expressions ###

import re

my_string = "Esta es la lección de número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección de número 7: Expresiones Regulares"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Expresiones Regulares", my_string)
#if match != None: # Otra forma de comprobar el None
#if match is not None: # Otra forma de comprobar el None
if not(match == None):
    print(match)
    start, end = match.span()
    print(my_string[start:end])

print(re.match("Esta es la lección", my_other_string))

# search
search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall
findall = re.findall("lección", my_string, re.I)
print(findall)

# split
print(re.split(":", my_string))

# sub
print(re.sub("lección|Lección", "LECCIÓN", my_string))
print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

# Patterns
pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print("aqui")
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

# email validation regular expresion
email = "jjgonzalez.agudo@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$"
print(re.match(pattern, email))

email_validado = re.match(pattern, email)
if not(email_validado == None):
    print("Email Correcto") 
else:
    print("Email Incorrecto") 
