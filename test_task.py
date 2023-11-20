# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 15:19:14 2023

@author: arsko
"""

from flask import Flask, request, jsonify
from tinydb import TinyDB
import re

app = Flask(__name__)
db = TinyDB('forms.json')
forms = db.table('templates')

# Загрузка существующих шаблонов форм из базы данных
templates = forms.all()


def validate_field_value(field_type, value):
    if field_type == "email":
        # Проверка валидности email
        if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$', value):
            return True
    elif field_type == "phone":
        # Проверка валидности телефонного номера
        if re.match(r'^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$', value):
            return True
    elif field_type == "date":
        # Проверка валидности даты
        if re.match(r'^(\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2})$', value):
            return True
    elif field_type == "text":
        return True
    return False


def get_matching_template(form_data):
    for template in templates:
        match_count = 0
        for field_name, field_value in form_data.items():
            if field_name in template and field_value == template[field_name]:
                match_count += 1
        if match_count == len(template)-1:
            return template.get('name')
    return None


@app.route('/get_form', methods=['POST'])
def process_form():
    form_data = request.form
    fields = {}
    for field_name, field_value in form_data.items():
        fields[field_name] = None
        for template in templates:
            if field_name in template and validate_field_value(field_value,template[field_name]):
                fields[field_name] = template[field_name]
                break
        if fields[field_name] is None:
            for field_type in ["date", "phone", "email", "text"]:
                if validate_field_value(field_type, field_value):
                    fields[field_name] = field_type
                    break
    matching_template = get_matching_template(fields)
    if matching_template:
        return matching_template
    else:
        return jsonify(fields)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000")
