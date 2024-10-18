import time
# While Loop : a statement that will excute it's block of code, as logn as its condtion remains true

#  for loop : a statement that will execute its block of code a limited amount of times

# while loop = unlimited
# for loop = limited

#  Loop control statements = change a loops execution from its normal sequence
#  1) break = used to terminate the loop entirely 2) continue = skips to the next iteration of the loop 3) pass does nothing acts as a placeholder


# name = ""

# while len(name) == 0:
#   name = input("enter your name:")

# print("hello " +name)


# for i in range(10):
  # print(i)

# for i in range(50,100+1, 2):
#   print(i)
  
# for i in "Rutuja":
#   print(i)

# for seconds in range(10,0,-1):
#   print(seconds)
#   time.sleep(1)
# print("happy new year")

#  nested Loops = the inner loop will finish all  of its iterations before finishing one iteration of the outer loop

# rows = int(input("how many rows?: "))
# col = int(input("how many cloumns?: "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#   for j in range(col):
#     print(symbol, end="")
#   print()


# break continue pass
# while True:
#   name = input("Enter your name: ")
#   if name != "":
#     print("you name is: " +name)
#     break


phone_number = "123-456-7890"

for i in phone_number:
  if i  == "-":
    continue
  print(i, end ="")
  
for i in range(1,21):
  if  i == 13:
    pass
  else :
    print(i)