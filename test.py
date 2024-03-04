from bs4 import BeautifulSoup

def extraer_clases_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    clases = set()
    
    # Buscar todas las etiquetas <img> y <div> y extraer sus clases
    for etiqueta in soup.find_all(['img', 'div']):
        if 'class' in etiqueta.attrs:
            for clase in etiqueta['class']:
                clases.add(clase)
    
    return clases

# Ejemplo de uso
html = '''
<div class="container">
    <img src="imagen.jpg" class="responsive img-thumbnail">
    <div class="row highlight">
        <img src="otra-imagen.jpg" class="detail">
    </div>
</div>
'''
clases_encontradas = extraer_clases_html(html)
print(clases_encontradas)
