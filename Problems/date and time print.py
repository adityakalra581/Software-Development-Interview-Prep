import datetime
today=datetime.datetime.now()
print(today)

print()

print(str(today))
# str() has no difference than the previous one.
# str() displays today’s date in a way that the user can understand the date and time.

#repr() prints “official” representation of a date-time object (means using
#the “official” string representation we can reconstruct the object).

print()
print(repr(today))
