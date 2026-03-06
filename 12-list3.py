#sort , count, reverse , sorted

listA = [33,22,66,88,11,55]
print(listA)
listA.sort()
print(listA)

listB = ["dip","adi","zshan","karan","babita","aahan"]
print(listB)
listB.sort()
print(listB)

#sort in decending order
listA = [33,22,66,88,11,55]
listB = ["dip","adi","zshan","karan","babita","aahan"]
listA.sort(reverse=True)
print(listA)
listB.sort(reverse=True)
print(listB)

#sort changes the original list

#sorted() new sorted list return
listA = [33,22,66,88,11,55]
listB = ["dip","adi","zshan","karan","babita","aahan"]

new_listA=sorted(listA)
print(listA)
print(new_listA)

new_listB=sorted(listB,reverse=True)
print(listB)
print(new_listB)

#reverse() : reverse the elements of list 

numbers = ["a","b","c","d"]

print(numbers)
numbers.reverse()
print(numbers)

#count() : counts how many times value present in list

listB = ["dip","adi","zshan","karan","dip","babita","aahan","adi","adi"]
print(listB.count("dip"))
print(listB.count("adi"))

#sort()

words = ["apple","banana","fig","kiwi"]

words.sort(key=len)
print(words)

words = ["Fig","apple","Banana","kiwi"]
print(words)
words.sort()
print(words)

words.sort(key=str.lower)
print(words)