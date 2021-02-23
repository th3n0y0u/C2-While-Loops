# print out the numbers 1 - 10

number = 1


while(number <= 10):
  print(number)
  number += 1

# print all even numbers between 0 - 20

number = 2
 
while(number <= 20):
 print(number)
 number += 2

# Ask the user for a number 
# print all numbers up to the user's name starting at 1
numberinput = int(input("Please input a number: "))
counter = 1
while(counter <= numberinput):
  print(counter)
  counter += 1 

# while (condition):
#   if(condition):
#     print

# Alternative way to print even numbers
counter = 1
while(counter <= 20):
  if(counter % 2 == 0):
   print(counter)
  counter += 1

# print all the numbers between 1 - 100, that are divisible by 3 or 7
# BUT NOT BOTH
counter = 1
while(counter <= 100):
  if(counter % 3 == 0 or counter % 7 == 0):
    if not(counter % 3 == 0 and counter % 7 == 0):
      print(counter)
  counter += 1

# print all the numbers between 1 - 100
# if the number is divisible by 3, print out "Fizz"
# if the number is divisible by 5, print out "Buzz"
# if the number is divisible by 3 and 5, print out "Fizz Buzz"

counter = 1
while(counter <= 100):
  if(counter % 3 == 0 or counter % 5 == 0):
    if(counter % 5 == 0 and counter % 3 == 0): 
      print("FizzBuzz")
    elif(counter % 3 == 0):
      print("Fizz")
    elif(counter % 5 == 0):
      print("Buzz")
  else:
   print(counter)
  counter += 1