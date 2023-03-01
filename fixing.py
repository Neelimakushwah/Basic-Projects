import os
import datetime
import time

n=1
c,b,a=input("Enter the Date = ").split("/")
hr, minn , sec =input("Enter the Time =").split( ":" )
shedule_date =datetime.date(int(a),int(b),int(c))
while n>0:
    if time.localtime().tm_hour==int(hr) and time.localtime().tm_min==int(minn) and time.localtime().tm_sec==int(sec) and datetime.date.today()==shedule_date:
        os.startfile(r"C:\Users\HP\Downloads\Alarm-Windows-10.mp3")
        print("Alarm Ringing......")
        break
else:
    n+=1