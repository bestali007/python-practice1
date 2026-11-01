##Write a program to check if a number is positive
num = int(input("Enter a number:"))
if num>0:
  print("positive number")
##print Eligible to vote if age is 18 or above 
age = int(input("Enter your age:"))
if age>=18:
  print("Eligible to vote")
##check if a number is divisible by 7
num = int(input("Enter a number:"))
if num%7==0:
  print("Divisible by 7")
##print pass if marks are greater than 40
marks = int(input("Enter your marks:"))
if marks>40:
  print("pass")
##check if a number is greater than 100
num = int(input("Enter a number:"))
if num>100:
  print("Number is greater than 100")
##Display a message if temprature exceeds 45degree C
temprature = int(input("Enter temprature:"))
if temprature>45:
  print("High temprature")
##check if a string length is more than 8 character
name = input("Enter a string")
if len(name)>8:
  print("String has more than 8 character")
##print logged if password matches admin123
password = input("Enter a password:")
if password =="admin123":
  print("Logged in")
##check if a number is multiple by 10 
num = int(input("Enter a number:"))
if num%10==0:
  print("multiple of 10")
##print a warning if balance is below minimum limit
balance = int(input("Enter your balance:"))
if balance <1000:
  print("Warning:Balance is minimum limit")
  