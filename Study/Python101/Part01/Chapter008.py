# Chapter 008 - Working with Files

# Read a File
handle = open(".\Python_Study_re\Test_001\Chapter008_test.txt","r")
data = handle.read()
print("\n"+data+"\n\n")
handle.close()

handle = open(".\Python_Study_re\Test_001\Chapter008_test.txt","r")
data = handle.readlines()
print(data)
handle.close()

# Read Files Piece by Piece
print("\n")
handle = open(".\Python_Study_re\Test_001\Chapter008_test.txt","r")
for line in handle:
    print(line)
handle.close()

print("\n")
handle = open(".\Python_Study_re\Test_001\Chapter008_test.txt","r")
while True:
    data = handle.read(1024)
    print(data)
    if not data:
        break
handle.close()

# Read a Binar file
# handle = open("test.pdf","rb")
print("")

# Writing Files in Python
handle = open(".\Python_Study_re\Test_001\Chapter008_output.txt","w")
handle.write("This is a test!")
handle.close()

# Using the with Operator
with open(".\Python_Study_re\Test_001\Chapter008_test.txt") as file_handler:
    for line in file_handler:
        print(line)
print("\n")

# Catching Errors
try:
    file_handler = open(".\Python_Study_re\Test_001\Chapter008_test.txt")
    for line in file_handler:
        print(line)
except IOError:
    print("An IOError has occurred!")
finally:
    file_handler.close()
print("\n")

try:
    with open(".\Python_Study_re\Test_001\Chapter008_test.txt") as file_handler:
        for line in file_handler:
            print(line)
except IOError:
    print("An IOError has occurred!")
print("\n")

handle = open(r"C:\Users\sjs10\OneDrive\git\RuleXuanOrg\Python\Python_Study\Python_Study_re\Test_001\Chapter008_test.txt", "r")
#print(handle)
