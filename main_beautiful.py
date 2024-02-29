import lxml
import requests
import json
from bs4 import BeautifulSoup


url = 'http://quotes.toscrape.com'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

quotes_list = []

for i in range(0, len(quotes)):
    tags_list = []
    tagsforquote = tags[i].find_all('a', class_='tag')
    for tagforquote in tagsforquote:
        tags_list.append(tagforquote.text)
    tmp_dict = {
        'tags': tags_list,
        'author': authors[i].text,
        'quote': quotes[i].text.strip(),
    }
    quotes_list.append(tmp_dict)

print(quotes_list)

with open('quotes.json', 'w', encoding='utf-8') as fd:
    json.dump(quotes_list, fd, ensure_ascii=False, indent=2)
