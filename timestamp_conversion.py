from datetime import datetime,timedelta
import time

current_timestamp = time.time()
print "Timestamp: ", current_timestamp

datetime_ts = datetime.fromtimestamp(current_timestamp).strftime('%Y-%m-%d %H:%M:%S')
print "Timestamp to datetime: ", datetime_ts

date_ts = datetime.fromtimestamp(current_timestamp).strftime('%Y-%m-%d')
print "Timestamp to date: ", date_ts

#timestamp to datetime object in UTC
date_utc = datetime.utcfromtimestamp(current_timestamp)
print "Timestamp in UTC: ", date_tc
  