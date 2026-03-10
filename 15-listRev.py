# list slicing list Comprehensions

# List Slicing -  allows you to extract parts of a list using : list[start : end : step]
# start → index where slice begins by default starts from 0
# end   → index where slice stops (not included) ,default last index
# step  → how many items to skip , default step size 1

# Basic slicing
#      0 1 2 3 4 5 6 
num = [11,22,33,44,55,66,77]

#slicing
#list_name[start:endIndex:step]

#print 1 to all
print(num[1:])

#print feom satrt to index 4
print(num[:5])

#print whole list
print(num)
print(num[:])

#print reverse
print(num[::-1])

#      0   1  2  3  4  5  6  
num = [11,22,33,44,55,66,77]
print(num[::2])

print(num[1::2])

print(num[::-2])

print(num[5::-2])


# List Comprehensions - List Comprehension provides a short, fast, clean way to create lists.
# Syntax: [new_item  for item in iterable  if condition]
#[expression for item in iterable]
# Basic Example

num=[1,2,3,4,5,6,7]

#using for loop
# square = []
# for x in num:
#     square.append(x+x)

# print(square)

#using list comprehension
square = [x*x for x in num]
print(square)

cube = [x*x*x for x in num]
print(cube)


names = ["dipanshu","neel","nitin","tanish"]

names_upper=[x.upper() for x in names]
print(names_upper)

#filter even numbers
listA = [1,2,67,3,88,4,5,6,7,8,9,11,13,14]

#using for loop 
# even=[]
# for x in listA:
#     if x%2==0:
#         even.append(x)
        
# print(even)        

even = [x for x in listA if x%2==0]
print(even)

odd = [a for a in listA if a%2!=0]
print(odd)

#nested loops with comprehension

#[1,2]   [3,4]  ===> [1,3], [1,4], [2,3],[2,4]

pair = [(x,y) for x in [1,2] for  y in [3,4]]
print(pair)

#nested for loop
list1=[1,2]
list2=['a','b']
pair2=[(x,y) for x in list1 for y in list2]
print(pair2)



# pair2=[]
# for x in list1:   #  1          2
#     for y in list2:  # a ,b    a   b
#         a=(x,y)
#         pair2.append(a)
# print(pair2)        