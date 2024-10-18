#  index opratos [] = gives access to a sequence's element (str, list, tuple)

name = "bro CODE!"

if (name[0].islower()):
  name = name.capitalize()

first_name = name [:3].upper()
last_name = name[4:].lower()
last_char = name [-2]
print(last_char)
print(last_name)
print(first_name)