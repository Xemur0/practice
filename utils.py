
from datetime import datetime
from requests import get, utils


response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

def currency_rates():
    valuta = input('Введите требуемую валюту: ').upper()
    for i in content:
        i = content[content.find(valuta):(content.find(valuta) + 3)]
        if i != valuta or len(i) < 3:
            return None
        else:
            curency = (content[content.find(valuta):(content.find(valuta) + 3)])
            date = content[(content.find('Date') + 6):(content.find('Date') + 16)]
            a = content.find('Value', content.find(valuta))
            a1 = float((content[(a + 6):(a + 13)]).replace(',', '.'))
            date = date.split('.')
            date_1 = datetime(year=int(date[2]), month=int(date[0]), day=int(date[1])).date()
            return f'{a1}, {date_1}'

if __name__ == "__main__":
    print("it's a file")
else:
    print("I's a module")
