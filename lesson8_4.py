def val_checker(lambd_func):
    def checker(func):
        def wrapper(num):
            if lambd_func(num):
                print(func(num))
            else:
                raise ValueError(f'err val {num}')
        return wrapper
    return checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

try:
    calc_cube(5)
except ValueError as err:
    print(err)
