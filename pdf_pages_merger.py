from pypdf import PdfMerger as pm

merg = pm()

a = open("pdf files - Copy\\329918_2023.pdf","+rb")
b = open("pdf files - Copy\\amishaPAN.pdf","+rb")
c = open("pdf files - Copy\\imp.pdf","+rb")
d = open("pdf files - Copy\\Syllabus IPU essed (1)-pages-9,28-50.pdf","+rb")

print("merging pdfs....")

merg.append(fileobj=a)

merg.append(fileobj=b)

merg.append(fileobj=c, pages=(0,2))

merg.append(fileobj=d, pages=(0,4))

output = open("output_doc.pdf","wb")
merg.write(output)

merg.close()
output.close()

print("pdf's merged successfully")

#code completed successfully