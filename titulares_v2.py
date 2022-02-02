import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Añadimos header para que no de error en algunas webs. En este caso simulamos navegar desde Mozilla.
headers = {'user-agent': 'Mozilla/5.0'}

# Creamos la fecha en que se actualizan las noticias:
time_now = datetime.now().strftime("%d-%m-%Y")
print('\n')

# Saludo según la hora del día:
hour = datetime.now().hour
if hour < 12 and hour > 3:
    print('Buenos días. Hoy es '+ time_now + ' y esto es lo más destacado de la mañana:')
elif hour >= 12 and hour < 20:
    print('Buenas tardes. Hoy es '+ time_now + ' y esto es lo más destacado de la tarde:')
else:
    print('Buenas noches. Hoy es '+ time_now + ' y esto es lo más destacado de la noche:')
print('\n')

# Diario de Pontevedra:
url = 'https://www.diariodepontevedra.es'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h2')
top15 = headlines[:15]

print('<--------------------Diario de Pontevedra-------------------->')

for index, x in enumerate(top15):
    print(index + 1, ':', x.text.strip() + '.')

# La Voz de Galicia:
url2 = 'https://www.lavozdegalicia.es'
response2 = requests.get(url2, headers=headers)

soup2 = BeautifulSoup(response2.text, 'html.parser')
headlines2 = soup2.find('body').find_all('h2')
top15_2 = headlines2[:15]

print('\n')
print('<--------------------La Voz de Galicia-------------------->')

for index, x in enumerate(top15_2):
    print(index + 1, ':', x.text.strip() + '.')

# El Mundo:
url3 = 'https://www.elmundo.es'
response3 = requests.get(url3, headers=headers)

soup3 = BeautifulSoup(response3.text, 'html.parser')
headlines3 = soup3.find('body').find_all('h2')
top15_3 = headlines3[:15]

print('\n')
print('<--------------------El Mundo-------------------->')

for index, x in enumerate(top15_3):
    print(index + 1, ':', x.text.strip() + '.')

# Financial Times:
url4 = 'https://cincodias.elpais.com'
response4 = requests.get(url4, headers=headers)

soup4 = BeautifulSoup(response4.text, 'html.parser')
headlines4 = soup4.find('body').find_all('h2')
top15_4 = headlines4[:15]

print('\n')
print('<--------------------Cinco Días-------------------->')

for index, x in enumerate(top15_4):
    print(index + 1, ':', x.text.strip() + '.')
