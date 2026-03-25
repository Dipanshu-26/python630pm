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
