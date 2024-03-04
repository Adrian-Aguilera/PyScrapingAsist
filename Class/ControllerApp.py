from Class.EngineIA import GetdataGPT
from Class.Conexion import Tools 
from Class.EngineDef import EngineDef
import os
from dotenv import load_dotenv

class EngineApp:
    def __init__(self, EngineIA=None, EngineDef=None):
        self.EngineIA =EngineIA
        self.Enginedef = EngineDef
    
    load_dotenv()
    #Functions...
    def venv_data():
        key = os.environ.get("Api_key")
        model = os.environ.get("model")
        page = os.environ.get("pag")
        promt = os.environ.get("Promt")
        print(page)
        return key, model, page, promt
    
    def modelos(key):
        tool = Tools(key)
        return tool
    
    #metodo para usar IAengine
    def get_classes(self, data):
        # Variables de entorno
        key, model, _, promt = EngineApp.venv_data()
        # Crear instancia de GetdataGPT
        gpt = GetdataGPT(api_key=key, promt=promt)  
        # Obtener clases usando el método get_data de GetdataGPT
        getClassesData = gpt.get_data(model, data)
        
        return getClassesData
    
    #metodo para usar EngineDefault.
    def EngineDefault(self, data):
        clases = EngineDef.Classhtml(data)
        return clases
    
    def main_engine(self):   
        #variables de entorno
        key, _, page, _ = EngineApp.venv_data()
        #modelos
        tool = EngineApp.modelos(key)
    
        structure = tool.getStructureHTML(page)
        if self.Enginedef:
            clases_encontradas = self.EngineDefault(structure)
            print(f"page: {page}")
            print(f"CLASES (Diagnóstico): {clases_encontradas}")
            
        elif self.EngineIA:
            #En esta funcion le paso como parametros la estructura y la cantidad de veces que quiero que se divida
            div_data = tool.FilterHTML(structure, 4)
            #mostrando datos..
            for index, data in enumerate(div_data):
                if index+1 == 2:
                    #print(f"Dato procesado: {data}")
                    if self.EngineIA:
                        clases_encontradas = self.get_classes(data)
                        print(f"CLASES (Diagnóstico): {clases_encontradas}")
        
    """"""
