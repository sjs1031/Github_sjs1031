# Test005 - Exception Handling
print("")
# print (1 / 0)

try:
    1 / 0
except:
    print("You cannot divide by zero!\n\n")

my_dict = {'a':1, 'b':1, 'c':1, 'd':1}
try:
    value = my_dict['e']
except KeyError:
    print("That key does not exist\n")

my_list = [1,2,3,4,5]
try:
    my_list[6]
except IndexError:
    print("That index is not in the list\n")

my_dict = {"a":1, "b":1, "c":1, "d":1}
try:
    value = my_dict["e"]
except IndexError:
    print("This index does not exist!\n")
except KeyError:
    print("This key is not in the dictionary\n")
except:
    print("Some other error occurred!\n")

try:
    value = my_dict["e"]
except (IndexError, KeyError):
    print("An indexError or KeyError occurred!\n")

my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except KeyError:
    print("A keyError occurred!")
finally:
    print("The finally statement has executed!\n\n")

my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["a"]
except KeyError:
    print("A keyError occurred!")
else:
    print("No error occurred!\n\n")

my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["a"]
except KeyError:
    print("A keyError occurred!")
else:
    print("No error occurred!")
finally:
    print("The finally statement ran!\n\n")
