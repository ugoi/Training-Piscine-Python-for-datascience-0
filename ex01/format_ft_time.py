# This script displays the current timestamp in seconds since January 1, 1970, 
# both in standard and scientific notation. It also prints the current date in the format "Month Day Year".

from datetime import datetime

today = datetime.now()

print(f"Seconds since January 1, 1970: {today.timestamp():,.4f} or {today.timestamp():.2e} in scientific notation")
print(today.strftime("%b %d %Y"))
