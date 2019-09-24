# finds files with a give prefix in a folder
# locates any gaps in the numbering
# renames all the later files to close the gaps
# Usage: python gaps.py <source> <prefix>

import sys
import os
import shutil
import re
'''
Pseudocode:

-find source
-list all files in source folder
-filter in files starting with given prefix
-loop over length of filtered files
- 001, 010, 100
'''

if len(sys.argv) == 3:
    source = sys.argv[1]
    source = os.path.abspath(source)
    if os.path.exists(source):
        textFiles = []
        numbering = []
        prefix = sys.argv[2]
        reg = re.compile(r"^{}(\d+).txt$".format(prefix))
        for file in os.listdir(source):
            if reg.match(file):
                textFiles.append(file)
                match = reg.match(file)
                match = match.groups()[0]
                match = int(match)
                numbering.append(match)
                if len(textFiles) > 0:
                    gap = None
                for iterator in range(len(textFiles)):
                    if iterator not in numbering:
                        reg = re.compile(r"^{}(0+)\d*.txt$".format(prefix))
                        m = (reg.match(textFiles[iterator]))
                        if m:
                            m = m.groups()[0]
                        else:
                            m = ""

                for jterator in range(iterator, len(textFiles)):
                    curFile = textFiles[jterator]
                    curFile = os.path.join(source, curFile)
                    new_name = prefix + m + str(jterator) + ".txt"
                    new_filename = os.path.join(source, new_name)
                    shutil.move(curFile, new_filename)
            else:
                print("There are no other files with that prefix")

    else:
        print("Provide valid source path")
else:
    print("Usage: python gaps.py <source> <prefix>")
