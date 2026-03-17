#strings in python 

a="dipanshu"
print(a)
print(type(a))

b='niranjan'
print(b)
print(type(b))

c = """
Hello i am learning python ,
python is go to language for AI
"""

print(c)
print(type(c))

d= ''' Hello i am learning python and python is go to language for AI '''
print(d)
print(type(d))

# f string in python 
fn="neel"
ln="chawde"

print(f'my name is {fn} and my surname is {ln}')

print("my name is "+fn+" and my surname is "+ln)

print(f'my name is {fn}...\nmy surname is {ln}...')

print("my name is "+fn+"...\nmy surname is "+ln+"...")

#---------------------------------------------------------------

names=["dipanshu","aditya","rucha"]
print(names[0])
names[0]="neel"
print(names)


#string is immuatable
#     012345678
fn = "dipanshu"
print(fn[0])

#fn[0]="k"  #'str' object does not support item assignment
#            0      1        2
#          0123   012345   012345
cities = ["pune","nagpur","mumbai"]

print(cities[0])
print(cities[2][2])

print("nagpur" in cities)

fn = "dipanshu"
print("d"in fn)
print("x"in fn)

#----------------------------------------------------------------
#looping
#for
for ch in fn:      #ch=0,1,2,3.... 
    print(ch)

nm="niranjan"
for c in range(len(nm)):       #c=0,1,2,3,.....
    print(c)                #c=0,1,2,3,.....
    print(nm[c])           #nm[0],nm[1],nm[2]....

#while
i=0
while i<len(nm):
    print(nm[i])
    i=i+1    

x="DipAnsHu CHawDE"
print(x.upper())    
print(x.lower())
print(x.capitalize())