from datetime import datetime


date1 = datetime(2015,03,04)
date2 = datetime(2015,03,03)
date3 = datetime(2015,03,05)
date4 = datetime(2015,03,03)

print "Date 1: ",date1
print "Date 2: ",date2
print "Date 3: ",date3
print "Date 4: ",date4

if date1 < date3:
	print "date1 is greater than date3"

if date1 > date2:
	print "date1 is greater than date2"

if date2 == date4:
	print "date2 and date4 are equal"
  