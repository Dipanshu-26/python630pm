#tuple
# A tuple is a collection of items, just like a list, but with one important difference:
# Tuples are immutable (cannot be changed after creation)

listA = [10,20,30,40]   #list 
print(listA)
listA[1]=44
print(listA)
print(type(listA))
print(30 in listA)

#tuple
tupA = 11,
print(tupA)
print(type(tupA))

tupB = 11,22,33,44
print(tupB)
print(type(tupB))

tupC = ("dipanshu","chawde",11,True)
print(tupC)
print(type(tupC))

# does tuple stores the values by index -- yes

print(tupC[0])
print(tupC[1])
print(tupC[2])
print(tupC[3])

# tupC[1]="masalkar"   #TypeError: 'tuple' object does not support item assignment
# print(tupC)

tupC = (100,200,300)
print(tupC)

# can we update 1 single value ? No , fixed length 
# tuples are fixed length 

# Why Use Tuple?
# When data should not change (e.g., coordinates, constants)
# Faster than lists
# Safe from accidental modification

#particular value exists in tupple

tupC = ("dipanshu","chawde",11,True,"pune")
print("dipanshu" in tupC)
print("Dipanshu" in tupC)

# length of tuple
print(len(listA))
print(len(tupC))

tupD=[11,5,77,3,99,22,7,10]
print(max(tupD))
print(min(tupD))


print(type([1,2,3,4,4]))
print(type((1,2,3,4,5)))

#packing and unpacking

#        0  1  2  3
tupE = (11,22,33,44)     #packing
print(tupE)

a,b,c,d = tupE         #unpacking
print(a)
print(b)
print(c)
print(d)

tupF = (11,22,33,44)
x,y,z,p = tupF
print(x)
print(y)

#looping
tupF = (11,22,33,44,55,66)
for x in range(len(tupF)):
    #print(x)         #print only index
    print(tupF[x])


tupG = ("a","b","c","d","e")
i=0
while(i<len(tupG)):
    print(tupG[i])
    i=i+1

# count - counts numbers of occurence of element
tupG = ("a","b","e","c","e","d","e")
print(tupG.count("e"))
print(tupG.count("a"))
print(tupG.count("z"))

# index finds of index of element
print(tupG.index("a"))
print(tupG.index("c"))
print(tupG.index("e"))
#print(tupG.index("z"))    #ValueError: tuple.index(x): x not in tuple

#Single Element Tuple (Important)
t = (5,)   # correct
t = (5)    # wrong → becomes int

# Key Characteristics
# - Ordered (items keep their position)
# - Immutable (cannot modify, add, or remove items)
# - Allows duplicate values
# - Can store different data types