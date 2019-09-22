# madlib : Scans text and replaces ADVERB, ADJECTIVE, NOUN and VERB with user values
# Usage python madlib.py <textfile>

import sys
import re
import os

keywords = ("Lorem", "is", "that", "will")
# TODO: READ COMMAND LINE ARGUMENTS
if len(sys.argv) == 2:
    # TODO: CHECK VALIDITY OF TEXT PATH GIVEN
    if os.path.exists(sys.argv[1]):
        # TODO: READ CONTENT OF FILE
        textFile = open(os.path.abspath(sys.argv[1]))
        content = textFile.readlines()
        textFile.close()
        if len(content) <= 0:
            print("File is empty")
        else:
            # TODO: LOOP THROUGH KEYWORDS, ASK USER FOR REPLACEMENT AND SUBSTITUTE WORD
            # get name of file
            textFileName = os.path.basename((os.path.abspath(sys.argv[1])))
            textFileName = textFileName.split(".")

            # create a new name for text file
            textFilePath = os.path.join(os.path.dirname(
                sys.argv[1]),
                "{}_updated.{}".format(textFileName[0], textFileName[1])
            )
            textFile = open(os.path.abspath(textFilePath), "w")
            textFile.write("")
            textFile.close()
            textFile = open(textFilePath, "a")
            for line in content:
                # loop over each line in content list
                updateline = line
                for keyword in keywords:
                    # loop over each keyword in keywords
                    # check for match of keyword in updateline
                    pattern = r"({}|{})".format(
                        keyword.lower(), keyword.upper())
                    reg = re.compile(pattern)
                    if reg.search(updateline):
                        # if 'adverb' is in the first line e.g.
                        # replace the word with user input
                        replWord = input(
                            "What word to replace {}: ".format(keyword))
                        # check if user provided a replacement
                        if replWord:
                            # replace word
                            updateline = re.sub(
                                pattern, replWord, updateline)
                            # if user did not provide leave the updateline unmodified
                            # if no match is found leave the updateline unmodified
                            # after each substitution of a key word, write the updateline in the textFile
                textFile.write(updateline)
            # when entire content is updated, close file
            textFile.close()

    else:
        print("Given path does not exist")

    textFile.close()
else:
    print("Provide a text file path")

# TODO: PRINT RESULT AND UPDATE FILE WITH NEW CONTENT
