# functions and types 
#comparision operator

# i/p (entity)  ----> i/p(entity)

# ==, >,>=,<,<=,!=   ==>result True/False

print(7 == 7)
print(7 == 9)

print(5 > 5)  
print(5 >= 5)

print(5 < 3)
print(5 <= 5)

print(2 != 4)
print(2 != 2)

#logical operator  (True and False )
#and, or , not

#and (if any of input is false then output is false, true only when all inputs are true)
# i/p     i/p     ==>  output
# True   True          True
# True     False       False
# False    True       False
# False    False      False
 
 
 
print(3==3 and 3 > 2)
#      T   and   T    ==> T

print(3 == 3 and 3 >4)
print(3 != 3 and 3 < 4)
print(3 != 3 and 3 < 3)

#or (if and of input is true then output is true , false only when all inputes are false)
# i/p     i/p     ==>  output
# True   True          True
# True     False       True
# False    True      True
# False    False      False
 
print(3==3 or 3 > 2)
#      T  or   T    ==> T

print(3 == 3 or 3 >4)
print(3 != 3 or 3 < 4)
print(3 != 3 or 3 < 3)


# not 
# True ==> False
# False ===>True

print(not(3==3))
#    not(T)
#     F

print(not(3 > 3))
#     not(F)
#      T


print(not(5 >= 4  and 8 <= 9))
#     not(T   and  T)
#    not(T)
#   F

# basic datatypes , function and its types, comparision operator and logical operator
# # conditional operators 
# if --else 
# if -- elif ---else