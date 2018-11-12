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
    for programs in resource.findAll("div", {"class": ["modulo-type-programa"]}):
        try:
            podcasts.append(
                {
                    'title': ["%s" % name.attrs['content'] for name in programs.select('meta[itemprop="name"]')][0],
                    'description': ["%s" % desc.attrs['content'] for desc in programs.select('meta[itemprop="description"]')][0],
                    'url': ["%s" % url.attrs['content'] for url in programs.select('meta[itemprop="url"]')][0],
                    'episodes': ["%s" % micro.getText().strip() for micro in programs.select('.microphone')][0]
                }
            )
        except IndexError:
            print("No se puede captuar el contenido") 

    return podcasts

podcasts = []
get_podcasts(read_file("sandbox/content/podcast_internet_tecnologia_1.html"), podcasts)
get_podcasts(read_file("sandbox/content/podcast_internet_tecnologia_2.html"), podcasts)
pprint(podcasts)