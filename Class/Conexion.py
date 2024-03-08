import requests
from bs4 import BeautifulSoup
from Class.EngineIA import GetdataGPT
from openai import OpenAI 
from Class.Credentials import Credenciales
class Tools:
    
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.Gpt = GetdataGPT(api_key=api_key)
        
    def getUserAgentRamdon(self):
        key, model, _, PrototypeUserAgent = Credenciales.venv_data()
        UsertAgentRamdon = GetdataGPT.get_userAgent(model, PrototypeUserAgent)
        return UsertAgentRamdon
        
    def getStructureHTML(self,url):
        # Pendiente realizar funcion para el userAgent
        response = requests.get(url, timeout=5, headers={'User-Agent': self.getUserAgentRamdon()})

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            result = soup.prettify()
            return result + self.getUserAgentRamdon()
        else:
            return (f'Error al obtener la página. Código de respuesta: {response.status_code}')
    
    def FilterHTML (self, htmldata, n):
        longitud_html=len(htmldata)
        #se divide la longitud de la data entre el numero que le pasemos
        log_parte= longitud_html//n
        
        data = [htmldata[i:i + log_parte] for i in range(0, longitud_html, log_parte)]
        return data
    
    
    
    
    # Realizar Funct UserAgent