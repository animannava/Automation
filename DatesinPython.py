import datetime
import decimal
from time import strftime

print(datetime.date.today())
print(datetime.datetime.now().strftime("%A, %B %d, %Y"))
x=datetime.datetime(2025,2,22)
y=datetime.datetime(2,4,22)
print(x.strftime("%w"))
print(y.strftime("%B"))
