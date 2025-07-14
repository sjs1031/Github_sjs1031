# The Subprocess module

# The call function
import subprocess

'''
code = subprocess.call("notepad.exe")
if code == 0:
    print("Success")
else:
    print("Error!")

code = subprocess.call(["ping", "www.yahoo.com"])
'''

'''
# The Popen Class
program = "notepad.exe"
process = subprocess.Popen(program)
code = process.wait()
print(code)
'''

# Learning to Communicate
'''
args = ["ping", "www.yahoo.com"]
process = subprocess.Popen(args, stdout=subprocess.PIPE)
data = process.communicate()
print(data)
'''

args = ["ping", "www.yahoo.com"]
process = subprocess.Popen(args, stdout=subprocess.PIPE)

data = process.communicate()
for line in data:
    print(line)