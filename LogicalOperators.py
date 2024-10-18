# Logical operators (and, or) = used to check if two or more coditional statements is true

temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp<=30):
  print("the temperature is good today!")
  print("You can go outside")
  
elif not(temp < 0 or temp > 30):
  print("THE temperature is bad today \nStay inside")