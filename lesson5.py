#1

def nums_generator(max_num):
   for num in range(1, max_num + 1, 2):
       yield num

print(*nums_generator(15))

#2
def num_gen(n):
    a = [i for i in range(1, n+1, 2)]
    return a

print(*num_gen(15))

#3
from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Alex', 'Boris']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б']
human = zip_longest(tutors, klasses,  fillvalue=None)
human1 = (i for i in human)
print(*human1)
print(*human1) # при вводе этой команды, появляется пустая строка, что означает - генератор исчерпан



#4
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
a = [int(s) for s in src]
result = list((a[i] for i in range(1, len(a)) if a[i] > a[i-1]))
print(result)


#5
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = list((i for i in src if src.count(i) == 1))
print(result)


