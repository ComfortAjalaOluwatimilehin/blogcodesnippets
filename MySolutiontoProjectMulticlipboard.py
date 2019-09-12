# mcb.pyw : Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard
# py.exe mcb.pyw list - Loads all keywords to clipboard
# py.exe mcb.pyw read <path text file> <keyword>

import shelve
import pyperclip
import sys
import os
import re


mcbShelf = shelve.open("mcb")

if len(sys.argv) == 4 and sys.argv[1].lower() == "read":
    # TODO: read file and save to shelf
    # check if path is valid
    path = sys.argv[2]
    if os.path.exists(path):
       # check if path is a text file
       if ".txt" in os.path.basename(path):
         # read file
         file = open(os.path.abspath(path))
         content = file.read()
         # close file
         file.close()
         key = sys.argv[3]
         mcbShelf[key] = content
       else:
         print("Path should lead to a text file")
   else:
     print("Path does not exist")
   # TODO: Save clipboard content 
elif len(sys.argv) == 3 and sys.argv[1].lower() == "save":
   content = pyperclip.paste() #copies the clipboard content 
   mcbShelf[sys.argv[2]] = content #stores the content to the keyword in the shelf object 
   # TODO : List keywords and load content 
elif len(sys.argv) == 2:
   keys = list(mcbShelf.keys())
   if sys.argv[1].lower() == "list":
     content = ""
     for pos in range(len(keys)):
       content += "{}. ".format(pos) + keys[pos] + "\n" 
       # content += mcbShelf[key] + "\n"*2
       # content += "-"*20 + "\n"*2
       pyperclip.copy(content)
       print(content)
   else:
      # TODO: Load keyword to clipboard
   if sys.argv[1] in keys:
     content = mcbShelf[sys.argv[1]]
     # paste to clipboard
     pyperclip.copy(content)
     print("\tkeyword: \n{}\n\tcontent: \n\n{}".format(sys.argv[1], content ) )
  else:
    print("Your command line arguments are invalid")
  



mcbShelf.close()
