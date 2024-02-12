from openai import OpenAI
from Class.GetdataGPT import GetdataGPT
from Class.PageStructureExtractor import Tools 

tool = Tools()
key = '' 
model = "gpt-3.5-turbo"

url = input('Introduce la url: ')
structure = tool.getStructureHTML(url)
html_content = structure
gpt = GetdataGPT(key)

print(f'las clases son: {gpt.get_data(model, html_content)}')