# =========================================
# GENERATORS AND DECORATORS IN PYTHON
# =========================================

# =====================================================
# PART 1 : GENERATORS
# =====================================================

# Important Note:
# return → ends the function completely
# yield  → pauses the function and returns value one by one


# ---------------------------------
# Example 1 : return statement
# ---------------------------------

def gen_numbers():
    return 1
    return 2
    return 3
    return 4

res1 = gen_numbers()
print(res1)
res1 = gen_numbers()
print(res1)

# ---------------------------------
# Example 2 : return multiple values using list
# ---------------------------------
def gen_numbers2():
    return [1,2,3,4]

res1 = gen_numbers2()
print(res1)

print("--------------------------------------")
# ---------------------------------
# Example 3 : Generator using yield
# ---------------------------------

# A generator is a special type of function
# that returns values one by one using yield

def gen_numbers3():
    yield 1
    yield 2
    yield 3
    yield 4

gen = gen_numbers3()
print(gen)               #<generator object gen_numbers3 at 0x0000022DFFEB94E0>

#next 
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#print(next(gen))     #error : StopIteration
print("---------------------------------")


# ---------------------------------
# Example 4 : Infinite Generator
# ---------------------------------

def infinite_numbers4():
    n=1
    while True:
        yield n 
        n=n+1

gen2 = infinite_numbers4()

print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))


print("---------------------------------")


# ---------------------------------
# Example 5 : Generator with for loop
# ---------------------------------

def get_numbers4():
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50

for x in get_numbers4():
    print(x)    

print("---------------------------------")
# ---------------------------------
# Example 6 : Generator for Squares
# ---------------------------------

def square_generator():
    for i in range(1,6):
        yield i*i

for values in square_generator():
    print(values)

print("---------------------------------")
# ---------------------------------

def square_generator2(start, stop):
    for i in range(start,stop+1):
        yield i*i

for values in square_generator2(5 , 10):
    print(values)

print("---------------------------------")

# =====================================
# DECORATORS IN PYTHON – Explanation
# =====================================

# Decorator means:
# Before a function runs → do something
# Run the original function
# After function runs → do something

# Real-life Example:
# Before entering office → security check
# Enter office → main work
# After work → exit process

# Syntax:
# @decorator_name

# syntax
# def decorator_name(func):
#     def wrapper():
#         before stmts 
#         func
#         after stmts 
#     return wrapper

# func → original function
# wrapper → extra functionality holder

# ---------------------------------
# Example 1 : Basic Decorator
# ---------------------------------

# Step 1 : Defining Decorator

def my_decorator(func):
    def wrapper():
        print("I am before function call")
        func()
        print("I am after function call")
    return wrapper    


# Step 2 : Using Decorator

@my_decorator
def say_hello():
    print("I am original function")

# Step 3 : Calling Function
say_hello()    


#explanation

#say_hello() = my_decorator(say_hello)
# print("I am befor function call")
# say_hello function call (print("I am original function"))
# print("I am after function call")


# ---------------------------------
# Example 2 : Decorator with Parameters
# ---------------------------------

def my_deco(myfunc):
    def wrapper(a,b):
        print(f"Adding {a} and {b}")
        result = myfunc(a,b)
        print(f"Result = {result}")
    return wrapper    

        
@my_deco
def add(x,y):
    return x+y       

#call
add(100,200)

#explanation
# add(100,200) = my_deco(add)
# print(f"Adding {a} and {b}")
# myfunc(a,b)   (add(a,b))
# print(f"Result = {result}")