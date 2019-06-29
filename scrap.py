from bs4 import BeautifulSoup
from selenium import webdriver
import sys,csv
import pandas as pd

city = 'Jaipur'#Enter City Name Here

browser = None

try:
    browser = webdriver.Chrome(executable_path='/Users/roshanchokshi/Downloads/chromedriver')#Replace it with your weddriver path.
except Exception as error:
    print(error)

class ZomatoRestaurantLinkGen:
    def __init__(self, url):
        self.url = url
        self.html_text = None
        try:
            browser.get(self.url)
            self.html_text = browser.page_source
        except Exception as err:
            print(str(err))
            return
        else:
            print('Access successful.')

        self.soup = None
        if self.html_text is not None:
            self.soup = BeautifulSoup(self.html_text, 'lxml')

    def getPage(self):
        soup = self.soup
        for tag in soup.find_all("div",attrs={'class':'col-l-4 mtop pagination-number'}):
            for count in tag.find_all('b'):
                if not count.text == '1':
                    return count.text
    def scrap(self):
        soup = self.soup
        name=[]
        rate=[]
        price=[]
        for tag in soup.find_all("a", attrs={'data-result-type': 'ResCard_Name'}):
            name.append(tag.text.strip())
        for tag in soup.find_all("div", attrs={'class': 'rating-popup'}):
            rate.append(tag.text.strip())
        for tag in soup.find_all("span", attrs={'class': 'col-s-11 col-m-12 pl0'}):
            price.append(tag.text.strip().replace('"','').replace(',','').replace('₹',''))
        for i in range(len(rate)):
            try:
                row=[name[i],rate[i],price[i]]

                with open('zomato.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
            except:
                continue

if __name__ == '__main__':
    if browser is None:
        print("Selenium not opened")
        sys.exit()
    zr = ZomatoRestaurantLinkGen('https://www.zomato.com/{}/restaurants?page=1'.format(city))
    c = zr.getPage()
    print(c)
    for x in range(1, int(c)+1):
        print(str(x) + '\n')
        zr = ZomatoRestaurantLinkGen('https://www.zomato.com/{}/restaurants?page={}'.format(city,x))
        zr.scrap()
    browser.close()

    df = pd.read_csv('zomato.csv', delimiter=',')

    df = df[df['rating'] != 'NEW'][df['rating'] != '-']

    df = df.sort_values(['rating', 'cost_for_two'],
                        ascending=[False, True])  # parameter ascending is applied to 'col1' and 'col2' respectively.

    df.to_csv('sorted.csv')