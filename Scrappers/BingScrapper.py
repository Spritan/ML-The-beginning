import requests
from bs4 import BeautifulSoup

def getResults(text):
    text = text.replace(" ","+")
    # print(text)
    url = f'https://www.bing.com/search?q="{text}"&qs=n&form=QBRE&sp=-1&pq={text.lower()}"' # f'https://www.google.com?q="{text}&oq={text}&sourceid=chrome&ie=UTF-8"'  # "https://dataquestio.github.io/web-scraping-pages/simple.html"

    # Crafting the proper request to fool Google
    header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0'}
    
    page = requests.get(url, headers= header, allow_redirects=True)

    content = BeautifulSoup(page.content, 'html.parser')
    # print(content.prettify())
    # return content
    # link= content.find('h2')
    element=content.find('li',class_='b_algo').h2

    try:
        link= element.find('a')['href']
        print(link)
    except:
        print('')


getResults('vs code')
