import requests, json
from requests.structures import CaseInsensitiveDict

# ----------------------------------------------------------------------------
# https://api.openweathermap.org/data/2.5/weather -- Погода в мире с API REST
# ----------------------------------------------------------------------------

url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "8607204f856daa81c1e77aa8bfcec941"

# На вход строка города: 'Tver' ... на выход словарь
def get_weather(city: str) -> dict:
    rez: dict = {}
    # Устанавливаем заголовок в utf-8
    data: str = '?q=' + city + "&units=metric&appid=" + api_key
    # API Call
    api_request: requests.models.Response = requests.get(url + data)
    if api_request.status_code == 200:
        # Без ошибок
        rez = json.loads(api_request.text)
    else:
        # Есть ошибки ... лень обрабатывать
        pass
    # Возврат результата
    return rez

# Проверка одного города
def allTestNameCity(name: str)-> None:
    d: dict = get_weather(name)
    if d:
        assert(d['name'] == name )
    else:
        assert(False)

# Пишем функции проверки городов
def test_London() -> None:
    d: dict = get_weather('London')

def test_Moscow() -> None:
    d: dict = get_weather('Moscow')

def test_Tver() -> None:
    d: dict = get_weather('Tver')

def test_Minsk() -> None:
    d: dict = get_weather('Minsk')


# ----------------------------------------------------------------------------
# https://restful-api.dev/ -- Интернет ресурс для тренировки работы с API REST
# ----------------------------------------------------------------------------
url2 = "https://api.restful-api.dev/objects"

def get_allObjectsr() -> dict:
    rez: dict = {}
    # API Call
    api_request: requests.models.Response = requests.get(url2)
    if api_request.status_code == 200:
        # Без ошибок
        rez = json.loads(api_request.text)
    else:
        # Есть ошибки ... лень обрабатывать
        pass
    # Возврат результата
    return rez

# Проверим количество объектов
def test_CountIdObjects() -> None:
    d: dict = get_allObjectsr()
    assert(len(d) == 13)

def add_Object() -> dict:
    rez: dict = {}
    addData = json.dumps(
        { 
            "name": "Apple ноутбук", 
            "data": { "color": "синий", "generation": "крутой", "price": 135 }
        }
    )
    headers = {"content-type": "application/json"}
    r: requests.models.Response = requests.post(url2, data=addData, headers=headers)
    if r.status_code == 200:
        rez = json.loads(r.text)
    return rez

# Проверим возможность добавления объекта
def test_add_Object() -> None:
    d: dict = add_Object()
    assert(d['name'] == 'Apple ноутбук')
    assert(d['data']['color'] == 'синий')


