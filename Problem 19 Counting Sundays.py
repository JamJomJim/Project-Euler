import datetime
from dateutil import relativedelta


def answer():
    numsundays = 0
    date = datetime.datetime(1901, 1, 1)

    while date.year < 2001:
        date += relativedelta.relativedelta(months=1)
        if date.weekday() == 6:
            numsundays += 1
    print(numsundays)


answer()
