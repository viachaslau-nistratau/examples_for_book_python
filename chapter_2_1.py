# EXAMPLE 1
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))
new_phrase = ''.join(plist)
print(new_phrase)
print(plist)

# EXAMPLE 2
phrase_two = "Don't panic!!"
plist_two = list(phrase_two)
print(phrase_two)
print(plist_two)
new_phrase = ''.join(plist_two[1:3])
new_phrase = new_phrase + ''.join(
    [plist_two[5],plist_two[4], plist_two[7], plist_two[6]])
print(new_phrase)
print(plist_two)

# EXAMPLE 3
paranoid_android = 'Marvin, the Paranoid Android'
letters = list(paranoid_android)
for char in letters[:6]:
    print('\t', char)
print()
for char in letters[-7:]:
    print('\t'*2, char)  # вставка 2 символов табуляции
print()
for char in letters[12:20]:
    print('\t'*3, char)
