#Задание 2, 3
list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

some_list = []

for ind, i in enumerate(list):
    if i in some_list:
        continue
    if i.isdigit():
        list.remove(i)
        string = f'{int(i):02}'
        list.insert(ind, string)
        list.insert(ind,'"')
        list.insert(ind + 2, '"')
        some_list.append(string)

    if i.startswith('+'):
        list.remove(i)
        b = f'+{int(i):02}'
        list.insert(ind, b)
        list.insert(ind, '"')
        list.insert(ind + 2, '"')
        some_list.append(b)

    elif i.startswith('-'):
        list.remove(i)
        b = f'-{abs(int(i)):02}'
        list.insert(ind, b)
        list.insert(ind, '"')
        list.insert(ind + 2, '"')
        some_list.append(b)

print(list)
for i in list:
    if i == '"':
        continue
    elif not i.isdigit() and i.startswith('+'):
        print(f'"{i}" ', end='')
    elif not i.isdigit() and i.startswith('-'):
        print(f'"{i}" ', end='')
    elif not i.isdigit():
        print(f'{i} ', end='')
    elif i != '"' and i.isdigit():
        print(f'"{i}"', end=' ')