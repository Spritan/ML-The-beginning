import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')

# Line we have to update outdated line:
chrome_options.add_argument(
    'userAgent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
browser = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options)


def find(sentence_to_search):
    sentence_to_search = sentence_to_search.replace(' ', '+')
    url = f'https://www.google.com/search?q="{sentence_to_search}"&num100'

    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    error_result1 = soup.find('div', class_='card-section rQUFld')
    error_result2 = soup.find('div', class_='card-section')
    if error_result1 == None and error_result2==None:
        link = soup.find('div', class_='yuRUbf').a['href']
        return link
    else:
        return ''


sentence_to_search = input("Enter what you want to search >>")
print('searching🔎...')

print(find(sentence_to_search))