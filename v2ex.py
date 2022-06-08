from urllib import request
import requests
import sys
from bs4 import BeautifulSoup

url_format = "https://www.v2ex.com/go/jobs?p=%d"

# 搜索关键词
key_words = ['外企', '新加坡', '澳洲', '欧洲', '日本', '新西兰']

base_url = 'https://www.v2ex.com'

proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}

def is_match(text):
    for word in key_words:
        if word in text:
            return True

    return False

for i in range(1, 60):
    url = url_format % i
    print(url)
    res = requests.get(url=url, timeout=5, proxies=proxies)
    if res.status_code != 200:
        print(res.status_code)
        sys.exit(1)
    html = res.text
    soup = BeautifulSoup(html, features="html.parser")
    spans = soup.find_all('span', {'class' : 'item_title'})
    for span in spans:
        text = span.get_text()
        
        if is_match(text):
            link = span.find('a')['href']
            print(text, base_url + link)
    
