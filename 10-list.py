#list in python

x=10
print(x)

y=20
print(y)

z=30
print(z)

#storing multiple values in one variable
# it is accessed by index ...index always starts form 0

#           0  1  2
numbers = [10,20,30]

print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[2])

#            0       1         2               3
cities = ["pune","nagpur","chandrapur","sambhajinagar"]
print(cities)
print(cities[0])
print(cities[1])
print(cities[2])
print(cities[3])


info = ["dipanshu","chawde","pune",40,True]
print(info)

print(type(x))
print(type(info))


#CRUD  -- create , retrive , update , delete
#            0       1        2       3
fruits  =["apple","banana","greps","papaya"]

print(fruits)
print(fruits[2])

#update
fruits[1]  = "mango"
print(fruits)
print(fruits[1])

# find perticulare element in list
vegetable = ["onion","potato","garlic","tomato"]

print("potato" in vegetable)

print("ginger" in vegetable)

print("Potato" in vegetable)   # case sensitive

# max and min
num = [12,4,56,78,23,99,100,34,56,2,5,500,-9]
print(max(num))
print(min(num))


#length
#             0         1        2         3        length of vegetable = 4
vegetable = ["onion","potato","garlic","tomato"]

print(vegetable)
print(len(vegetable))

print(len(num))

# looping 
#            0       1         2               3
cities = ["pune","nagpur","chandrapur","sambhajinagar"]

print(cities[0])
print(cities[1])
print(cities[2])
print(cities[3])

#use looping
#range(start index, end index, step size)
#print 0 to 2 
for el in range(3):
    print(el)

for inx in range(4):
    print(cities[inx])      #cities[0],  cities[1], cities[2], cities[3]

print("--------------------")
#       0  1 2 3   4  5   6  7  8 9 10 11  12
num = [12,4,56,78,23,99,100,34,56,2,5,500,-9]

#                13
for x in range(len(num)):
    print(num[x])