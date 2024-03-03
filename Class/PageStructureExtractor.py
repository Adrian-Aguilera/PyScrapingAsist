import requests
from bs4 import BeautifulSoup
from Class.GetdataGPT import GetdataGPT
from openai import OpenAI 
class Tools:
    
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.Gpt = GetdataGPT(api_key=api_key)
        
    def getUserAgentRamdon(self):
        #
        return
        
    def getStructureHTML(self,url):
        # Pendiente reaizar funcion para el userAgent
        self.url = url
        response = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            result = soup.prettify()
            return result
        else:
            return (f'Error al obtener la página. Código de respuesta: {response.status_code}')
    
    def FilterHTML (self, htmldata, n):
        longitud_html=len(htmldata)
        #se divide la longitud de la data entre el numero que le pasemos
        log_parte= longitud_html//n
        
        data = [htmldata[i:i + log_parte] for i in range(0, longitud_html, log_parte)]
        return data
    
    
    
    
    # Realizar Funct UserAgent