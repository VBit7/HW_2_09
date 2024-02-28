import lxml
import requests
from bs4 import BeautifulSoup


url = 'http://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')

print(quotes)
