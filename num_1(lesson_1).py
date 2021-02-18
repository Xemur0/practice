duration = int(input("Введите промежуток времени в секундах: "))

if duration < 60:
    print(duration, "sec")

elif duration >= 60 and duration <= 3599:
    min = duration // 60
    sec = duration - (min * 60)
    print(min, 'min', sec, 'sec')

elif duration >= 3600 and duration <= 86399:
    hour = duration // 3600
    min = duration // 60
    sec = duration - (min * 60)
    if hour >= 1:
        min = min - (hour * 60)
        print(hour, 'hour', min, 'min', sec, 'sec')

elif duration >= 86400 and duration <= 2629743:
    day = duration // 86400
    hour = duration // 3600
    min = duration // 60
    sec = duration - (min * 60)
    if hour >= 24:
        min = min - (hour * 60)
        hour = hour - (day * 24)
        print(day, 'day', hour, 'hour', min, 'min', sec, 'sec')

