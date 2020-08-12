
# Python 3 does not accept mixture of tab and spcae for indentation and prefers only spaces.
# This program can be used while migration of code from python 2x to 3x.
# 1 tab  = 4 spaces . Replace tab by 4 spaces.

import os

file_path = 'test.py'
spaces = "    "
file = open(file_path, 'r')
content = file.read()
content = content.replace("\t", spaces)
file.close()
file = open(file_path, 'w')
file.write(content)
