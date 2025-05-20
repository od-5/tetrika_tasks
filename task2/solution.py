import csv
import string
from typing import Optional
from urllib.parse import quote
from urllib.request import urlopen

from bs4 import BeautifulSoup

BASE_URL = 'https://ru.wikipedia.org'
WIKI_URL = BASE_URL + '/wiki/' + quote('Категория:Животные_по_алфавиту')

result = {}


def wiki_animal_parser(url: str) -> Optional[str]:
    response = urlopen(url)
    content = response.read()
    soup = BeautifulSoup(content, 'html.parser')
    div = soup.find(id='mw-pages')

    def _get_item_count(div_el):
        _letter = div_el.find('h3').get_text(strip=True)
        _items = div_el.find_all('li')
        return _letter, len(_items)

    for group in div.find_all('div', class_='mw-category-group'):
        letter, items = _get_item_count(group)
        if letter.lower() in string.ascii_lowercase:
            raise StopIteration
        letter_result = result.get(letter, 0)
        result[letter] = letter_result + items
    next_link = div.find('a', string='Следующая страница')
    if next_link:
        return BASE_URL + next_link['href']
    return None


if __name__ == '__main__':
    try:
        link = WIKI_URL
        while link:
            link = wiki_animal_parser(link)
    except StopIteration:
        with open('beasts.csv', 'w', newline='') as f:
            csvwriter = csv.writer(f, delimiter=',')
            for letter, count in result.items():
                csvwriter.writerow([letter, count])
