import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0",
}

text_to_search= input('>>')
text_to_search= text_to_search.replace(' ','+')
def search(text_to_search):
    url= f'https://duckduckgo.com/html/?q=0{text_to_search}'
    page = requests.get(url, headers=headers).text
    soup=BeautifulSoup(page, 'html.parser')

    # error_search= soup.find('div', class_='msg__wrap', href= False)
    # print(error_search)

    # first_link = soup.find("a", class_="result__url", href=True)
    first_link = soup.find("a", class_="result__a", href=True)
    print(first_link['href'])

search(text_to_search)
# print(url)