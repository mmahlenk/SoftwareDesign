"""Chapter 16: Exercise 16.7 of ThinkPython

Author: Marisa Mahlenkamp
"""

import datetime
import string 


def get_date():
    today = datetime.date.today()
    week = datetime.date.weekday(today)

    if week == 0:
        week_day = 'Monday'
    if week == 1: 
        week_day = 'Tuesday'
    if week == 2:
        week_day = 'Wednesday'
    if week == 3:
        week_day = 'Thursday'
    if week == 4:
        week_day = 'Friday'
    if week == 5:
        week_day = 'Saturday'
    if week == 6:
        week_day = 'Sunday'

    print today, week_day


def birthday_countdown(year, month, day):
    """Function that computes an individuals age and the number of days,
    hours, minutes and seconds until their next birthday. 

    year: integer
    month: integer
    day: integer
    """

    now = datetime.datetime.now()
    birth = datetime.datetime(year, month, day)

    age = str((now.date() - birth.date()) / 365)
    years = age.split(' d')[0]
    print 'You are %s years old' % years

    # TODO: figure out variable for year
    countdown = datetime.datetime(2013, month, day, 0, 0) - now
    total_seconds = countdown.total_seconds()
    if (total_seconds <0):
        countdown = datetime.datetime(2014, month, day, 0, 0) - now
    print 'Until your next birthday:', countdown

def double_day(bday1, bday2):
    if bday2 > bday1:
        diff = bday2 - bday1
        ans = bday2 + diff
        return ans
    else:
        diff = bday1 - bday2
        ans = bday1 + diff
        return ans

def n_times_older(bday1, bday2, n):
    if bday2 > bday1: 
        diff = bday2 - bday1
        ans = bday2 + (diff / (n-1))
        return ans
    else:
        diff = bday1 - bday2
        ans = bday1 + (diff / (n-1))
        return ans 



if __name__ == '__main__':

    get_date()
    birthday_countdown(1992, 10, 12)

    bday1 = datetime.datetime(1992, 5, 17)
    bday2 = datetime.datetime(1992, 5, 5)
    print double_day(bday1, bday2)
    
    print n_times_older(bday1, bday2, 2)













