kub_list = []
summary_list = 0
summary_list_seventeen = 0

for i in range(1, 1000, 2):
    kub_list.append(i**3)

for i in kub_list:
    num = i
    s_num = 0
    while i > 0:
        digit = i % 10
        s_num = s_num + digit
        i = i // 10

    if s_num % 7 == 0:
        summary_list += num



print(summary_list)

for i in kub_list:
    num = i
    i += 17
    s_num = 0
    while i > 0:
        digit = i % 10
        s_num = s_num + digit
        i = i // 10

    if s_num % 7 == 0:
        summary_list_seventeen += num + 17

print(summary_list_seventeen)

