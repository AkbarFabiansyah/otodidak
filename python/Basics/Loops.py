#Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
print(fruits[1])

print("      ")

#Looping Through a String
for x in "banana":
  print(x)

print("      ")

#The break Statement
for x in fruits:
  print(x)
  if x == "banana":
    break
  
print("      ")

#The continue Statement
for x in fruits:
  if x == "banana":
    continue
  print(x)

print ("     ")

#range
for x in range(6):
  print(x)

for x in range(1,6):
  print (x)

print("    ")

#looping If Else
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
