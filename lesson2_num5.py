# 5

prices = [60.60, 23.07, 99.99, 56.25, 3000.76, 55.06, 234.50, 87.23, 20, 5, 1.20]
print(id(prices))
for i in prices:
    a = str(i).split('.')
    if len(a) == 1:
        print(f'{a[0]} руб 00 коп', end=", ")
    elif len(a[1]) > 1:
        print(f'{a[0]} руб {a[1]} коп', end=", ")
    else:
        b = int(a[1]) * 10
        print(f'{a[0]} руб {b} коп', end=", ")

print('\n')
prices.sort()
for i in prices:
    a = str(i).split('.')
    if len(a) == 1:
        print(f'{a[0]} руб 00 коп', end=", ")
    elif len(a[1]) > 1:
        print(f'{a[0]} руб {a[1]} коп', end=", ")
    else:
        b = int(a[1]) * 10
        print(f'{a[0]} руб {b} коп', end=", ")

print('\n')
print(id(prices))
print('\n')
new_prices = sorted(prices, reverse=True)
print(new_prices)
print('\n')

best = prices[-5::]
for i in best:
    a = str(i).split('.')
    if len(a) == 1:
        print(f'{a[0]} руб 00 коп', end=", ")
    elif len(a[1]) > 1:
        print(f'{a[0]} руб {a[1]} коп', end=", ")
    else:
        b = int(a[1]) * 10
        print(f'{a[0]} руб {b} коп', end=", ")
