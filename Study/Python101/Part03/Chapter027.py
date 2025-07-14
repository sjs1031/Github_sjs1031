# Code Profiling

# Profiling Your Code with cProfile

'''
# import hashlib
import cProfile
import Chapter027_ptest

cProfile.run("hashlib.md5(b'abcdefghijkl').digest()")

cProfile.run("Chapter027_ptest.main()")
'''

import pstats
p = pstats.Stats(".\Python_study_re\Python101\Part03\data\output.txt")
p.strip_dirs().sort_stats(-1).print_stats()