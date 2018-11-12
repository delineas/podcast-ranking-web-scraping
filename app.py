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

def get_podcasts(resource, podcasts):
    """
        Extrae el listado de podcasts 
        Devuelve una lista con el diccionario de elementos encontrados
    """
    names = []
    descs = []
    urls = []
    for programs in resource.findAll("div", {"class": ["modulo-type-programa"]}):
        for name in programs.select('meta[itemprop="name"]'):
            names.append(name.attrs['content'])
        for desc in programs.select('meta[itemprop="description"]'):
            descs.append(desc.attrs['content'])
        for url in programs.select('meta[itemprop="url"]'):
            urls.append(url.attrs['content'])

    podcasts = [names, descs, urls]
    return podcasts

podcasts = []
podcasts = get_podcasts(read_file("sandbox/content/podcast_internet_tecnologia_1.html"), podcasts)
pprint(podcasts)