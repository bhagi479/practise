# 1. wap to accept two intergers and check whether they are equal or not
"""  
x=int(input("Enter first value:"))
y=int(input("Enter second value:"))
if(x==y):
    print("Entered values are equal")
elif(x!=y):
    print("Entered values are not equal")
"""
#2. wap to check whether a given number is even or odd
"""
x=int(input("Enter a number:"))
if(x%2==0):
    print("Entered number is even")
else:
    print("Entered number is odd")
"""
# 3. wap to check whether a given number is positive or negative
"""
x=float(input("Enter a number:"))
if(x>0):
    print("Entred number is positive")
elif(x<0):
    print("Entred number is negative")
else:
    print("zero is neither positive nor negative")
"""
# 4. wap to find whether a given year is leap year or not
"""
year=int(input("Enter a year:"))

if year%4==0 and year%100!=0:
    print("This is leap year")
elif year%100==0 and year%400!=0:
    print("this is not leap year")
elif year%400==0:
    print("this is a leap year")
else:
    print("this is not a leap year")

              OR    

if (year%4==0 and year %100!=0) or (year%400==0):
    print("leap year")
else:
    print("Non leap year")
"""
# 5. wap to read the age of candidate and determine whether  candidate eligible to caste his/her vote
"""
age=int(input("Enter the age:"))
if(age>=18):
    print("Eligible to cast his/her vote")

else:
    print("Not eligible to cast his/her vote")
"""
# 6. Wap to read the value of an integer m and display the value of n is 1 when m is larger than 0, 0 when m is 0, -1 when m is less than 0
"""
m= int(input("Enter the value: "))
if(m>0):
    print("value of n is 1")
elif(m==0):
    print("value of n is  0")
elif(m<0):
    print("value of n is -1")
"""
# 7. checking height of a person
"""
h= int(input("Enter height of a person in centimeters:"))
if(h<150):
    print("DWARF")
elif(h>=150 and h<165):
    print("Avereage Height")
elif(h>165):
    print("Tall")
"""
# 8. Wap to find largest of two numbers
"""
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
if(a>b):
    print("Largest number is", a)
else:
    print("Large number is", b)
"""
# 9. Wap to find largest of three numbers
"""
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))
if(a>b and a>c):
    print("Largest number is:", a)
elif(b>a and b>c):
    print("Largest number is:", b)
else:
    print("Largest number is:", c)
"""
# 10. wap to check whether a character is an alphabet, digit or special character
"""
ch = input("Enter a character: ")
if((ch>= 'a' and ch<='z') or (ch>='A' and ch<='Z')): 
    print("Entered character is an Alphabet: ",ch) 
elif(ch>='0' and ch<= '9'):
    print("Entered character is a Digit: ",ch)
else:
    print("Entered character is a Special Character: ",ch)

"""
# 11. Wap to check whether an alphabet is a vowel or consonant
"""
al=str(input("Enter an alphabet: "))
vowel='aeiou'
if(al=='a' or al=='e' or al=='i' or al=='o' or al=='u'):
    print("Entered alphabet is a vowel: ", al)
elif al in ('A', 'E', 'I', 'O', 'U'):
    print("Entered alphabet is a vowel: ", al)
else:
    print("Entered alphabet is a consonat: ", al)
"""
# 12. Wap to calculate profit and loss on a transaction from the given cost price (cp) and selling price (sp)
"""
cp= int(input("Enter a cost price: "))
sp= int(input("Enter a selling price: "))
profit= sp-cp
loss=cp-sp
if(profit==loss):
    print("No profit nor loss")
elif(sp>cp):
    print("Profit: ", profit)
else:
    print("Loss: ", loss)
"""
# 13. Wap to read temparature in centigrade and display suitable message according to the temperature
"""
temp=int(input("Enter a temperature in centigrade: "))
if(temp<0):
    print("Freezing Weather")
elif(temp>=0 and temp<=10):
    print("Very Cold Weather")
elif(temp>10 and temp<=20):
    print("Cold Weather")
elif(temp>20 and temp<=30):
    print("Normal in Temperature")
elif(temp>30 and temp<=40):
    print("Its Hot")
elif(temp>=40):
    print("Its Very Hot")
"""
# 14. Wap to eligibility of admission
"""
maths=int(input("Enter marks in Maths: "))
phy=int(input("Enter marks in Physics: "))
chem=int(input("Enter marks in Chemistry: "))
t1=maths+phy+chem
t2=maths+phy
if((maths>=65) and (phy>=55) and (chem>=50) and t1>=180):
    print("Eligible")
elif(t2>=140):
    print("Eligible")
else:
    print("Not Eligible")
"""
# 15. Wap to read roll no, name and marks of three subjects and calculate the total, percentage and division
"""
rno=int(input("Please enter a roll no: "))
name=str(input("Please enter a name: "))
s1=int(input("Enter the marks of first subject: "))
s2=int(input("Enter the marks of second subject: "))
s3=int(input("Enter the marks of third subject: "))
t=s1+s2+s3
print("Total of three subjects marks: ", t)
p=(t/300)*100
print("Percentage of three subjects marks: ", p)
if(p>=60):
    print("Division is First Class")
elif(p<60 and p>=48):
    print("Division is Second Class")
elif(p<48 and p>=36):
    print("Division is Pass")
elif(p<36):
    print("Division is Fail")
else:
    print("Invalid input")
"""
#16. Wap to accept a coordinate point in xy coordinate system and determine in which quadrant coordinate point lies
"""
x=int(input("Enter coordinate value of x: "))
y=int(input("Enter coordinate value of y: "))
if(x>=0 and y>=0):
    print("xy values lies in First Quadrant")
elif(x<=0 and y>=0):
    print("xy values lies in Second Quadrant")
elif(x<=0 and y<=0):
     print("xy values lies in Third Quadrant")
else:
    print("xy values lies in Fourth Quadrant")
"""
#17. Wap to check whether a triangle is equilateral, Isosceles and scalene
"""
x=int(input("Enter Triangle first angle value: "))
y=int(input("Enter Triangle second angle value: "))
z=int(input("Enter Triangle third angle value: "))
t=x+y+z
if(t==180):
    print("Triangle is: ")
    if(x==y and x==z):
        print("Equilateral")
    elif(x==z):
        print("Isoscelene")
    else: 
        print("scalene")
else:
    print("Wrong values entered:", t)
                  
                  (OR)
                  
x=int(input("Enter Triangle first angle value: "))
y=int(input("Enter Triangle second angle value: "))
z=int(input("Enter Triangle third angle value: "))
if(x==60 and y==60 and z==60):
    print("Equilateral")
elif((x+y+z==180) and x==z and y<z and y<x ):
    print("Isoscelene")
elif((x+y+z==180) and x!=y and x!=z and y!=z):
    print("Scalene")
else:
    print("Not formed triangle with given values")
"""
#18. Wap to check weather a triangle can be formed by the given value for the angles
"""
x=int(input("Enter Triangle first angle value: "))
y=int(input("Enter Triangle second angle value: "))
z=int(input("Enter Triangle third angle value: "))
t=x+y+z
if(t==180):
    print("Triangle formed with given vales: ",t)
else:
    print("Triangle not formed beacuse given values less than or above 180: ", t)
"""
#19. Wap to calculate and print electricity bill per unit
"""
ci= int(input("Enter the custimer id: "))
cn=str(input("Enter the customer name: "))
unit=float(input("Enter the units consumed by customer: "))
if(unit<=199):
    bill=unit*1.20
    print("Electricity Bill: ", bill)
elif(unit>=200 and unit<400):
    bill=unit*1.50
    print("Electricity Bill: ", bill)
elif(unit>=400 and unit<600):
    bill=unit*1.80
    print("Electricity Bill: ", bill)
elif(unit>= 600):
    bill=unit*1.80
    print("Electricity Bill: ", bill)
"""
#20. Wap to accept a grade and declare the equivalent description
"""
grade=str(input("Enter the Grade: "))
if(grade=='E'):
    print("Exellent")
elif(grade=='V'):
    print("Very Good")
elif(grade=='G'):
    print("Good")
elif(grade=='A'):
    print("Average")
elif(grade=='F'):
    print("Fail")
else:
    print("Invalid Input")
"""
#21. Wap to read any day number in integer and display day name in the word
"""
day=int(input("Enter a day number from 1-7: "))
if(day==1):
    print("Its Sunday")
elif(day==2):
    print("Its Monday")
elif(day==3):
    print("Its Tuesday")
elif(day==4):
    print("Its Wednesday")
elif(day==5):
    print("Its Thursday")
elif(day==6):
    print("Its Friday")
elif(day==7):
    print("Its Saturday")
else:
    print("Invalid Input")
"""
#22. wap to read any month number in integer and display the number of days for this month
"""
month=int(input("Enter month number from 1-12: "))
if(month==1):
    print("Its January- 31 days")
elif(month==2):
    print("Its February- 28 days for common year or 29 days for leap year ")
elif(month==3):
    print("Its March- 31 days")
elif(month==4):
    print("Its April- 30 days")
elif(month==5):
    print("Its May- 31 days")
elif(month==6):
    print("Its June- 30 days")
elif(month==7):
    print("Its July- 31 days")
elif(month==8):
    print("Its August- 31 days")
elif(month==9):
    print("Its September- 30 days")
elif(month==10):
    print("Its October- 31 days")
elif(month==11):
     print("Its November- 30 days")
elif(month==12):
    print("Its December- 31 days")
else:
    print("Invalid input")
"""
#22. Wap in python which is a Menu Driven program to perfrom a simple calculation
"""
print("*****Menu******")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
select=int(input("Select any number: "))
if(select>4):
    print("Invalid Input")
else:
    a=int(input("Enter fisrt value: "))
    b=int(input("Enter second value: "))
    if(select==1):
        c=a+b
        print("Addition is: ",c)
    if(select==2):
        c=a-b
        print("substraction is: ",c)
    if(select==3):
        c=a*b
        print("Multiplication is: ",c)
    if(select==4):
        c=a/b
        print("Divison is: ",c)

"""
#24. Wap which is menu driven program to compute the area of the various geometrical shape

print("*****Menu******")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")
select=int(input("Select any number: "))
if(select>3):
    print("oops!! Invalid Input")
else:
    if(select==1):
        radius=float(input("Enter the radius of circle: "))
        area=3.14*radius*radius
        result=round(area, 3)
        print("Area of Circle is: ", result)
    if(select==2):
        l=int(input("Length of Rectangle: "))
        w=int(input("Width of Rectangle: "))
        area=l*w
        print("Area of Rectangle is: ", area)
    if(select==3):
        h=int(input("Height of Triangle: "))
        b=int(input("Base of the Triangle: "))
        area=(b*h)/2
        print("Area of Triangle is: ", area)
        
  


    
    




    
    




         




    
