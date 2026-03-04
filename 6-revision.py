a=10
print(a)
print(type(a))

a=-10
print(a)
print(type(a))
# 10,-10,22,-22

a=20.4
print(a)
print(type(a))

a=-20.4
print(a)
print(type(a))
#10.5,-10.5

a=True
print(a)
print(type(a))
#True,False

true = 200
a=true
b=a
print(b)
print(type(b))

a="dipanshu"
print(a)
print(type(a))

a='dip@123'
print(a)
print(type(a))

a="10+10"
print(a)
print(type(a))

a="@#$"
print(a)
print(type(a))
#"a","absfdg","dip@123","112233","@#$"


#arithmatic operators

a=10
b=20 
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)


#functions 

#without parameter and without return type
#function defination
def greet():
  print("Hello Dipanshu....")

#call 
greet()
greet()
greet()

#with parameter and without return type
#function defination
def cube(x):    # x isparameter   x=5      x=15
  print(x*x*x)   # print(5*5*5)       print(15*15*15)


#function call  
cube(5)     #5 is argument
cube(15)  

#with parameter and with return type

def square(y):
  res = y*y
  return res

#call 

sq = square(10)
print(sq)

#comparison operators 
# ==,!=,>,>=,<,<=

#entity  ==>entity ===> True / False
print(3==3)
print(3!=3)

#logical operators
# and  => if any of input is false o/p is false , true only when all i/ps are true
# or   => if any of input is True o/p is True , false only when all i/ps are false
# not  =>  true==>false   false => true

print(3!=3 and 3>=2)
print(3!=3 or 3>=2)

print(not(3!=3 or 3>=2))


#conditional operators
#if--elif--else
#one input and multiple output

#find greator number
x=200
y=200

if x>y:
  print("x is greater")
elif y>x:
  print("y is greator")
else:
  print("both are equal..")
  
# find greater number of 3 

a=10
b=30
c=30

if a>b and a>c:
  print("a is greater")
elif b>a and b>c:
  print("b is greater")
elif c>a and c>b:  
  print("c is greator")
else:
  print("either any of 2 or all are equal...")