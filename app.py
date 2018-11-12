from bs4 import BeautifulSoup
from pprint import pprint

def read_file(filepath):
    """
        Extrae el contenido de ficheros locales y comprueba si existen
    """
    try:
        file = open(filepath)
    except FileNotFoundError:
        print("El fichero no existe") 
    
    soup = BeautifulSoup(file.read(), "lxml")

    return soup

