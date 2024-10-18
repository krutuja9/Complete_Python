# Dictionary : A changeable, unordered collection of unique key: value pairs fast becz they use hashing , allow us to access a value quickly


capitals = {"USA": "Washington DC",
            'India': "New Dehli",
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({"Germany": "Berlin",})
capitals.update({"USA": "Las Vegas",})
capitals.pop('China')
capitals.clear()

# print(capitals['China'])
# print(capitals.get('germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key , value in capitals.items():
  print(f"{key}: {value}")