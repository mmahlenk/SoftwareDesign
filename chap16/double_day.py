"""Chapter 16: Exercise 16.7 of ThinkPython

Author: Marisa Mahlenkamp
"""

from datetime import *
import string 


def get_date():
    today = date.today()
    week = date.weekday(today)

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

    now = datetime.now()
    birth = datetime(year, month, day)

    age = str((now.date() - birth.date()) / 365)
    years = age.split(' d')[0]
    print 'You are %s years old' % years

    # TODO: figure out variable for year
    countdown = datetime(2013, month, day, 0, 0) - now
    print 'Until your next birthday:', countdown

def double_day():
    print 'Hi'


if __name__ == '__main__':
    # get_date()
    birthday_countdown(1992, 11, 6)