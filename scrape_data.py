import numpy as np
import pandas as pd
import time
import requests
from bs4 import BeautifulSoup as bs



def get_soup(url) -> 'BeautifulSoup object':
    r = requests.get(url)
    # create a beautiful soup object
    soup = bs(r.content, 'lxml')
    return soup


def get_data(min: int=1, max: int=200) -> 'csv file':
    import csv
    
    pages = []
    for n in range(min, max + 1):
        time.sleep(0.2)
        url = f'https://nigeriapropertycentre.com/for-sale/houses/lagos/showtype?page={n}'
        pages.append(url)
    
    # create csv file
    with open('house_data.csv', 'w') as f:
        col_names = ['title', 'address', 'bed', 'bath', 'toilet', 'pkn_space', 'price']
        # instantiate
        my_csv = csv.writer(f, delimiter=',')
        
        # add the column names
        my_csv.writerow(col_names)
    
        for i, url in enumerate(pages):
            if i % 5 == 0:
                print(f'page ==> {i}')
                soup = get_soup(url)

            body = soup.select('.property-list .col-md-12')

            for idx, row in enumerate(body):
                if idx < len(body) - 3:
                    try:
                        title = row.select_one('.content-title').get_text()
                    except:
                        title = None
                    try:
                        address = row.select_one('.voffset-bottom-10 strong').get_text(strip=True)
                    except: 
                        address = None
                    try:    
                        bed = row.select_one('.aux-info li:nth-child(1)').get_text(strip=True)
                    except: 
                        bed = None  
                    try:    
                        bath = row.select_one('.aux-info li:nth-child(2)').get_text(strip=True)
                    except:
                        bath = None   
                    try:
                        toilet = row.select_one('.aux-info li:nth-child(3)').get_text(strip=True)
                    except:
                        toilet = None   
                    try:
                        pkn_space = row.select_one('.aux-info li:nth-child(4)').get_text(strip=True)
                    except:
                        pkn_space = None   
                    try:
                        price = row.select_one('.price+ .price').get_text(strip=True)
                    except:
                        price = None
                    
                    # write the files into my_csv object
                    my_csv.writerow([title, address, bed, bath, toilet, pkn_space, price])
