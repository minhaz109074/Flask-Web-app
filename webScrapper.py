# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 23:54:59 2022

@author: Minhazul Abedin
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
def scrapping(url):
    response = requests.get(url)
    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent,'html.parser')
    test = soup.find_all(attrs = {'class': 'entry-content'})
    data = test[0].text.split('\n')
    data = data[10:-1]
    df = pd.DataFrame(data, columns=['Newly added scoupus indexed journals Title'])
    df.to_csv("output.csv")
def csvToHtml(csv):
    df = pd.read_csv(csv, encoding='latin-1')
    df.to_html("list.html")
    
if __name__ == "__main__":
    
    url = 'https://phdtalks.org/2021/05/newly-added-scopus-journals.html'
    scrapping(url)
    csvToHtml("./output.csv")
