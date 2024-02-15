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
        
        
        
    
    def FilterHTML (self, html):
        # Variables Necesarias para realizar la peticion
        key = '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' 
        model = "gpt-3.5-turbo"
        # Instancia de la clase 
        gpt = GetdataGPT(key)
      
        # Division Del Codigo HTML
        middle_index = len(html) // 2
        firstPart = html[:middle_index]
        SecondPart = html[middle_index:]
        # Envía Cada Parte Por Separado a ChatGPT
        html1 = gpt.get_data(model, firstPart.strip()) 
        html2 = gpt.get_data(model, SecondPart.strip())
        # Concatenamos los Resultados De ChatGPT
        full_html_structure = f' Las Clases Son:  \nParte 1: {html1.strip()} \nParte 2: {html2.strip()}'
        return full_html_structure