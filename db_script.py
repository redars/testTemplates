# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 15:31:47 2023

@author: arsko
"""

from tinydb import TinyDB, Query

db = TinyDB('forms.json')
templates = db.table('templates')
templates.insert({'name': 'Order Form',
           'user_email': 'email',
           'user_phone': 'phone',
           'order_date': 'date',
           'order_comment': 'text'})