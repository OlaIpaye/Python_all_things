from datetime import datetime

# the datetime object keeps track of my birthday
birthday = datetime(1994, 2, 8, 6, 35, 12)

print(birthday)

print(birthday.year) # getting the year of my birthday

print(birthday.weekday()) # getting the week day of my birthday

print(birthday.now()) # getting the date for the present time

print(f"It's been {datetime.now() - datetime(2025, 2, 8)} since my birthday!") # using datetime module to get time difference

parse_date = datetime.strptime("Feb 8, 2025", "%b %d, %Y")
print(parse_date.year)
print(parse_date.month)
print(parse_date.day)

