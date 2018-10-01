import requests
from bs4 import BeautifulSoup

def py_spider():
    while True:
        url = 'https://docs.python.org/3/'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.findAll('a', {'class': 'biglink'}):
            href = "https://docs.python.org/3/" + link.get('href')
            title = link.string
            #print(href)
            print(title)
            get_single_item_data(href)

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    for item_name in soup.findAll('tr', {'class': 'field-odd field'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = "https://docs.python.org/3/" + link.get('href')
        print(href)
    print('***************************************************************************************************')

py_spider()
