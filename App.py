from Class.GetdataGPT import GetdataGPT
from Class.PageStructureExtractor import Tools 


key = '' 
tool = Tools(key)
model = "gpt-3.5-turbo"

url = input('Introduce la url: ')
structure = tool.getStructureHTML(url)
# Proceso De Division
prueba = tool.FilterHTML(structure)
print(prueba)


#html_content = structure
#gpt = GetdataGPT(key)
#
#print(html_content)
#print(f'las clases son: {gpt.get_data(model, html_content)}')
