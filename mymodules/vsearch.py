def search4vowels(phrase: str) -> set:
    """
    Выводит гласные, найденные в указанном слове
    """
    vowels = set('aeiouy')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiouy') -> set:
    """
    возвращает множество букв из 'letters', найденных в указанной фразе
    """
    return set(letters).intersection(set(phrase))