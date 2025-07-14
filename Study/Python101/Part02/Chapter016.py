# The OS module

'''
# os.name
import os
print(os.name)
'''

'''
# os.environ
import os
print(os.environ["TMP"])
os.getenv("TMP")
'''

'''
# os.chdir() and os.getcwd()
import os
print(os.getcwd())
print(os.chdir(".\Python_study_re\Python101\Part01\"))
'''

'''
# os.mkdir() and os.makedirs()
import os
path = r'.\Python_study_re\Python101\Part03'
os.mkdir(path)
'''

'''
# os.remove() and os.rmdir()
import os
path = r'.\Python_study_re\Python101\Part03'
os.rmdir(path)
'''

'''
# os.rename(src, dst)
import os
src = r'.\Python_study_re\Python101\Part02\source.rename'
dst = r'.\Python_study_re\Python101\Part02\destination.rename'
os.rename(src, dst)
'''

'''
# os.startfile()
import os
os.startfile(r'.\Python_study_re\Python101\Part02\logging.conf')
'''

'''
# os.walk()
import os
path = r'.\Python_study_re\Python101\Part02'
for root, dirs, files in os.walk(path):
    print(root)
    for _files in files:
        print(_files)
'''

# os.path
import os
print(os.path.basename(r'.\Python_study_re\Python101\Part02\Chapter015.py'))
print(os.path.dirname(r'.\Python_study_re\Python101\Part02\Chapter015.py'))
print(os.path.exists(r'.\Python_study_re\Python101\Part02\Chapter015.py'))
print(os.path.isdir(r'.\Python_study_re\Python101\Part02\Chapter015.py'))
print(os.path.isfile(r'.\Python_study_re\Python101\Part02\Chapter015.py'))
print(os.path.join(r'.\Python_study_re\Python101\Part02', 'Chapter015.py'))
print(os.path.split(r'.\Python_study_re\Python101\Part02\Chapter015.py'))