# from datetime import date

from datetime import date

#write your code here...
from datetime import datetime

# Read input dates
date1 = input().strip()
date2 = input().strip()

# Convert string to date objects
d1 = datetime.strptime(date1, "%Y-%m-%d")
d2 = datetime.strptime(date2, "%Y-%m-%d")

# Calculate difference
difference = d2 - d1

# Print number of days
print(difference.days)
