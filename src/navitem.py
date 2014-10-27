__author__ = 'elijahfoster-wysocki'
#Version 0.2

import shutil
import tempfile

# EDIT THIS IF YOU HAVE CHANGED YOUR DIRECTORY NAMES.
directory = 'work/input.txt'

#These can be found on Template:G/Mods.
modname = raw_input("What is the mod abbreviation?\nIf you are unsure, or it is not on the list, please contact Santa. If you are Santa, do it.\n")

tmp = tempfile.NamedTemporaryFile(delete=False)
with open(directory) as finput:
    with open(tmp.name, 'w') as ftmp:
        for line in finput:
            x = str(line)
            ftmp.write('    -->{{NI|' + x.rstrip("\r\n") + "|mod=" + modname + "}}{{,}}<!--\n")
shutil.move(tmp.name, directory)

'''
== Changelog ==
=== 0.2 ===
* fixed the text that is written.
* changed modname raw_input text
=== 0.1 ===
* initial
'''