import datetime
from dateutil.parser import parse

#pulls up today's date
today = datetime.date.today()
#uses today's date to capture the year
thisYear = today.strftime("%Y")
#need the end of the year for this year and last year to get the total days within the year -- this helps with leap years
yearEnd = f'Dec 31, {thisYear}'
lastyearEnd = f'Dec 31, {int(thisYear)-1}'
delta = parse(yearEnd) - parse(lastyearEnd) #this prints a datetime format. used '.days' to get just the number
#shows current day in the year and then calculates the remaining days in the year
daysin = today.strftime("%j")
remaining = abs(int(daysin) - int(delta.days)) #does not include TODAY!! because 'daysin' has TODAY included

# debug
# print(delta)
# print(f'{delta.days}')
# print(f'Today {today} -- this Year {thisYear} -- End of the year {yearEnd} -- days in {daysin} -- days remaining {remaining}')

def daysRemaining(num):
    total = num / remaining
    return round(total,2)

#print(daysRemaining(300))