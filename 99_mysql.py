### Prueba conexión MySQL ###

import pymysql

mi_conexion = pymysql.connect(host='localhost', user='root', password='', database='pruebas_python')
cur = mi_conexion.cursor()
cur.execute("SELECT nombre, apellidos, edad FROM usuarios")

for nombre, apellidos, edad in cur.fetchall() :
    print(nombre, apellidos, "Años:", edad)

mi_conexion.close()