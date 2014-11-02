FTB-py
======

Stuff for the FTB Wiki

navitems.py
-----------
This will turn a list of names in work/input.txt to NI templates. It will ask you for the mod abbreviation for use with the tilesheet extension. For example, 'Item' with abbreviation 'EX' will become '   -->{{NI|Item|mod=EX}}{{,}}<.!--'. (no period between < and !) input.txt will not be replaced, instead output.txt will be created. 

navbox.py
---------
This will ask you if you want a big or small navbox. Currently, only small ones are supported. It will then ask you how many groups you want. This can be anywhere from 1-20. It will ask you for the name of each group, and the mod's name, then it will use this data to create a formatted navbox. It doesn't do anything with the |list parameters.

navbox_small.py is a sub-file that is needed for navbox.py.
