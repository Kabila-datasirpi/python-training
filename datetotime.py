#string to date
import datetime
strdate="2023-12-23"
objdate=datetime.datetime.strptime(strdate,"%Y-%m-%d")
print(objdate)


#date to string
strobj=datetime.datetime(year=2023,month=12,day=23)
strdatee=strobj.strftime("%y-%m-%d")
print(strdatee)


