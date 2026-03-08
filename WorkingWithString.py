#string
print("It's alright")
print("He is called 'Akbar'")
print('He is called "Akbar"')

#Assign String to Variable
a = "Hello"
print(a)

#multilinestrings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#strings are arays
a = "Hello, World!"
print(a[1])

#Looping Through a String
for x in "banana":
  print(x)

#String Length
a = "Hello, World!"
print(len(a))

#check string 
txt = "The best things in life are free!"
print("best" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")