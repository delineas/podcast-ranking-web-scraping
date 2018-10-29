# Importacion de librerias completas
import pprint  # pprint es para formateo bonito de los print en pantalla

""" 
    __ Funciones y alcance de la variable (scope) __
    mermelade solo tiene el valor local dentro de la funcion
"""
mermelade = 'peach'

# Así se define una función
# ¡Ojo a la identación!

def toastWith(mermelade):
    """Comentario multilinea para explicar 
    que hace esta función."""
    mermelade = 'strawberry'
    pprint.pprint(mermelade)

pprint.pprint(mermelade)  # podria hacerse sin problemas con print(mermelade)
toastWith(mermelade)

mermelade = 'apple'
toastWith(mermelade)

"""
    __ Un string es una lista inmutable (tupla) __
"""

keystring = 'El veloz murciélago hindú comía feliz cardillo y kiwi'
print(keystring)
pprint.pprint(keystring[5])

# Mostará un error de asignacion, ¡no es modificable!
# keystring[15] = 'k'

"""
    __ Capturar el error __
"""

# esto es una lista
[a,b] = (5,0) 
print(type([a,b]))

# esto es una tupla
(x,y) = (5,0) 
print(type((x,y)))

try:
  z = x/y
except ZeroDivisionError: # como no puede dividir por cero, este es el error que podemos capturar
  print("You can't divide by zero") 

# Capturamos aquí el error de asignación de valor a un elemento de un string (inmutable)
keystring = 'El veloz murciélago hindú comía feliz cardillo y kiwi'
try:
  keystring[15] = 'k'
except TypeError: # como no puede dividir por cero, este es el error que podemos capturar
  print("No puedes hacer eso calamar! 😱") 

"""
    __ Recorrer una lista o tupla __
"""
prettystring = 'El veloz murciélago hindú comía feliz cardillo y kiwi'
print(len(prettystring))

# Entre el caracter 15 y 20
print(prettystring[15:20])
# A partir del caracter 10
print(prettystring[10:])
# Solo los 10 primeros caracters
print(prettystring[:10])
# Hasta el caracter -10
print(prettystring[:len(prettystring)-10])
print(prettystring[:-10])

# Así he llegado a este resultado
# for i in prettystring da error, ya que no le decimos el número de elementos del rango
# for i in len(prettystring) da error, ya que es un número (longitud de la cadena) pero no un rango
# for i in range(0,len(prettystring)) funciona y recorrerá toda la cadena
# el resultado final es recorrer solamente los 10 primeros elementos de la cadena
for i in range(0,len(prettystring[:10])):
    print(prettystring[i].upper())
