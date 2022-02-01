import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Añadimos header para que no de error en algunas webs. En este caso simulamos navegar desde Mozilla.
headers = {'user-agent': 'Mozilla/5.0'}

# Fecha y hora en la que se actualizan las noticias:
print('\n')
time_now = datetime.now().strftime("%Y-%m-%d_%I:%M:%S_%p")
print('Última actualización: ', time_now)
print('\n')

# Saludo:
hour = datetime.now().hour
if hour < 12 and hour > 3:
    print('Buenos días. Esto es lo más destacado de la mañana:')
elif hour >= 12 and hour < 20:
    print('Buenas tardes. Esto es lo más destacado de hoy:')
else:
    print('Buenas noches. Esto es lo más destacado de hoy:')
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

# Financial Times:
url4 = 'https://www.elmundo.es'
response4 = requests.get(url4, headers=headers)

soup4 = BeautifulSoup(response4.text, 'html.parser')
headlines4 = soup4.find('body').find_all('h2')
top15_4 = headlines4[:15]

print('\n')
print('<--------------------El Mundo-------------------->')

for index, x in enumerate(top15_4):
    print(index + 1, ':', x.text.strip())
