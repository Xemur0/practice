
import json
with open('users.csv', 'r', encoding='utf-8') as users:
    result = {}
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:

        for line in users:
            if hobby.readline() == '':
                result.update({line.replace(',', ' ').strip(): None})
            else:
                result.update({line.replace(',', ' ').strip(): hobby.readline().strip()})
        print(result)
        with open('result.json', 'w', encoding='utf-8') as f:
            for i, key in result.items():
                if key == None:
                    exit(1)
            else:
                json.dump(result, f, indent=10, ensure_ascii=False)


