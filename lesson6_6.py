from sys import argv

with open('bakery.csv', 'a', encoding='utf-8') as a:
    with open('bakery.csv', 'r', encoding='utf-8') as b:
        if len(argv) == 1:
            print(b.read())
        elif len(argv) == 2:
            if ',' in argv[1]:
                b.read()
                print(argv[1], file=a)
            else:
                print(*b.readlines()[int(argv[1]) - 1:], sep='')
        else:
            print(*b.read().split()[int(argv[1]): int(argv[2]) + 1], sep='\n')