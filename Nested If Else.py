##Find the largest of three number.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a>b:
  if a>c:
    print("Largest",a)
  else:
    print("Largest",c)
else:
  if b>c:
    print("Largest",b)
  else:
    print("Largest",c)

##Check whether a number is positive negative or zero.
num = int(input("Enter a number:"))
if num>=0:
  if num==0:
    print("Zero")
  else:
    print("Positive")
else:
  print("Negative")  

##Assign grades using nested if else.
marks = int(input("Enter your marks:"))
if marks>=60:
  if marks>=75:
    if marks>=90:
      print("Grade A")
    else:
      print("Grade B")
  else:
    print("Grade C")
else:
  print("Fail") 
##Grade criteria:
##A:90 or above  B:75-89  C:60-74  fail:Below 60  

##Check triangle type.

##All sides are equal:Equilateral.
##Two sides are equal:Isosceles.
##All sides are diffrent:Scalen.

a = int(input("Enter first side:"))
b = int(input("Enter second side:"))
c = int(input("Enter third side:"))
if a==b:
  if b==c:
    print("Equilateral Triangle")
  else:
    print("Isosceles Triangle")
else:
  if a==c or b==c:
    print("Isosceles Triangle")
  else:
    print("Scalen Triangle")

##Validate login using username and password.
username = input("Enter username:")
password = input("Enter password:")
if username=="admin":
  if password=="admin123":
    print("Login successful")
  else:
    print("Wrong password")
else:
  print("Wrong username")

##Check loan eligibility using age, salary, credit score.
##Assume criteria:
##Age>=21
##Salary>=25000
##credit score>=700
age = int(input("Enter your age:"))
salary = int(input("Enter your salary:"))
credit = int(input("Enter your credit score:"))
if age>=21:
  if salary>=25000:
    if credit>=700:
           print("Loan eligible")
    else:
      print("Low credit score")
  else:
    print("salary to low")
else:
  print("Age not eligible")  