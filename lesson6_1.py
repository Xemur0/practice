with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
        for i in file_1:
            line = i.split()
            result = line[0], line[5].replace('"', ''), line[6]
            print(result)


