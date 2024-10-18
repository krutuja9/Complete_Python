#  if statement =  a block of code that will excute if its coditioon is true

age = int(input ("How old are you?: "))

if age >= 18:
  print("You are an adult")
  if age == 100:
    print("You are a century old!")
  
elif age < 0:
  print("You are in gods house")
else:
  print("You are a child!")