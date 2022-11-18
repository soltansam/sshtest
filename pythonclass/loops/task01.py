print('Give a number and see the multiplication result')
entry = int(input('Enter a number: > '))
for i in list(range(11)):
    print('{} X {} = '.format(entry, i), (entry*i))
    