from Class.GetdataGPT import GetdataGPT
from Class.PageStructureExtractor import Tools 
import os
from dotenv import load_dotenv

load_dotenv()

def venv_data():
    key = os.environ.get("Api_key")
    model = os.environ.get("model")
    
    return key, model

def modelos(key):
    tool = Tools(key)

    return tool

if __name__ == "__main__":
    #variables de entorno#
    key, model, = venv_data()
    #modelos#
    tool = modelos(key)
    
    url = input('Introduce la url: ')
    structure = tool.getStructureHTML(url)
    
    #en esta funcion le paso como parametros la estructura y la cantidad de veces que quiero que se divida
    div_data = tool.FilterHTML(structure, 4)
    
    #mostrando datos...
    for index, data in enumerate(div_data):
        print(f"Imprimiendo parte {index + 1}...")
        if index+1 == 2:
            print(data)