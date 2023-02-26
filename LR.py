from bs4 import BeautifulSoup
import requests
url = 'https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php'#передаем URL адрес
page = requests.get(url) # отправляем запрос методом get на данный адрес и получаем ответ в переменную
# print(page.status_code)
allKafedra = []
soup = BeautifulSoup(page.text, "html.parser")
# print(soup)
allKafedra = soup.findAll('div', class_='main__content')#находим контейнер снужным классом и тегом
description = ''
# print(allKafedra)
for kafedra in allKafedra: #проходим циклом по содержимому контейнера
    if kafedra.find('br'):# если есть тег br
        description=kafedra.text #записываем в переменную содержимое тега
print(description)
# запись в файл

f=open('OmSTU_kaf.txt', 'w')
f.write(description)

f.close()