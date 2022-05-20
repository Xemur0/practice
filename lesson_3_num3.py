def thesaurus(*args):
    names = {name.title() for name in args} # сделали вид с большой буквы
    first_sign = [name[0] for name in names] #взяли первую букву от имени
    result = {a: list() for a in first_sign} #делаем словарь и генерируем где ключ первая буква, значение список

    for name in names:
        result[name[0]].append(name)

    return result

print(thesaurus('Иван', 'мария', 'Петр', 'Илья', 'Ilich'))





