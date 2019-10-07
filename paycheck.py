from datetime import datetime, timedelta
from callDate import daysRemaining
import time 


class Paycheck(object):
    def __init__(self, amount, date, details):
        self.amount = amount
        self.date = date.strftime("%B %d, %Y at %I:%M %p")
        self.details = details
        self.special = self.amount * .08

    def printPaycheck(self):
        print(f'Paycheck on {self.date} in the amount of ${self.amount} --(details)-- {self.details} ')
    
    def getAmount(self):
        total = daysRemaining(self.special)
        return total 
    #FIX THIS PROBLEM! getAmount (extra money collected because of the rounding up)


one_day = timedelta(days=1)
date = datetime.now()
#date = datetime.datetime.now().strftime("%y-%m-%d %H:%M")
paycheck1 = Paycheck(1000, date, 'First Paycheck!' )
paycheck2 = Paycheck(2000, date + one_day, 'Second Paycheck' )

print(paycheck1.printPaycheck())
print(paycheck2.printPaycheck())

special = dict(paycheck1=paycheck1.getAmount(), paycheck2=paycheck2.getAmount())
print(special)


