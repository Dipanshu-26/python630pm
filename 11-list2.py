#loops, CRUD operations
#         0            1       2      3
names = ["dipanshu","nitin","neel","tanish"]

#for

for x in range(len(names)):
    print(names[x])


#while

i=0
while(i<len(names)):     #i=0,1,2,3, 4   
    print(names[i])
    i=i+1

#adding new element inlist

#append, insert, extend

# append - adds element at last of list

fruits = ["grapes","banana","papaya","apple","mango"]
fruits.append("orange")
print(fruits)

x=[1,2]
y=[3,4]
x.append(y)      #[1,2,[3,4]]
print(x)

#insert 
# insert  - adds element at the given index and shift at other element to right side
#            0        1       2         3       4
fruits = ["grapes","banana","papaya","apple","mango"]      #len(fruits)=5
fruits.insert(2,"kiwi")
print(fruits)

#add element at the last
fruits.insert(len(fruits),"strawberry")
print(fruits)

fruits.insert(0,"mango")
print(fruits)

# extend - one list to another list
# extend() in Python is a list method used to add multiple items from another iterable (list, tuple, set, string, etc.) 
# to the end of the list.

listA = ["a","b","c","d"]
listB = ["e","f","g"]

listA.extend(listB)
print(listA)
print(listB)

a=["d","i","p"]
a.extend("anshu")
print(a)

# deleting element from list

# del listname[i], pop(i),pop, remove(value),clear 

# del - delets element

fruits = ["grapes","banana","papaya","apple","mango"]   
del fruits[1]
print(fruits)

fruits = ["grapes","banana","papaya","apple","mango"]   
fruits.pop()
print(fruits)

fruits = ["grapes","banana","papaya","apple","mango"]   
fruits.pop(2)
print(fruits)

# remove(value) - deletes first matching element
fruits = ["mango","grapes","banana","grapes","papaya","apple","mango"]  
fruits.remove("banana")
print(fruits)

fruits.remove("mango")
print(fruits)

fruits.remove("grapes")
print(fruits)

# fruits.remove("bananaa")     #ValueError: list.remove(x): x not in list
# print(fruits)


# clear -Deletes all elements
num = [1,2,3,4,5,6,7,8]
print(num)
num.clear()
print(num)

# | Method              | What it does                 | Works by |
# | ------------------- | ---------------------------- | -------- |
# | `del listname[i]`   | Deletes element              | index    |
# | `pop(i)`            | Deletes + returns element    | index    |
# | `pop()`             | Deletes last element         | —        |
# | `remove(value)`     | Deletes first matching value | value    |
# | `clear()`           | Deletes all elements         | —        |
