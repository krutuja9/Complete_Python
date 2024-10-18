#  Slicing = create a substring by extracting elements from another string
#  indexing[]  or slice () ... [start: end: step]

name = "rutuja Kokate"
first_name = name[:6]
last_name = name[7:]
funky_name = name[::3]
reversed_name = name[::-1]
# print(reversed_name)
# print(funky_name)
# print(first_name)
# print(last_name)

website = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)
print(website[slice])
print(website2[slice])