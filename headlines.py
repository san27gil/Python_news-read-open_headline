import webbrowser
import requests
from bs4 import BeautifulSoup
from datetime import datetime

headers = {'user-agent': 'Mozilla/5.0'}

# Last updated news
time_now = datetime.now().strftime("%d-%m-%Y")
print('\n')

# Greeting
hour = datetime.now().hour
if hour < 12 and hour > 3:
    print(' Good morning. Today is '+ time_now + ' and these are the most important news so far:')
elif hour >= 12 and hour < 20:
    print(' Good afternoon. Today is  '+ time_now + ' and these are the most important news so far:')
else:
    print(' Good night. Today is '+ time_now + ' and these are the most important news so far:')
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

# Ask for a link to open in browser
while True:
    x = int(input('Which one do you want to open?'))
    y = x - 1
    if x <=60:
        webbrowser.open(links[y])
screen_clear()
