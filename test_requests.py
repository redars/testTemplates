# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 16:00:48 2023

@author: arsko
"""

import requests

url = "http://127.0.0.1:5000/get_form"
data = {   'user_email': 'arskot2002@yan.ru',
           'user_phone': '+7 985 424 40 25',
           'order_date': '2023-10-10',
           'order_comment': 'sometext2'}

response = requests.post(url=url,data = data)
print(response.text)

data = {   'user_email': '24dsdsf',
           'user_phone': '+7 985 424 40 25',
           'order_date': '2023-10-10',
           'order_comment': 'sometext1234'}

response = requests.post(url=url,data = data)
print(response.text)