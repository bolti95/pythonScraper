from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
path = '../data/'
urls = [
    "https://www.visitisleofman.com/", 
    "https://blisshotels.co.uk/", 
    "https://www.visitgreenwich.org.uk/", 
    "https://www.visitcaymanislands.com/en-gb",
    "https://www.visitguernsey.com/"
]


def scrape():
    dict = {
        'Scraped Text': [],
        'URLs': []
    }
    for url in urls:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
        visible_text = soup.getText()
        dict['Scraped Text'].append(visible_text)
        dict['URLs'].append(url)

    df = pd.DataFrame(dict)   
    df.to_csv(path+'webtext.csv', index=False, encoding='utf-8')
    if len(urls) == len(dict["URLs"]):
            return True
    

if __name__ == "__main__":
    # result = scrape(urls)
    # print(result)
    print("success!")