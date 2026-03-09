# list slicing list Comprehensions

# List Slicing -  allows you to extract parts of a list using : list[start : end : step]
# start → index where slice begins by default starts from 0
# end   → index where slice stops (not included) ,default last index
# step  → how many items to skip , default step size 1

# Basic slicing

#        0  1  2  3  4
nums = [10,20,30,40,50]

#list_name[start_index: end_index:step_size]

#print forom 1 to all
print(nums[1:])


#start to index 3 
print(nums[:4:])

# print whole list
print(nums[:])

#        0  1  2  3  4  5  6  7  8
nums = [10,20,30,40,50,60,70,80,90]

print(nums[::2])

print(nums[::3])

#print list in reverse
print(nums[::-1])

#reverse step size 2

print(nums[::-2])

#pint odd step 
print(nums[1::2])

# List Comprehensions - List Comprehension provides a short, fast, clean way to create lists.
# Syntax: [new_item  for item in iterable  if condition]
#[expression for item in iterable]
# Basic Example

listA = [1,2,3,4,5]
print(listA)
#----------using foe loop-----
# square=[]
# for x in listA:
#     square.append(x*x)

# print(square)    

#----list comprehensition-----------------
#        [expression   for item in iterable]
square = [x*x for x in listA]
print(square) 

cube = [x*x*x for x in listA]
print(cube)


#filter even numbers
listA = [1,2,3,4,5,6,7,8,9,11,13,14]
# even = []
# for x in listA:
#     if x%2==0:
#         even.append(x)

# print(even)

#list comprehensition
print(listA)
even = [x for x in listA if x%2==0]
print(even)

odd = [x for x in listA if x%2!=0]
print(odd)

names = ["dipanshu","tanish","neel","nitin"]

upper_names = [x.upper() for x in names]
print(upper_names)

# create list of 0 to 10
numbers = [x for x in range(11)]
print(numbers)

# create list of  to 10
numbers = [x for x in range(1,11)]
print(numbers)

# create list of  table of 2
table2 = [x for x in range(2,21,2)]
print(table2)