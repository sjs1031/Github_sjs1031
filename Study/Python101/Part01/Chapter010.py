# Functions
def a_function():
    print("")
    print("You just created a function!")
    print("")
a_function()

# An Empty function (the stub)
def empty_function():
    pass
empty_function()

# Passing Argguments to a Function
def add(a,b):
    return a + b

print(add(1,2))
print(add(a=2, b=3))
total = add(b=4, a=5)
print(total)
print("")

# Keyword Arguments
def keyword_function(a=1, b=2):
    return a + b

print(keyword_function(b=4, a=5))
print(keyword_function())

def mixed_function(a, b=2, c=3):
    return a + b + c

print(mixed_function(1, b=4, c=5))
print(mixed_function(1))

# *args and **kwargs or *bill and **kate

def many(*args, **kwargs):
    print(args)
    print(kwargs)

print(many(1,2,3, name='Mike', job='Programmer'))

# A note on Scope and Globals
def function_a():
    a = 1
    b = 2
    return a+b

def function_b():
    c = 3
    return a + c

print(function_a())
print(function_b())
