import requests
from bs4 import BeautifulSoup

class IvooxScraperClient:
    """
        Clase para construir la URL y hacer la petición a ivoox
        @see https://www.ivoox.com/podcast-internet-tecnologia_sc_f445_1.html
    """
    def __init__(self, category_name, category_id):
        self.url_base = "https://www.ivoox.com/podcast-{0}_sc_f{1}_{2}.html"
        self.category_name = category_name
        self.category_id = category_id
        self.params = {}
    
    def request(self, page):
        """
            Generamos la petición para una página dada
        """
        url = self.__format_url(page)
        return self.__get_content(url)

    def __format_url(self, page):
        """
            Clase privada pra formatear de forma correcta la URL a solicitar
        """
        return self.url_base.format(self.category_name, self.category_id, page)

    def __get_content(self, url):
        """
            Clase privada que extrae el contenido de unas URL específicas
        """
        res = requests.get(url)
        # Levanta el error solo si algo fue mal (errores 400)
        try:
            res.raise_for_status()
        except Exception as exc:
            print('Problem! %s' % (exc))
        
        soup = BeautifulSoup(res.text, "lxml")

        return soup