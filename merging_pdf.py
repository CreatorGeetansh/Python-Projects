from pypdf import PdfMerger

pdfs = ['pdf files/329918_2023.pdf','pdf files\\amishaPAN.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
print("pdf's merged successfully")
#code in hold.....