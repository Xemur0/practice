from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n):
    '''
    Функция возвращает n шуток, сформированных из трех случайных слов, взятые из трех списков
    :param n: количество требуемых
    :return: возвращает список с шутками
    '''
    list = []
    a = 1
    while a <= n:
        list.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        a += 1
    return list
print(get_jokes(1)




def get_jokes_repeat(n, i=True):
    '''
    Функция возвращает n шуток, сформированных из трех случайных слов, взятые из трех списков
    :param n: количество требуемых
    :param i: по умолчанию повторы слов включены, false - без повторов слов
    :return: возвращает список с шутками
    '''
    noun, adverb, adject = nouns.copy(), adverbs.copy(), adjectives.copy()
    finish_list = []
    list_min = min(noun, adverb, adject)

    while n and len(list_min):
        num = randrange(len(list_min))
        if i:
            finish_list.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        else:
            finish_list.append(f"{noun.pop(num)} {adverb.pop(num)} {adject.pop(num)}")
        n -= 1

    return finish_list

print(get_jokes_repeat(5, False))

