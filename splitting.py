import PyPDF2 as pdf
import math
import re
import time

string = re.compile(r"(\D+|\s)")

# The PDF file name.
while True:
    try:
        print()
        pdffile = input("Type the PDF file name here. (Include the \".pdf\" extension): ")
        print()
        with open(pdffile, "rb"):
            break
    except FileNotFoundError:
        print("\n" + "*"*50)
        print("File not found. Please, include the full path.")
        print("For example: C:/user/fernanda/anyname.pdf")
        print("*"*50 + "\n")
        continue


# New filenames you wish to split.
while True:
    print()
    filename = input("How would you like to name the new file? (NOTE: the name wouldn't have numbers or special characters) ")
    if string.fullmatch(filename) == None:
        print("\n" + "*"*50)
        print("ERROR. Please, include only letters.")
        print("The name will include number. For example. newpdf1(from 1 to 10) newpdf2(from 11 to 20) and so on.")
        print("*"*50 + "\n")
        continue
    else:
        break

# Number of pages you wish to split.
while True:
    try:
        print()
        split = int(input("How many pages do you need to split? "))
        break
    except ValueError:
        print("\n" + "*"*50)
        print("ERROR. Please, include only numbers.")
        print("*"*50 + "\n")
        continue

print("Processing... Wait until complete.")
time.sleep(2)

# Algorithm to process the file and split
with open(pdffile, "rb") as file:

    reader = pdf.PdfFileReader(file)

    nnn = 1

    #  Creating new pdf to add pages.
    newname = filename + str(nnn) + ".pdf"
    writer = pdf.PdfFileWriter()

    start = 0
    end = split

    for pages in range(math.ceil(reader.numPages/split)):

        try:
            for npages in range(start, end):
                # print(npages, end)

                writer.addPage(reader.getPage(npages))

                with open(newname, "wb") as new_file:
                    writer.write(new_file)

                
                # print(pages, newname, npages)

                if (npages == (end-1)):
                    nnn += 1
                    newname = filename + str(nnn) + ".pdf"
                    # print(newname + " adding")
                    writer = pdf.PdfFileWriter()
            
        except IndexError:
            break

        start += split  # 10, 20, 30
        end += split  # 20, 30, 40

print()
print("Done!" + "\n")