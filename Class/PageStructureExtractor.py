import requests
from bs4 import BeautifulSoup

class Tools:
    def getStructureHTML(self,url):
        self.url = url
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            result = soup.prettify()
            return result
        else:
            return (f'Error al obtener la página. Código de respuesta: {response.status_code}')