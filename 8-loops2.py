# loops in python 

# for loop , break and continue 
# while loop , break and continue
# table of 2
for x in range(2,21,2):
  print(x)
  
# # table of 2 in reverse  
for x in range(20,1,-2):
  print(x)  
  
#table of 2, i want to stop at 16  
for x in range(2,21,2):
  if x==16:
    break
  print(x)
  
#table of 2, i want to skip 16  
for x in range(2,21,2):
  if x==16:
    continue
  print(x)
  
#----------------------------------------------------
#while
# inilization
# while condition
# inc/dec

#print 1 to 0

x=1         #inilization

while x<=10:     #condition   while x is less than or equal to 10  execute  x=1,2,3,4,......10
  print(x)
  x=x+1          #increment   #x=2,3,4,......11


#print table of 2

a = 2 

while a<=20:
  print(a)
  a=a+2
  
# print table 2 
x=1   #counter

while x<=10:    #x=1...to 10
  print(x*2)    # x*2 == 2,4,6.....20
  x=x+1         #x=1,2,......10,11


#print table of 3 in reverse

x=30

while x>=3:
  print(x)
  x=x-3 


# break   
#print 1 to 10 and stop at 7

x=1 
while x<=10:
  if x==7:
    break
  print(x)
  x=x+1
  
x=1 
while x<=10:   
  print(x)    
  if x==7:
    break
  x=x+1  
  
#continue  
#print 1 to 10 and skip at 7 

x=1
while x<=10:     #x= 1,2,3....7,8,7,9,10
  if x==7:      #x=7
    x=x+1        #x=8
    continue
  print(x)        #x=1,2,3....6,8,9,10
  x=x+1           #x=2,3,4....7, 9,10,11