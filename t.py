# Тестирование API https://ndt-edu.ru/mgw/ek877/ek99s.html

# Основной формат передачи данных - json
# Код сайта на PHP
# SQL база - Postgres ИЗМИНЕНИЯ !!!

import os.path
import json
import requests
from requests.structures import CaseInsensitiveDict
import datetime
from typing import List, Dict, Union
import pytest

DateDict = Dict[str, Union[str, int]]

MOODLE_URL: str = "https://ndt-edu.ru/mgw/test_mpost.php"
MOODLE_USERNAME = "ceabbcbdahce_16"

# Функция для получения данных из Moodle
def fetch_moodle_data() -> Dict[str, DateDict]:
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = f'kmd=5&&username={MOODLE_USERNAME}'
    
    response = requests.post(MOODLE_URL, headers=headers, data=data.encode('utf-8'))
    data_dict: Dict[str, DateDict] = {}
    
    if response.status_code == 200:
        data_dict = json.loads(response.text)
        if data_dict.get('ok'):
            return  data_dict.get('msg', {})
    
    return data_dict


def sum2(x, y):
    return x + y

def sum3(x, y):
    return x + y

def test_sum2():
    assert sum2(15, 8) == 23

def test_sum3():
    assert sum3(15, 8) == 44
# Выполнить запрос к API
#print(fetch_moodle_data())
