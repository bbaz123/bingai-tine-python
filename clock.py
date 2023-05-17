# Import datetime and pytz modules
import datetime
import pytz

# Create a timezone object for Shanghai
shanghai_tz = pytz.timezone("Asia/Shanghai")

# Get the current datetime in Shanghai
shanghai_dt = datetime.datetime.now(shanghai_tz)

# Format the datetime as HH:MM:SS
shanghai_time = shanghai_dt.strftime("%H:%M:%S")

# Print the time
print("The current time in Shanghai is:", shanghai_time)
