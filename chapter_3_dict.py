import pprint

person = {'Name': 'Ford Prefect',
          'Gender': 'Male',
          'Occupation': 'Researcher',
          'Home Planet': 'Betelgeuse Seven'}

vovels = ['a', 'e', 'i', 'o', 'u', 'y']
word = input('Введите слово - ')
found = {}

# found['a'] = 0
# found['e'] = 0
# found['i'] = 0
# found['o'] = 0
# found['u'] = 0
# found['y'] = 0

for letter in word:
    if letter in vovels:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')


people = {}
people['Ford'] = {'Name': 'Ford Prefect',
                  'Gender': 'Male',
                  'Occupation': 'Researcher',
                  'Home Planet': 'Betelgeuse Seven'
                  }
people['Arthur'] = {'Name': 'Arthur Dent',
                  'Gender': 'Male',
                  'Occupation': 'Paranoid Android',
                  'Home Planet': 'Unknown'
                  }
pprint.pprint(people)  # более удобочитаемый вывод словаря словарей

print(people['Arthur']['Occupation'])