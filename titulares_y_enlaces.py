import webbrowser
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Simulamos navegar desde Mozilla.
headers = {'user-agent': 'Mozilla/5.0'}

# Fecha de actualización de las noticias:
time_now = datetime.now().strftime("%d-%m-%Y")
print('\n')

# Saludo:
hour = datetime.now().hour
if hour < 12 and hour > 3:
    print(' Buenos días. Hoy es '+ time_now + ' y esto es lo más destacado de la mañana:')
elif hour >= 12 and hour < 20:
    print(' Buenas tardes. Hoy es '+ time_now + ' y esto es lo más destacado de la tarde:')
else:
    print(' Buenas noches. Hoy es '+ time_now + ' y esto es lo más destacado de la noche:')
print('\n')

links =[]
index = 0

# Diario de Pontevedra
url = 'https://www.diariodepontevedra.es'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find('body').find_all('article')
top15 = articles[:15]

print('<----------Diario de Pontevedra---------->')
for article in top15:
    index = index + 1
    headline = article.h2.text.strip()
    link = article.h2.find('a', href=True)
    links.append('https://www.diariodepontevedra.es' + link['href'].strip())
    news = headline + '.'
    print(index, ':', news)
print('\n')

# La Voz de Galicia
url = 'https://www.lavozdegalicia.es'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find('body').find_all('article')
top15 = articles[:15]


print('<-----------La Voz de Galicia----------->')
for article in top15:
    index = index + 1
    headline = article.h2.text.strip()
    link = article.h2.find('a', href=True)
    links.append('https://www.lavozdegalicia.es' + link['href'].strip())
    news = headline + '.'
    print(index, ':', news)
print('\n')

# El Mundo
url = 'https://www.elmundo.es'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find('body').find_all('article')
top15 = articles[:15]


print('<--------------El Mundo-------------->')
for article in top15:
    index = index + 1
    headline = article.h2.text.strip()
    link = article.find('a', href=True)
    links.append(link['href'].strip())      # Le quité lo de añadir la primera parte
    news = headline + '.'
    print(index, ':', news)
print('\n')

# Cinco Dias
url = 'https://cincodias.elpais.com'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find('body').find_all('article')
top15 = articles[:15]


print('<-------------Cinco Dias------------->')
for article in top15:
    index = index + 1
    headline = article.h2.text.strip()
    link = article.find('a', href=True)
    links.append('https://cincodias.elpais.com' + link['href'].strip())
    news = headline + '.'
    print(index, ':', news)

print('\n')
while True:
    x = int(input('¿Qué noticia quieres leer?: '))
    y = x - 1
    if x <=60:
        webbrowser.open(links[y])
screen_clear()
