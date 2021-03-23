from functools import wraps

def type_logger(func):
    @wraps(func)
    def tag_wrapper(*args, **kwargs):
        list2 = [i for i in (*args, *kwargs.values())]
        print(*(f'{func.__name__}({i}: {type(i)})' for i in list2), *func(*args, **kwargs), sep=',\n')

    return tag_wrapper

@type_logger
def calc_cube(*args, **kwargs):
    list1 = []
    for i in (*args, *kwargs.values()):
        if isinstance(i, int) or isinstance(i, float):
            list1.append(i)
    return [i ** 3 for i in list1]

calc_cube(5, 6, 7, 8, 'dsadsa', x=9)