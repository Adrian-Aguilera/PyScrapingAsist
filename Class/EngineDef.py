from bs4 import BeautifulSoup


class EngineDef():
    @staticmethod
    def Classhtml(html):
        soup = BeautifulSoup(html, 'html.parser')
        clases = set()
        
        # Buscar todas las etiquetas <img> y <div> y extraer sus clases
        for etiqueta in soup.find_all(['img', 'a']):
            if 'class' in etiqueta.attrs:
                for clase in etiqueta['class']:
                    clases.add(clase)
        
        return clases

