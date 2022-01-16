#--------------------------------------Document Info Starts------------------------------------------------#
# Project Number:01
# Code by: PAVAN SG
# Task Number:01
# Created Date  : 16-01-2002
# Modified Date : 16-01-2002
# git url:
#--------------------------------------Document Info Ends---------------------------------------------------#
#To Calculate the number of days in between the given date
#-------------------------------------Function Starts-------------------------------------------------------#
from datetime import datetime
today=datetime.today()
#strftime this means it is string formatter ,this will format a datetime to string format
print(f"Today's date is {today.strftime('%d/%m/%Y')}")
d_1='20/12/2021'
d_2=today.strftime('%d/%m/%Y')
d_format='%d/%m/%Y' 
#striptime this is string parsser this will convert string format to datetime
p_1=datetime.strptime(d_1,d_format)
p_2=datetime.strptime(d_2,d_format)
difference=p_2-p_1
print(f"No of dates between the given dates is :{difference.days}")



