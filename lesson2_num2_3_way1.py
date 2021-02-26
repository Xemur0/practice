#Задание 2, 3
list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

some_list = []

for ind, i in enumerate(list):
    if i in some_list:
        continue
    if i.isdigit():
        list.remove(i)
        string = f'"{int(i):02}"'
        list.insert(ind, string)
        some_list.append(string)

    if i.startswith('+'):
        list.remove(i)
        b = f'"+{int(i):02}"'
        list.insert(ind, b)
        some_list.append(b)

    elif i.startswith('-'):
        list.remove(i)
        b = f'"-{abs(int(i)):02}"'
        list.insert(ind, b)
        some_list.append(b)

print(list)
print(' '.join(list))