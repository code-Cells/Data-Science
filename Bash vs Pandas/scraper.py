#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 23:11:20 2022

@author: eduardo
"""

import pandas as pd
import requests as r

from bs4 import BeautifulSoup as BS


resp = r.get('https://www.computerhope.com/unix/signals.htm')
soup = BS(resp.text, 'html5lib')
columns, data = [], []

header = soup.find_all('table')[0].find('tr')
for _ in header:
    if _ != '\n':
        try:
            columns.append(_.get_text())
            if len(columns) == 4:
                break
        except:
            continue
    
for info in soup.find_all('table')[0].find_all('tr')[1:]:
    temp_data = []
    for _ in info:
        try:
            temp_data.append(_.get_text())
        except:
            continue
    data.append(temp_data[1:len(temp_data):2])
    
signals = pd.DataFrame(data=data, columns=columns)
signals = signals.set_index(['Signal'])
signals.to_csv('signals.csv', sep=';')
