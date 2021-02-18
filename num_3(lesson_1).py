

percent = ["процент", "процента", "процентов"]

num = int(input('Введите  число: '))
while True:
    if num < 0:
        num = int(input("Введите число от 0 до 20: "))
    else:
        break

if num == 0:
    print(num, percent[2])
elif num == 1:
    print(num, percent[0])
elif num >= 2 and num < 5:
    print(num, percent[1])
elif num >=5 and num <= 20:
    print(num, percent[2])



for i in range(0, 21):
    if i == 1:
        print(i, percent[0])
    elif i >= 2 and i < 5:
        print(i, percent[1])
    elif i >= 5 and i <= 20:
        print(i, percent[2])

