#functions==> reusable block of  code

#function without parameter and without return type

#functuin defination 

def calculator():
  print(100+20)
  print(100-20)
  print(100*20)
  print(100/20)
  print(100%20)
  
# call 
calculator()

calculator()
#100,20
#500,20

print("--------------------")
#function with parameter and without return type

def calculator2(a,b):   #parameter
  print(a+b)
  print(a-b)
  print(a*b)
  print(a/b)
  print(a%b)
  
# call 
calculator2(500,20)     #arguments
print("--------------------")
calculator2(678,2)

print("--------------------")  
  
#function with parameter and with return type  
  
def average(x,y,z):
  avg=(x+y+z)/3
  return avg

#call 
res = average(20,30,40)
print(res) 
  
print("--------------------")  
  
  
def average2(x,y,z):
  avg=(x+y+z)/3
  print("hello")
  return avg
  print("hello")   #this will naver get executed
print("bye")       
#call 
res = average2(20,30,40)
print(res)   
print("--------------------")  
  
# amount deposit withdraw

balance = 10000

def deposit(amt):
  return balance+amt

def withdraw(amt):
  return balance-amt

print(balance)    #10000
#call 
balance = withdraw(5000)    #50000
print(balance)
balance = deposit(7000)     #12000
print(balance)