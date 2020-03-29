# Not Completed

from PyPDF2 import PdfFileReader, PdfFileWriter                # From the module "PyPDF2" import the object called "PdfFileReader"

pdfFileObject = open("blankform.pdf", "rb")        # This program will only work on PDF files with only text
pdfReader = PdfFileReader(pdfFileObject)           # Using the PdfFileReader() function, we were able to call the pdfFileObject argument.

print
print ("Number of Page in pdf: \n" + str(pdfReader.numPages))                      # print the total number of pages in the pdf file

print("_"*20)

formField = pdfReader.getFormTextFields()

print (formField)                                           # This is a dictionary datatype
print (formField.get("Height Formatted Field"))             # Grab text in the formField called "Height Formatted Field" = 150

height = {"Height Formatted Fieldbn  ": "160"}                  # Dictionary "Height Formatted Field" gets updated to "160"

formField.update(height)                                    # in the dictionary formField, "Height Formatted Field" gets updated
print ("_"*20)
print (formField)                                           # This is a dictionary datatype
print (formField.get("Height Formatted Field"))             # Grab text in the formField called "Height Formatted Field" = 160 (whatever the update was)

print ()

#pageObj = pdfReader.getPage(0)
#print()

#extractText = (pageObj.extractText)()              # Takes the function of pageObj.extractText() and iterate it to the variable extractText
#print (extractText)                             # Replace the word "Simple" with "

#print(pageObj.extractText)                    # Extract text from pdf file. Only works for pdf file with only text
#print()
