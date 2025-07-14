# test 001
'''
from matplotlib.pyplot import *

plot([1,2,3,10])

xlabel("x- axis")
ylabel("my numbers")
title("my figure")
show()
'''

# test002
i = 0
while i < 10:
    if i == 3:
        i += 1
        continue

    print(1)

    if i == 5:
        break
    i += 1

# Test 003
my_list = [1,2,3,4,5]

for i in my_list:
    if i == 3:
        print("Item Found")
        break
    print(i)
else:
    print("Item Not Found")

# test004
# List Comprehension
x =['1','2','3','4','5']
y =[int(i) for i in x]
print(y)

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

# Dictionay comprehension
print( {i: str(i) for i in range(5)})

my_dict = {1:'dog', 2:'cat', 3:'hamster'}
print( {value:key for key, value in my_dict.items()} )

# set Comprehensions
my_list= [1,2,3,4,5,6,7,8,9]
my_set = set(my_list)
print(my_set)

my_list  = [1,2,3,4,5,6,7,8]
my_set = {x for x in my_list}
print(my_set)


