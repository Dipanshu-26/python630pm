setA={11,22,33,44}
setB={11,33,55,66,77}
setC =setA.intersection(setB)
print(setC)

print("--------------------------")
setA={11,22,33,44}
setB={11,33,55,66,77}
setA.intersection_update(setB)
print(setA)    #{33, 11}
print(setB)    #{33, 66, 55, 11, 77}

print("--------------------------")
setA={"a","b","c",11,33}
setB={11,33,55,66,77}
setD=setA.difference(setB)
print(setD)

print("--------------------------")
setE=setB.difference(setA)
print(setE)

print("--------------------------")
setA={"a","b","c",11,33}
setB={11,33,55,66,77}
setA.difference_update(setB)
print(setA)

print("--------------------------")
setA={"a","b","c",11,33}
setB={11,33,55,66,77}
setB.difference_update(setA)
print(setB)

print("--------------------------")
setA={"a","b","c",11,33}
setB={11,33,55,66,77}
setF = setA.symmetric_difference(setB)
print(setF)
print(setA)
print(setB)

print("--------------------------")
setA={"a","b","c",11,33}
setB={11,33,55,66,77}
setA.symmetric_difference_update(setB)
print(setA)
print(setB)


# isdisjoint() - Checks if two sets have NO common elements.
# issuperset() - A set is a superset if it contains all elements of another set.
# issubset() - A set is a subset if ALL its elements are in another set.
# union() - Returns a new set with all elements from both sets.
# discard() - Removes an element from the set.
# ✔ discard() does NOT give error if the element is missing.
# ❌ remove() gives an error if element is not found.
print("--------------------------")
setA={"a","b","c"}
setB={11,33,55,66,77}

print(setA.isdisjoint(setB))

print("--------------------------")
setA={"a","b","c",11,33,55,66,77}
setB={11,33,55,66,77}

print(setB.issuperset(setA))
print(setA.issuperset(setB))  #True

print(setB.issubset(setA))

print("--------------------------")
setA={"a","b","c",11,33}
setB={1,2,3,4,5}
print(setA.union(setB))


#discard() - Removes an element from the set.
setA={"a","b","c",11,33}
setA.discard("a")
print(setA)

setA.discard("z")
print(setA)

setA.remove("z")
print(setA)