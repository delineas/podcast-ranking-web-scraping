from bs4 import BeautifulSoup
from pprint import pprint

# Primero debemos definir la función para luego llamarla
def extract_toc(filepath):
    """
        Extrae el TOC de un fichero HTML almacenado en local proviniente de la wikipedia
        Devuelve una lista de items diccionario con title y anchor
    """
    try:
        file = open(filepath)
    except FileNotFoundError:
        print("El fichero no existe") 
    
    soup = BeautifulSoup(file.read(), "lxml")

    # TOC es una lista
    toc = []
    # Los titulos del contenido estan en este selector
    # TODO: Debería ser un selector configurable en la función
    titles = soup.select('#mw-content-text h3')
    for i in range(0, len(titles)):
        # Leemos los datos hijos de titles (el HTML contiene el ID del anchor)
        for child in titles[i].children:
            # Si el hijo tiene un id entonces añadimos a la lista toc 
            # TODO: El replace de [edit] debería ser un parámetro de funcion o una tupla de cadenas a eliminar
            toc.append({'title': titles[i].getText().replace('[editar]',''), 'anchor': child.get('id')}) if child.get('id') is not None else None

    return toc

pprint(extract_toc("sandbox/content/paella.html"))
