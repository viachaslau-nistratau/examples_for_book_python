""" Форматы выводв"""
price = 49.99
tag = 'is a real bargain!'

msg = 'At ' + str(price) + ', Head First Python ' + tag

msg_1 = 'At %2.2f, Head First Python %s' % (price, tag)

msg_2 = 'At {}, Head First Python {}' .format(price, tag)

""" Сортировка"""
product = {'Book': 49.99,
           'Pdf': 43.99,
           'Video': 199.99
           }
for k in product:
    print(k, '->', product[k]) # вывод словаря на экран

for k in sorted(product):
    print(k, '->', product[k]) # сортирует словарь по ключам

for k in sorted(product, key=product.get):
    print(k, '->', product[k])            # сортирует словарь по значениям

for k in sorted(product, key=product.get, reverse=True):
    print(k, '->', product[k])            # меняется порядок сортировки

""" ООП"""
@staticmethod
"""
декоратор, позволяющий создать статическую функцию внутри класса
(без первого аргумента self)
"""
@classmethod
"""
декоратор, позволяющий создать метод класса, принимающий в первом 
параметре(как правило с именем cls) сам класс вместо ссылки self на объект 
"""
@property
"""
декоратор, позволяющий определять и использовать метод, как если бы он был атрибутом
"""
__slots__
"""
дирректива класса может (при использовании) значительно повысить эффективность 
использования памяти объектами, созданными из класса (за счет некоторой потери гибкости)
"""

""" Libraries """
collections
"""
Этот модуль реализует структуры данных в дополнение к встроенным
спискам, кортежам, словарям и множествам. В нем вы найдете много
интересного. Вот краткий список того, что есть в collections.
• OrderedDict: словарь, сохраняющий порядок вставки элементов.
• Counter: класс, с помощью которого легко можно посчитать, что угодно.
• ChainMap: позволяет представить группу словарей как одно целое.
"""

