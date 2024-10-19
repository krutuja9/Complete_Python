# find sum of all the even numbers up to 50

sum = 0
for i in range (1,51):
  if i%2 == 0:
    sum += i

# print(sum)

# write first 20 numbers and their squared numbers

# for i in range (1, 21):
#   print(f'{i} = {i*i}')

# first 10 odd numbers sum using while loop

# sum = 0
# n =0
# while  n <= 20:
#   if n %2 != 0:
#     sum += n
#   n += 1
# print(sum)


# check if a num is divisible by 8 and 12 to 100 numbers
# for i in range (1,100+1):
#   if i % 12 ==0  and i % 8 == 0:
#     print(i)


#  write a program to create a billing system  at supermarket
while True:
  name = input("Enter customer name: ")
  total = 0
  
  while True:
    print("enter the amount and quantity")
    amount = float(input("Enter amount"))
    quantity = float(input("Enter quantity"))
    total += amount * quantity
    repeat = input('do you want to add more items? (yes/no): ')
    if repeat == "no" or repeat == "No":
      break
  print("-"*40)
  print("Name:", name)
  print("Amount to be paid: ", total)
  print("-"*40)
  print("*****happy Shopping*****")
  
  repeat1 = input("do u want to go to next customer? (yes/ no: )")
  if repeat1 == 'no' or repeat == "No":
    break