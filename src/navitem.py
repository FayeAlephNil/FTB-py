__author__ = 'elijahfoster-wysocki'

import re

# EDIT THIS IF YOU HAVE CHANGED YOUR DIRECTORY NAMES.
directory = 'work/input.txt'

#These can be found on Template:G/Mods.
modname = raw_input("What is the mod abbreviation?\n")

input_file = open(directory)
x = input_file.readlines()
if len(x) > 0:
    for line in input_file:
        input_file.write("{{NI|" + x + "|mod=" + modname + "}}")
input_file.close()




'''
for line in hand:
    line = line.rstrip()
    x = re.findall()
    if len(x) > 0:
        print "{{NI|" + x + "|mod=" + modname + "}}"
'''