
numbers = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def translate_num(a):
    for i in numbers.keys():
        if i == a:
            return numbers[i]
    return None
print(translate_num(input('Введите число на английском : ')))

#2

def translate_num_whatever(a):

    for i in numbers.keys():       #В задаче указано что только с большой буквы сделать, я сделал
        if i.lower() == a.lower(): # вне зависимости, начинается слово с большой буквы или нет
            return numbers[i].title()
    return None


print(translate_num_whatever(input('Введите число на английском языке: ')))