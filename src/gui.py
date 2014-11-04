# Created by Eli Foster
# Version 0.1.0

from Tkinter import *
from tkFileDialog import *
import tkMessageBox
from navitem import run
import ScrolledText
import tempfile
import shutil
import os

directory = 'work/navitem_output.txt'

def fn_navchanges():
    ch = Tk()
    changelog = Message(ch, text="0.1.1\n* FIX: Changed output dir\n\n0.1.0\n* Initial")

    changelog.pack()
    ch.mainloop()

def fn_abbrvchanges():
    ch = Tk()
    changelog = Message(ch, text="0.1.0\n* Initial")

    changelog.pack()
    ch.mainloop()

def fn_nichanges():
    ch = Tk()
    changelog = Message(ch, text="0.1.6\n*FIX: Shoved everything in run() method\n\n0.1.5\n *FIX: Changed directories AGAIN\n\n0.1.4\n* FIX: Changed directories to work/navitem/input-output.txt, for when I add more programs\n\n0.1.3\n* FIX: Fixed tab spacing; it's no longer 4 spaces, and is actually indents\n\n0.1.2\n* FIX: No longer overwrites input.txt; instead it makes output.txt\n* FIX: It should work now,  though be weird, on non-UNIX systems (thanks Wolfman)\n* FIX: Program exits properly using sys.exit()\n\n0.1.1\n* FIX: Made the text that gets written actually correct\n* TWEAK: Changed modname raw_input text\n\n0.1.0\n* Initial")

    changelog.pack()
    ch.mainloop()

def fn_guichanges():
    cl = Tk()
    changelog = Message(cl, text="0.1.0\n* Initial")

    changelog.pack()
    cl.mainloop()


def fn_open_changelog():
    cl = Tk()
    navboxchanges = Button(cl, text="Navbox Program changelog", command=fn_navchanges)
    abbrevchanges = Button(cl, text="Abbreviation Program changelog", command=fn_abbrvchanges)
    nichanges = Button(cl, text="NI Program changelog", command=fn_nichanges)
    guichanges = Button(cl, text="GUI Program changelog", command=fn_guichanges)

    guichanges.pack()
    nichanges.pack()
    abbrevchanges.pack()
    navboxchanges.pack()
    cl.mainloop()

def fn_openfile():
    filedialog = askopenfilename()
    filedialog.pack()

def fn_navitem():
    nav = Tk()
    navlabel = Label(nav, text="Mod abbreviation")
    navlabel.pack()
    naventry = Entry(nav)
    naventry.pack()

    filebutt = Button(nav, text="Select Input File", command=fn_openfile)
    filebutt.pack()


    nav.mainloop()

'''
    tmp = tempfile.NamedTemporaryFile(delte=False)
    with open(directory) as finput:
        with open(tmp.name, 'w') as ftmp:
            for line in finput:
                x = str(line)
                ftmp.write("\t-->{{NI|" + x.rstrip("\r\n") + "|mod=" + naventry.get() + "}}{{,}}<!--\n")
    try:
        shutil.copyfile(tmp.name, directory)
    except:
        print "There was an issue using shutil! Trying to use os instead."
        os.rename(directory, directory)
    #run()
'''



def fn_main():
    tk = Tk()
    changelog_button = Button(tk, text="Changelogs", command=fn_open_changelog)
    navitem_butt = Button(tk, text="NI Template Program", command=fn_navitem)
    quit = Button(tk, text="Quit Program", command=tk.quit)

    navitem_butt.pack()
    changelog_button.pack()
    quit.pack()
    tk.mainloop()

fn_main()

'''
== Changelog ==
=== 0.1.0 ===
* Initial
'''