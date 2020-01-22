from PyPDF2 import PdfFileMerger
import glob                                     

pdf_files = glob.glob("./*.pdf")                    # read pdf files based off file extension using glob
# print (pdf_files)                                 # print pdf_files list

output_pdf = ("PDF-Output.pdf")                     # outputs the file as "PDF-Output.pdf"
merger = PdfFileMerger()                            # the PdfFileMerger() function is iterated to the merger object in order to be called later

for pdf in pdf_files:
    merger.append(open(pdf, "rb"))
   
with open (output_pdf, "wb") as fout:
    merger.write(fout)

print ("\nPDF Files have been successfully merged.")
