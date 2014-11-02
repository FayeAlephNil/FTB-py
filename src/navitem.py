__author__ = 'elijahfoster-wysocki'
#Version 0.1.4

import shutil
import tempfile
import sys
import os

# EDIT THIS IF YOU HAVE CHANGED YOUR DIRECTORY NAMES.
directory = 'work/navitem/input.txt'
new_dir = 'work/navitem/output.txt'

#These can be found on Template:G/Mods.
#If you are running Python 3, change raw_input to input for it to work. You may still get errors though.
modname = raw_input("What is the mod abbreviation?\nIf you are unsure, or it is not on the list, please contact Santa. If you are Santa, do it.\n")

tmp = tempfile.NamedTemporaryFile(delete=False)
with open(directory) as finput:
    with open(tmp.name, 'w') as ftmp:
        for line in finput:
            x = str(line)
            ftmp.write('\t-->{{NI|' + x.rstrip("\r\n") + "|mod=" + modname + "}}{{,}}<!--\n")
try:
    shutil.copyfile(tmp.name, new_dir)
except:
    print "There was an issue using shutil! Trying to use os instead."
    os.rename(directory, new_dir)

sys.exit()

'''
== Changelog ==
=== 0.1.4 ===
* FIX: Changed directories to work/navitem/input-output.txt, for when I add more programs to this repo.

=== 0.1.3 ===
* FIX: Fixed tab spacing; it's no longer 4 spaces.

=== 0.1.2 ===
* FIX: No longer overwrites input; instead it makes output.txt.
* FIX: It should now work, though be weird, on non-UNIX-based systems. (thanks wolfman)
* FIX: Program exits properly with sys.exit

=== 0.1.1 ===
* FIX: Made the text that gets written actually correct.
* TWEAK: Changed modname raw_input text.

=== 0.1.0 ===
* Initial build.

'''