### Exception Handling ###

primer_valor = 5
segundo_valor = "7"

try: # Obligatorio
    # Se ejecuta siempre
    print(primer_valor + segundo_valor)
except:  #Obligatorio
    # Se ejecuta si se produce cuna excepción
    print("Error!!!")
else: # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta simpre
    print("La ejecución continúa")


# Excepciones por tipo
try: # Obligatorio
    # Se ejecuta siempre
    print(primer_valor + segundo_valor)
except TypeError:
    # Se ejecuta si se produce cuna excepción
    print("Error!!! TypeError")
except ValueError:
    # Se ejecuta si se produce cuna excepción
    print("Error!!! ValueError")


# Captura de la información de la excepción
try: 
    print(primer_valor + segundo_valor)
except Exception as e:
    print(f"Error!!! TypeError {e}")
