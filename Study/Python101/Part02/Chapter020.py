# The sys Module

# sys.argv
import sys
'''
print(sys.argv)

# sys.excutable
print(sys.executable)

# sys.exit
sys.exit(0)

# sys.path
print(sys.path)
'''

'''
# sys.platform
os = sys.platform
if os == "win32":
    # use Window-related code here
    import _winreg
elif os.startswith('linux'):
    # do something Linux specific
    import subprocess
    subprocess.Popen(["ls", "-l"])
'''

# sys.stdin / stdout / stderr

