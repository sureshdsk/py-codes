from datetime import datetime
from pytz import timezone

# Current time 
print datetime.now()

# Current time to UTC
now_utc = datetime.now(timezone('UTC'))
print now_utc.strftime("%Y-%m-%d %H:%M:%S %Z%z")

# Convert to US/Eastern time zone
now_useastern = now_utc.astimezone(timezone('US/Eastern'))
print now_useastern.strftime("%Y-%m-%d %H:%M:%S %Z%z")

# Convert to Asia/Kolkata time zone
now_india = now_useastern.astimezone(timezone('Asia/Kolkata'))
print now_india.strftime("%Y-%m-%d %H:%M:%S %Z%z")

  