import requests
from bs4 import BeautifulSoup
from Class.GetdataGPT import GetdataGPT
from openai import OpenAI 
class Tools:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.Gpt = GetdataGPT(api_key=api_key)
        
    def getStructureHTML(self,url):
        
        #funcion para obtener user agent rotativos
        ##self.userAgent = self.Gpt.UserAgent()
        self.url = url
        response = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            result = soup.prettify()
            return result
        else:
            return (f'Error al obtener la página. Código de respuesta: {response.status_code}')