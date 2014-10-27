__author__ = 'elijahfoster-wysocki'
#Version 0.2

import shutil
import tempfile
import sys
import os

# EDIT THIS IF YOU HAVE CHANGED YOUR DIRECTORY NAMES.
directory = 'work/input.txt'
new_dir = 'work/udungoofd.txt'

#These can be found on Template:G/Mods.
#If you are running Python 3, change raw_input to input for it to work. You may still get errors though.
modname = raw_input("What is the mod abbreviation?\nIf you are unsure, or it is not on the list, please contact Santa. If you are Santa, do it.\n")

tmp = tempfile.NamedTemporaryFile(delete=False)
with open(directory) as finput:
    with open(tmp.name, 'w') as ftmp:
        for line in finput:
            x = str(line)
            ftmp.write('    -->{{NI|' + x.rstrip("\r\n") + "|mod=" + modname + "}}{{,}}<!--\n")
try:
    shutil.move(tmp.name, directory)
except:
    print "Permission Error/IOError! Trying something else save the file!"
    os.rename(directory, new_dir)

sys.exit()

'''
== Changelog ==
=== 0.3 ===
* hopefully fixed the Windows issue
* it now exits properly using sys.exit()
=== 0.2 ===
* fixed the text that is written.
* changed modname raw_input text
=== 0.1 ===
* initial
'''