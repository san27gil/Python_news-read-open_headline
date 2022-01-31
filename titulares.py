import requests
from bs4 import BeautifulSoup

# Añadimos header para que no de error en algunas webs. En este caso simulamos navegar desde Mozilla.
headers = {'user-agent': 'Mozilla/5.0'}

# Cada web organizar el html de manera diferente. En este caso usa h2 para los titulares. 
url = 'https://www.diariodepontevedra.es'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h2')

# Creamos un loop para cada etiqueta h2 en la que nos vaya enumerando cada noticia.
for index, x in enumerate(headlines):
    print('\n')
    print(index + 1, ':', x.text.strip() + '\n')
