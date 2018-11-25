from ivoox_scraper_client import IvooxScraperClient

class Ranker:
    """
        Clase para obtener el listado de podcasts
    """
    def __init__(self,category_name, category_id,  max_page):
        self.podcasts = []
        self.max_page = max_page
        self.category_name = category_name
        self.category_id = category_id
    
    def build(self):
        """
            Construye el listado
        """
        ivooxScrapperClient = IvooxScraperClient(self.category_name, self.category_id)
        for page in range(1, self.max_page+1):
            self.__parse_resource(ivooxScrapperClient.request(page))
        
        return self.podcasts

    def get_podcasts(self):
        return self.podcasts

    def __parse_resource(self, resource):
        """
            Extrae el listado de podcasts 
            Devuelve una lista con el diccionario de elementos encontrados
        """
        for programs in resource.findAll("div", {"class": ["modulo-type-programa"]}):
            try:
                self.podcasts.append(
                    {
                        'title': ["%s" % name.attrs['content'] for name in programs.select('meta[itemprop="name"]')][0],
                        'description': ["%s" % desc.attrs['content'] for desc in programs.select('meta[itemprop="description"]')][0],
                        'url': ["%s" % url.attrs['content'] for url in programs.select('meta[itemprop="url"]')][0],
                        'episodes': ["%s" % micro.getText().strip() for micro in programs.select('.microphone')][0]
                    }
                )
            except IndexError:
                print("No se puede captuar el contenido") 
