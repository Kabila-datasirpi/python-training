import datetime
time=datetime.datetime.now()        #returns the current date and time
print(time)

month=datetime.datetime(2002,1,23)  #y/m/d oder
print(month.strftime("%B"))
print(month.strftime("%D"))