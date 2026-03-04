# loops 
print(0)
print(1)
print(2)
print(3)

# loops for loop and while loop
#for 

#print 0 to 10

for x in range(10):
  print(x)   
  
# range(startIndex(optional),endIndex(not included),stepSize(optional))
# startIndex : if not given by default 0
# stepSize : if not give size is 1

# inilization == start index  ==default =0 
# condition / endIndex(endIndex is not included )  == x < endIndex 
# stepSize == increment / decrement == default 1

for x in range(11):
  print(x)
  
print("------------------")  
#print 1 to 10

for a in range(1,11):
  print(a)
  
#print table of 2  

for x in range(2,21,2):
  print(x)

# # print dipanshu 5 times

for a in range(5):    #x=0,1,2,3,4
  print("dipanshu")    # dipanshu(0), dipanshu(1),dipanshu(2), dipanshu(3),dipanshu(4),x=5(is 5 less 5)

#print table of 5
for x in range(5,51,5):    #x=5, 10,15,.....45,50,55
  print(x)                 #5, 10, 15,......45,50


#print 10 to 1

for x in range(10,0,-1):
  print(x)


#print table of 2 in reverse

for x in range(20,1,-2):
  print(x)

#break and continue

#print 1 to 10 but at 7 break

for x in range(1,11):    #x=1,2,3...7
  if x==7:
    break                # comes out of loop 
  print(x)               #x=1,2,3,4,5,6

print("----------------")


for x in range(1,11):    #x=1,2,3...7
  print(x)               #x=1,2,3,4,5,6,7
  if x==7:
    break                # comes out of loop 
 

#continue
#print 1 to 10 but at 7 skip

for x in range(1,11):     #x=1,2,3,4,5,6,7,8,9,10,11
  if x==7:                #x=7 true
    continue              #skip   x=8
  print(x)               #x=1,2,3,4,5,6,8,9,10