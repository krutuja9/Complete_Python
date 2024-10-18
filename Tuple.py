#  Tuple = collection which is ordered and unchangeable used to group toghether related data

student = ("bro", 21, "male")

print(student.count("bro"))
print(student.index("male"))

for i in student:
  print(i)
  
if "Bro" in student :
  print("bro is here")