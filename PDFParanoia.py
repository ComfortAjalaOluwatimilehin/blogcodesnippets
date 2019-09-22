# usage pdf_paranoia_encrypt.py <password>

import PyPDF2
import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")
# TODO: GET PASSWORD FROM COMMAND LINE
if len(sys.argv) == 2:
    # TODO: OS WALK FROM CURRENT DIRECTORY
    password = sys.argv[1]
    for foldername, subfolders, files in os.walk("."):
        for file in files:
            # TODO: FIND PDFS
            if file.endswith(".pdf"):
                filename = os.path.abspath(os.path.join(foldername, file))
                logging.info("Reading file: " + str(filename))
                file = open(filename, "rb")
                pdfFileReader = PyPDF2.PdfFileReader(file)
                if not pdfFileReader.isEncrypted:
                    pdfFileWriter = PyPDF2.PdfFileWriter()
                    # TODO: COPY EVERY PAGE
                    for pageNum in range(pdfFileReader.numPages):
                        pdfFileWriter.addPage(pdfFileReader.getPage(pageNum))
                        # TODO: ENCRYPT EACH PDF FILE
                        pdfFileWriter.encrypt(password)
                        logging.info("File " + str(filename) +
                                     " has been successfully encrypted")
                        # TODO: SAVE FILE
                        name = (os.path.basename(filename)).split(".")[0]
                        newname = os.path.join(
                            foldername, "encrypted_" + name + ".pdf")
                        newname = os.path.abspath(newname)
                        resultPdf = open(newname, "wb")
                        pdfFileWriter.write(resultPdf)
                        logging.info(
                            "fFile has been renamed to: " + str(newname))
                        resultPdf.close()
                        file.close()
                        resultPdf = open(newname, "rb")
                        pdfFileReader = PyPDF2.PdfFileReader(resultPdf)
                        if pdfFileReader.decrypt(password):
                            # TODO: DELETES OLD FILE
                            os.unlink(filename)
                            logging.info("File " + str(filename) +
                                         " has been successfully deleted")
                        else:
                            # DELETE NEWLY ENCRYPTED FILE
                            os.unlink(newname)
                            logging.warning(
                                "Problem while encrypting file: " + str(filename))
                            file.close()

                else:
                    logging.error("Password required")

# usage python pdf_paranoia_decrypt.pdf <password>


logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

if len(sys.argv) == 2:
    password = sys.argv[1]
    # TODO:loop through all pdfs
    for foldername, subfolders, files in os.walk("."):
        for filename in files:
            if filename.endswith(".pdf"):
                    # TODO: decrypt if encrypted
                filename = os.path.join(foldername, filename)
                filename = os.path.abspath(filename)
                fileObj = open(filename, "rb")
                pdfFileRead = PyPDF2.PdfFileReader(fileObj)
                if not pdfFileRead.isEncrypted:
                    logging.warning(
                        "This file: " + str(filename) + " is not encrypted")
                    continue
                try:
                    pdfFileRead.decrypt(password)
                    logging.info("File: " + str(filename) +
                                 " was succes. decrypted")
                    fileObj.close()
                except Exception as err:
                    logging.error("File decryption failed: " + str(err))

                    # TODO:if failed decryption
                    # TODO:print error

else:
    logging.error("Password required")
