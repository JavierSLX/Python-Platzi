import requests
from bs4 import BeautifulSoup
import urllib

def run():
    # Obtendremos las imagenes de 1 al 5 de la pagina
    for i in range(1, 6):
        response = requests.get('https://xkcd.com/{}'.format(i))

        # Se parsea el contenido obtenido a HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Obtenemos la referencia al contenedor de la etiqueta
        imageContainer = soup.find(id = 'comic')

        # Obtenemos la url
        imageUrl = imageContainer.find('img')['src']

        # Obtenemos la referencia del nombre de la imagen
        imageName = imageUrl.split('/')[-1]

        # Guardamos la imagen
        print('Descargando la imagen {}'.format(imageName))
        urllib.urlretrieve('https:{}'.format(imageUrl), imageName)

if __name__ == '__main__':
    run()