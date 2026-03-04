#operatoers condiyionala and logical
#conditional statements

#one input and multiple output

# if condition:
#   statements
# else :
#   stmts 

# number <=5    5%desc
# number 6 to 10 10%desc
# number above 10 20% desc

# num = 10

# if num >0 and num <=5:      #f
#   print("5% discount")
# if num >5 and num <=10:     #t
#   print("10% discount")  
# if num > 10:                 #f
#   print("20 % discount")
  
#-------------------------------------

#if -- elif -- else
# num=-70

# if num > 0 and num <=5:
#   print("5% discount")
# elif num >5 and num <=10:   
#   print("10% discount") 
# elif num > 10:
#   print("20% discount")
# else:
#   print("enter correct number..")

#-------------------------------------

#marks >90 A  >75  B  >65 C

# marks = 96
# if marks > 90:
#   print("A")
# if marks > 75:
#   print("B")
# if marks > 65:
#   print("C")

marks = 46
if marks > 90:
  print("A")
elif marks > 75:
  print("B")
elif marks > 65:
  print("C")
else : 
  print("plz try again...")

#------------------------------------------
#find greater number of 2 numbers
x=100
y=1000

if x>y:
  print("x is greater")
else:
  print("y is greater")
  
print("----------------------")  
  
if x>y:
  print("x is greater")
elif y>x:
  print("y is greater")
else:
  print("both are same")
  
print("----------------------")    
  
#find greater number of 3 numbers  
a=100
b=200 
c=30

if a>b and a>c:
  print("a is greater")
elif b>a and b>c:
  print("b is greater")
else:
  print("c is greater")