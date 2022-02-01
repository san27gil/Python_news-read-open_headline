import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Añadimos header para que no de error en algunas webs. En este caso simulamos navegar desde Mozilla.
headers = {'user-agent': 'Mozilla/5.0'}

# Especificamos fecha y hora en la que se actualizaron las noticias:
print('\n')
time_now = datetime.now().strftime("%Y-%m-%d_%I:%M:%S_%p")
print('Última actualización: ', time_now)
print('\n')

# La Voz de Galicia:
url = 'https://www.lavozdegalicia.es'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h2')
top15 = headlines[:15]

print('<--------------------La Voz de Galicia-------------------->')

for index, x in enumerate(top15):
    print(index + 1, ':', x.text.strip())

# Diario de Pontevedra:
url2 = 'https://www.diariodepontevedra.es'
response2 = requests.get(url2, headers=headers)

soup2 = BeautifulSoup(response2.text, 'html.parser')
headlines2 = soup2.find('body').find_all('h2')
top15_2 = headlines2[:15]

print('\n')
print('<--------------------Diario de Pontevedra-------------------->')

for index, x in enumerate(top15_2):
    print(index + 1, ':', x.text.strip())

# El Economista:
url3 = 'https://www.eleconomista.es'
response3 = requests.get(url3, headers=headers)

soup3 = BeautifulSoup(response3.text, 'html.parser')
headlines3 = soup3.find('body').find_all('h2')
top15_3 = headlines3[:15]

print('\n')
print('<--------------------El Economista-------------------->')

for index, x in enumerate(top15_3):
    print(index + 1, ':', x.text.strip())
