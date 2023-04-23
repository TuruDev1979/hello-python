### Modules ###

# Para que importe todo el módulo
import Basic.my_module as my_module
# Para que importe solo una función del módulo
from Basic.my_module import sumValue

my_module.sumValue(5, 7)

import math

print(math.pi)
print(math.cos(5))
print(math.pow(2, 8))

# Para poder importar una funcion determinado de un módulo y queremos darle un nombre particular.
from math import pi as PI_NUMBER
print(PI_NUMBER)