# -*- coding:utf-8 -*-


import requests
from bs4 import BeautifulSoup



city_list = []

def getCity():
    rank_url = 'http://www.pm25.com/rank.html'
    rank_html = requests.get(rank_url)
    rank_soup = BeautifulSoup(rank_html.text, 'html.parser')
    for rank_city in rank_soup.select('a.pjadt_location'):
        pinyin = rank_city.get('href')
        cityname = pinyin.replace('/city/', '').replace('.html', '')
        if cityname in city_list:
            pass
        else:
            city_list.append(cityname)

if __name__ == '__main__':
    getCity()