import re

RE_EMAIL = re.compile(r'[a-z\w\d]+@[a-z]+\.[a-z]+|[а-яЁ\w\d]+@[а-яЁ]+\.[а-яЁ]+|[а-яЁ\w\d]+@[a-z]+\.[a-z]+'
                      r'|[а-яЁ\w\d]+@[а-яЁ]+\.[a-z]+|[а-яЁ\w\d]+@[a-z]+\.[а-яЁ]+', re.IGNORECASE)

def valid_email(name=input('Введите Email: ')):
    if bool(RE_EMAIL.findall(name)) == True:
        a = name.split('@')
        result = {'username':a[0], 'domain': a[1]}
    else:
        raise ValueError(f'Uncorrect email {name}')
    return result


print(valid_email())
