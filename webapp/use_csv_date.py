import csv

with open('bussers.csv') as data:
    for line in csv.reader(data):
        print(line)
"""
csv.reader превращает строки из файла в списки из двух элементов
"""


with open('bussers.csv') as data:
    for line in csv.DictReader(data):
        print(line)

"""
DictReader трансформирует данные из CSV-файла в коллекцию словарей
"""

import pprint

with open('bussers.csv') as data:
    ignore = data.readline()  # игнорируем заголовок
    flights = {}
    for line in data:
        """
        split разбивает исходную строку на две и возвращает список строк
        strip удаляет пробельные символы в начале и в конце строки
        """
        k, v = line.strip().split(',')
        flights[k] = v
    pprint.pprint(flights)

from datetime import datetime

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')
"""
получая время в 24-часовом формате (в виде строки), данная цепочка методов
преобразует его в строку в 12-часовом фоомате
"""

from datetime import datetime
import pprint

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('bussers.csv') as data:
    ignore = data.readline()  # игнорируем заголовок
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v
pprint.pprint(flights)
print()

    flights2 = {}

    for k, v in flights.items():
        """
        в каждой итерации ключ (к) преобразуется в 12-часовой формат, а затем
        используется в качестве ключа в новом словаре
        """
        flights2[convert2ampm(k)] = v.title()
        """"
        значение (v) преобразуется в регистр заголовка,
        а затем присваивается преобразованному ключу
        """
    pprint.pprint(flights2)


    flight_times = []
    for ft in flights.keys():
        flight_times.append(convert2ampm(ft))

    destinations = []
    for dest in flights.values():
        destinations.append(dest.title())

    more_dests = [dest.title() for dest in flights.values()] # генератор списка

    fts2 = [convert2ampm(ft) for ft in flights.keys()]

    more_flights = {convert2ampm(ft): v.title() for k, v in flights.items()}

    more_flights = {convert2ampm(k): v.title()
                    for k, v in flights.items()
                    if v = 'FREEPORT'
                    }
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    evens = []
    for num in data:
        if not num % 2:
            evens.append(num)

    evens = [num for num in data if not num % 2]

    data = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
    words = []
    for num in data:
        if isinstance(num, str):
            words.append(num)

    words = [num for num in data if isinstance(num, str)]

    data = list('So long and thanks for all the fish'.split())
    title = []
    for word in data:
        title.append(word.title())

    title = [word.title() for word in data]

    dests = set(fts.values())  # уникальные пункты назначения

    when = {}
    for dests in set(fts.values()):
        when[dest] = [k for k, v in fts.items() if v == dest()])
    pprint.pprint(when)

    when2 = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}

    vowels = {'a', 'e', 'i', 'o', 'u'}
    message = "Don't forget to pack your towel."
    found = set()
    for v in vowels:
        if v in message:
            found.add(v)

    found_2 = {v for v in vowels if v in message}  # генератор множества


    for i in [x*3 for x in [1, 2, 3, 4, 5]]:
        print(i)
    """
    цикл for не начнет обработку данных, созданных генератором списков
    пока выполняется сам генератор
    """

    for i in (x*3 for x in [1, 2, 3, 4, 5]): # выражение-генератор
        print(i)
    """
    выражение-генератор возвращает данные по мере их создания
    """

import requests

    urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com')
    for resp in [requests.get(url) for url in urls]: # генератор списков (медленно)
        print(len(resp.content), '->', resp.status_code, '->', resp.url)

    for resp in (requests.get(url) for url in urls):  # выражение-генератор (по одному значению)
        print(len(resp.content), '->', resp.status_code, '->', resp.url)

    """
    функция gen_from_urls принимает одно значение (кортеж URL) 
    и возвращает кортеж результатов для каждого URL. 
    Возвращаемый кортеж содержит три значения - размер страницы, код HTTP 
    и URL, откуда пришел ответ
    """
import requests

from url_utils import gen_from_urls


    urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com')
    for resp_len, status, url in gen_from_urls(urls):
        """
        вызывается функция-генератор gen_from_urls(urls)
        интерпретатор переходит в эту функцию и начинает выполнять ее код
        """
        print(resp_len, status, url)

    def gen_from_urls(urls: tuple) -> tuple:
    """
    кортеж с адресами URL копируется в единственный аргумент функции, а затем
    начинает выполняться цикл for функции-генератора
    """
        for resp in (requests.get(url) for url in urls):
    """
    цикл for содержит выражение-генератор, которое извлекает первый URL из кортежа
    URLS и посылает запрос GET по указанному адресу. Когда приходит HTTP-ответ,
    выполняется инструкция yield
    """
            yield len(resp.content), '->', resp.status_code, '->', resp.url
    """
    вместо перехода к следующему URL в кортеже urls (то есть к следующей итерации
    в цикле for внутри gen_from_urls) yield передает три элемента данных вызывающему коду.
    Вместо завершения функция-генератор gen_from_urls приостанавливается.
    Когда данные (переданные инструкцией yield) поступают в вызывающий код, 
    выполняется тело цикла for. Тело содержит единственный вызов функции print.
    Он выполняется и на экране появляются результаты обработки первого URL.
    
    Затем цикл for в вызывающем коде начинает новую итерацию,
    функция  gen_from_urls возобновляет работу с того места, где она была приостановлена.
    Цикл for внутри gen_from_urls начинает новую итерацию, извлекает следующий URL 
    из кортежа urls, посылает запрос серверу, указанному в этом URL. Когда
    приходит HTTP-ответ, выполняется инструкция yield, возвращающая три элемента данных
    вызывающему коду (эти данные функция получает из объекта resp).
    
    Как и в прошлый раз вместо завершения функция-генератор gen_from_urls 
    снова приостанавливается.
    
    Когда данные (переданные инструкцией yield) поступают в вызывающий код, 
    снова выполняется функция print в теле цикла for, 
    выводя на экран второй результат
    
    Далее цикл for в вызывающем коде начинает следующую итерацию и вновь «вызывает»
    функцию gen_from_urls, возобновляя ее выполнение. Функция выполняет инструкцию
    yield, результаты возвращаются вызывающему коду и снова выводятся на экран.
    
    После обработки последнего URL в кортеже циклы for в функции-генераторе и вызывающем
    коде завершают свою работу.
    """

    urls_res = {url: size for size, _, url in gen_from_urls(urls)}
    """
    функция вызывается в генераторе словарей. Генератор словарей связывает URL 
    с размером загруженной страницы
    символ _ сообщает, что код состояния HTTP игнорируется
    """

