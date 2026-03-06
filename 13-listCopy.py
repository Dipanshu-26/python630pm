num1=[11,22,33,44]

num2=num1      #copy reference 

print(num1)
print(num2)

num1[1]=777

print(num1)
print(num2)

num2[3]=999 
print(num1)
print(num2)

#-----------------------------------------------------

listA = ['a','b','c','d','e']

listB = listA.copy()

print(listA)
print(listB)

listA[2] =11
print(listA)
print(listB)

listB[4] =49
print(listA)
print(listB)