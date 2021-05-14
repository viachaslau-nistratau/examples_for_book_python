def search4vowels(phrase: str) -> set:
    """
    аннотация (начиная с Python 3)
    phrase:str - ожидаемый тип, -> set - возврат множества
    Выводит гласные, найденные в указанном слове
    """
    vowels = set('aeioyu')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str) -> set:
    """
    возвращает множество букв из 'letters', найденных в указанной фразе
    """
    return set(letters).intersection(set(phrase))


search4vowels('millenium')
search4letters('galaxy', 'life')


def double(arg):
    print('Before: ', arg)
    arg *= 2
    print('After:' , arg)


def change(arg: list):
    print('Before: ', arg)
    arg.append('More date')
    print('After: ', arg)