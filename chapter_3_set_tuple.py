vovels = {'a', 'e', 'i', 'o', 'u', 'y'}
word = input('Введите слово - ')
found = vovels.intersection(set(word))
for vovel in found:
    print(vovel)

u = vovels.union(set(word))  # объединение множеств
d = vovels.difference(set(word))  # разница между vovels и word
i = vovels.intersection(set(word))  # пересечение объектов двух множеств

vowels = ('a', 'e', 'i', 'o', 'u', 'y')  # type = tuple
vowels2 = ('a',)  # кортеж с одним объектом