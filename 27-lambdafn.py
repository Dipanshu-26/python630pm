#addition of 2 numbers

def addA(x,y):
    return x+y

res1=addA(10,20)
print(res1)

#lambda 

addB = lambda x,y:x+y

print(addB(11,22))

# lambda --> keyword
# x,y -->parameter
# x+y -->return

#square

square = lambda x:x*x
print(square(4))
sq = square(8)
print(sq)

cube = lambda y: y*y*y 
print(cube(6))

#function as parameter

def addition():
    fn = lambda x,y: x+y
    x=55
    y=66
    a1 = fn(x,y)
    return a1

res2 = addition()
print(res2)

#-----------------------------------
addC= lambda x,y:x+y
#            addC 111 222
def addition2(fn,a,b):
    a2 = fn(a,b)
    return a2    #333

print(addition2(addC,111,222))


subA = lambda x,y:x-y
def sub(fn,a,b):
    s1 = fn(a,b)
    return s1

res3 = sub(subA,100,50)
print(res3)

print(addition2(subA,200,2))