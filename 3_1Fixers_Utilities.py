#---------------------------- Program to Demonstrate Fixers utilities -------------------
import string
import datetime as dt

# 1. Remove leading or trailing spaces
baddata = " Hello My name is abc xyz "
cleandata = baddata.strip()
print(f"Original: '{baddata}' -> Cleaned: '{cleandata}'")

print("********************************************************")

# 2. Remove nonprintable characters
baddata = "Data\x00Science with\x02 funny characters is \x10bad!!!"
cleandata = ''.join(filter(lambda x: x in string.printable, baddata))
print(f"Bad Data: '{baddata}' -> Clean Data: '{cleandata}'")

print("********************************************************")

# 3. Reformat date from YYYY-MM-DD to DD Month YYYY
baddate = dt.date(2001, 1, 1)
gooddata = dt.datetime.strptime(str(baddate), '%Y-%m-%d').strftime('%d %B %Y')
print(f"Bad Date: {baddate} -> Good Date: {gooddata}")
