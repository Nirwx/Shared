import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import json

x = True

try:
    with open('mtp_items.json', 'r+') as f:
        item_dict = json.load(f)
except Exception as e:
    print(e)
    item_dict = {}

while x:
    r = requests.get('')
    soup = BeautifulSoup(r.content, 'html.parser')
    items = soup.find_all('div', {'class': 'content'})
    for item in items:
        title = item.findChild('a', {'class': 'header'}).text
        url = '' + item.findChild('a', {'class': 'header'}).get('href')
        price = item.findChild('span', {'class': 'price'}).text
        #print(float(price))
        #print(type(item_dict[title]['price']))
        if title in item_dict and item_dict[title]['price'] == price:
            pass
        else:
            try:
                if title not in item_dict:
                    item_dict[title] = {'price': price, 'url': url}
                    print('Found a new item at {}: '.format(datetime.now()))
                    print(title, '\n', price, '\n', url)
                else: #Calculate price drop
                    #print(type(price))
                    pass
            except Exception as e:
                print(e)
    with open('mtp_items.json', 'w+') as f:
        f.write(json.dumps(item_dict))
    time.sleep(600)
