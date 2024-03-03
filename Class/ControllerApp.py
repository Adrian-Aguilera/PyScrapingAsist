from Class.GetdataGPT import GetdataGPT
from Class.PageStructureExtractor import Tools 
import os
from dotenv import load_dotenv
from openai import OpenAI


class EngineApp:
    
    load_dotenv()
    
    #Functions

    def venv_data():
        key = os.environ.get("Api_key")
        model = os.environ.get("model")
        page = os.environ.get("Page")
        return key, model, page
    
    def modelos(key):
        tool = Tools(key)
        return tool
    
    def get_classes(self, data):
        # Variables de entorno
        key, model, page = EngineApp.venv_data()
        # Crear instancia de GetdataGPT
        gpt = GetdataGPT(api_key=key)  
        # Obtener clases usando el método get_data de GetdataGPT
        getClassesData = gpt.get_data(model, data)
        
        return print(f'Clases: {getClassesData}\n')
    
    def main_engine(self):
            
        #variables de entorno
        key, model, page = EngineApp.venv_data()
        #modelos
        tool = EngineApp.modelos(key)
    
        #url = input('Introduce la url: ')
        structure = tool.getStructureHTML(page)
    
        #En esta funcion le paso como parametros la estructura y la cantidad de veces que quiero que se divida
        div_data = tool.FilterHTML(structure, 4)
    
        #mostrando datos...
        for index, data in enumerate(div_data):
            print(f"Imprimiendo parte {index + 1}...")
            if index+1 == 2:
                self.get_classes(data)
                