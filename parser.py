#пример парсинга сайта "Aвторио"
import requests
import csv
from fake_useragent import UserAgent # присоединение фейк-юзерагент позволяет слелать запросы анонимными;
from bs4 import BeautifulSoup
import os
URL = "https://auto.ria.com/uk/car/opel/"

user = UserAgent().random
HEADERS = {
            'user_agent':user
          }
#HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.1.2222.33 Safari/537.36
HOST = "https://auto.ria.com"
FILE = 'cars.csv'


def get_html (url, params = None):
        r = requests.get (url, headers = HEADERS, params = params)
        return r

def get_pages_count (html):
    soup = BeautifulSoup (html, 'html.parser')
    pagenation = soup.find_all ('span', class_='page-item mhide')
    if pagenation:
        return int( pagenation[-1].get_text())
    else:
        return 1


def get_content (html):
    soup = BeautifulSoup (html, 'html.parser')
    items = soup.find_all ('div', class_='content-bar')
    #print (iteams)
    cars = []
    for item in items:
        ua_price = item.find ( 'span', class_ ='i-block' )
        if ua_price:
            ua_price = ua_price.get_text()
        else:
            ua_price = "Specify the price"
        cars.append ({
            'title': item.find ( 'div', class_='item ticket-title' ) .get_text(strip=True),
            'link': item.find ('a', class_='address') .get('href'),
            'usd_price': item.find ('span', class_='green') .get_text(),
            'ua_price' : ua_price,
            'city': item.find ('li', class_='view-location') .get_text(),
            })
    return cars


def save_file (items, path):
    with open (path, 'w', newline = '') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Brand', 'link', 'usd_price', 'ua_price', 'City'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['usd_price'], item['ua_price'], item['city']])

def parse ():
        URL = input ("Enter URL: ")
        URL = URL.strip() 
        html = get_html (URL)
        if html.status_code == 200:
            cars = []
            pages_count = 1#get_pages_count (html.text)
            for page in range (1, pages_count + 1):
                print("Page parsing: " + str(page) + " of " + str(pages_count))
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))
                #cars = get_content (html.text)
            #print(cars)
            save_file(cars, FILE)
            print("Received  " + str(len(cars)) + " cars")
            os.startfile(FILE) 
        else:
            print ('Error')

parse()
