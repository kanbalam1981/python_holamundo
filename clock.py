import time
import datetime as datetime 
import calendar
print(time.time())
print(time.localtime())

print (calendar.month(2025, 1))
hoy = datetime.date.today()
hora_actual = time.localtime()
ahora = datetime.datetime.now()
print(ahora.hour, ahora.minute, ahora.second)  
print(hora_actual)
print(hoy)