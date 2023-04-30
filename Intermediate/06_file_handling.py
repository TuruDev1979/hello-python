### Fiel Handling ###
import os
import json

# .txt file
txt_file = open(file="Intermediate/my_file.txt", mode="r+") # Leer, escribir y sobrescribir si ya existe

txt_file.write("Mi nombre es Juanjo\nMi apellido es González\nTengo 43 años\nY mi lenguaje preferido es Python")

#print(txt_file.read()) # Leer el fichero completo
print(txt_file.read(10)) # Leer un número de caracteres
print(txt_file.readline()) 
print(txt_file.readline())
print(txt_file.readlines()) # Leer linea a linea
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien me gusta Swift")
print(txt_file.readline())

txt_file.close()

with open(file="Intermediate/my_file.txt", mode="a") as my_other_file:
    my_other_file.write("\nY Kotlin")

#os.remove("Intermediate/my_file1.txt")


# .json file
json_file = open(file="Intermediate/my_file.json", mode="w+")

json_test = {
    "Nombre":"Juanjo",
    "Apellido":"Gonzalez",
    "Edad":"43",
    "Lenguaje":["Python","Kotlin","Swift","Cobol","PHP"],
    "WebSite":"https://juanjogonzalez.es"
    }

json.dump(obj=json_test, fp=json_file, indent=2)
json_file.close()

with open(file="Intermediate/my_file.json") as my_other_json:
    for line in my_other_json.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file_dos.json"))
print(json_dict)
print(type(json_dict))

print(json_dict["Nombre"])

# .csv . file
import csv
csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name","surname","age","language","webside"])
csv_writer.writerow(["Juanjo","Gonzalez","43","Python","https://juanjogonzalez.es"])

csv_file.close()

with open(file="Intermediate/my_file.csv") as my_other_csv:
    for line in my_other_csv.readlines():
        print(line)

# .xlsx file
#import xlrd # Debe instalarse el módulo
# 
# # .xml file
from xml.dom import minidom

doc = minidom.parse("Intermediate/xml_example.xml")
empleados = doc.getElementsByTagName("empleado")
for empleado in empleados:
    sid = empleado.getAttribute("id")
    nombre = empleado.getElementsByTagName("nombre")[0]
    username = empleado.getElementsByTagName("username")[0]
    password = empleado.getElementsByTagName("password")[0]
    print(f"id: {sid}")
    print(f"Nombre: {nombre.firstChild.data}")
    print(f"username: {username.firstChild.data}")
    print(f"password: {password.firstChild.data}")


