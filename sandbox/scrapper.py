from bs4 import BeautifulSoup
from pprint import pprint
import os

# Nos da el valor del directorio de trabajo desde el que se ejecuta el comando
# > python sandbox/scrapper.py -> sandbox/
# > cd sandbox
# > python scrapper.p -> ./
script_dir = os.path.dirname(__file__)

file = open(os.path.join(script_dir, "content/paella.html"))

# Muestra todo el contenido leido
# print file.read()
soup = BeautifulSoup(file.read(), "lxml")

# Imprime directamente el title de la pagina
# print(soup.title)


# Leemos las metas que tienen name y mostramos en pantalla solo el atributo content
metas = soup.select('meta[name]')

# Nos devuelve una list
# pprint(type(metas))

for meta in metas:
    pprint(meta.attrs['content'])

# Captura por el ID y otros selectores al estilo jQuery
# print(soup.select('#Historia'))

# Leemos los h3 y mostramos su contenido. Strip es para eliminar espacios en blanco
for titles in soup.find_all("h3"):
    pprint(titles.text.strip())

# Nos devuelve una lista, pero es una class que exitende list @see http://docs.ros.org/diamondback/api/rosdeb/html/rosdeb.BeautifulSoup.ResultSet-class.html
# pprint(type(soup.find_all("h3")))

titles = soup.select("h3")
for i in range(0, len(titles)):
    pprint(titles[i].getText())
    pprint(titles[i].get('id'))

