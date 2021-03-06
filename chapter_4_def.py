def search4vowels(phrase: str) -> set:
    """
    аннотация (начиная с Python 3)
    phrase:str - ожидаемый тип, -> set - возврат множества
    Выводит гласные, найденные в указанном слове
    """
    vowels = set('aeiouy')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiouy') -> set:
    """
    возвращает множество букв из 'letters', найденных в указанной фразе
    """
    return set(letters).intersection(set(phrase))


search4vowels('millenium')
search4letters('galaxy', 'life')


# аргументы передаются в функцию по значению
def double(arg):
    print('Before: ', arg)
    arg *= 2
    print('After:' , arg)


# аргументы передаются в функцию по ссылке
def change(arg: list):
    print('Before: ', arg)
    arg.append('More date')
    print('After: ', arg)

"""
Переменные в Python  — это ссылки на объекты. Значение, хранимое в переменной,
— это адрес объекта в памяти. И в функцию передается адрес, а не фактическое значение. 
Функции в Python поддерживают семантику вызова с передачей аргументов по ссылкам на объекты.
В зависимости от типа объекта, на который ссылается переменная, семантика вызова функции
может различаться. Интерпретатор определяет типы объектов, на которые ссылается переменная
(адрес в памяти). 
Если переменная ссылается на изменяемое значение, применяется семантика передачи
аргумента по ссылке. 
Если тип данных, на который ссылается переменная, неизменяемый, происходит передача
аргумента по значению. 
Списки, словари и множества (будучи изменяемыми) всегда передаются в функцию по ссылке —
изменения, внесенные в них внутри функции, отражаются в вызывающем коде.
Строки, целые числа и кортежи (будучи неизменяемыми) всегда передаются в функцию 
по значению — изменения, внесенные в них внутри функции, не отражаются в вызывающем коде. 
Если тип данных неизменяемый, то функция не может его изменить.
"""