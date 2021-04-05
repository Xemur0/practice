import time
class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date(cls, date):
        a = date.split('-')
        return (int(i) for i in a)
    @staticmethod
    def validate_date():
        try:
            date = input('Input date format: "dd-mm-yyyy":')
            valid = time.strptime(date, '%d-%m-%Y')
            print(date)
        except:
            print('Wrong date, try again')

a = Data.get_date('20-20-21')
print(*a)
Data.validate_date()