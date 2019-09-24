
# USAGE python brute_force.py <pdfFile>

import PyPDF2
import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

if len(sys.argv) == 2:
    # TODO: GET PDF FILE
    filename = sys.argv[1]
    filename = os.path.abspath(filename)
    # TODO: CHECK IF EXISTS
    if not os.path.exists(filename):
        logging.error("File: " + str(filename) + "does not exist ")
    else:
        # TODO: GET DICTIONARY
        dict = open(os.path.abspath(".\\automate\\dictionary.txt"), "r")
        # TODO: CREATE PDF READER
        fileRead = open(filename, "rb")
        pdfReader = PyPDF2.PdfFileReader(fileRead)
        # TODO: LOOP THROUGH WORDS
        for word in dict.readlines():
            # TODO: TEST LOWER AND UPPER CASE OF WORD
            # TODO: TILL MATCH - > BREAK
            if pdfReader.decrypt(word.lower()) == 1:
                logging.info("Password match found: " + str(word.lower()))
                break
            elif pdfReader.decrypt(word.upper()) == 1:
                logging.info("Password match found: " + str(word.upper()))
                break
    # TODO: CLOSE FILE
        logging.info("all passwords were tested")
        dict.close()
        fileRead.close()

else:
    logging.error("USAGE python brute_force.py <pdfFile>")
