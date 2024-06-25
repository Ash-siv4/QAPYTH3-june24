
# 4.	Using a for loop, display the files in your home directory, with their size
# a)	Use the skeleton file Ex3.py
# b)	Get the directory name from the environment using the dictionary os.environ with key HOMEPATH on Windows and HOME on Linux
# (we have done that part for you, notice the test of system.platform()).
# c)	Construct a portable wildcard pattern using os.path.join() -(we have done that part for you as well.
# d)	Use the glob.glob() function to obtain the list of filenames
# e)	Use os.path.getsize() to find each file's size
# f)	Add a test to only display files that are not zero length
# g)	Use os.path.basename() to remove the leading directory name(s) from each filename before you print it.


import glob
import os
import sys

if sys.platform == "win32":
    home_dir = os.environ['HOMEPATH']
else:
    home_dir = os.environ['HOME']

pattern = os.path.join(home_dir, "*")

for filename in glob.glob(pattern):
    size = os.path.getsize(filename)
    if size > 0:
        print(os.path.basename(filename), size)