# Imports the datetime module.
# This is different to 'from datetime import *', which imports all PUBLIC NAMES from the module directly into the current namespace.
import datetime

# Calling the today() method of the datetime class, and assigning the resulting datetime object to the variable called 'today'.
today = datetime.datetime.today()   # module.class.method()
print("Today is:", today)

# Loop through several attributes of the datetime object.
# getattr(object, attribute_name, default)
for attr in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print(attr, ':\t', getattr(today, attr))

# Access the attributes directly, and format parts of the date.
print("Time:", today.hour, ":", today.minute)
day = today.strftime("%A")      # Full day name, e.g. Monday
month = today.strftime("%B")    # Full month name, e.g. October
print("Date:", day, month, today.day)