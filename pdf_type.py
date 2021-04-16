import os
import PyPDF2 as pyPdf

import pdf_dpi

# # working
# pdf = pyPdf.PdfFileReader(open("D:\\_TestBank\\_Package\\Python\\_MyProjects\\PDF_code\\144023.140330812806912.40836.2013-014_page_1.pdf", "rb"))
# pages_num=list(pdf.getPage(0)['/Resources']['/ProcSet']) # Process all the objects.
# print(pages_num)
# pdf_object=(pdf.resolvedObjects.items())

def get_pdf_res(input_dir, input, page):
    return pdf_dpi.pdf_resolution(input_dir, input, page)

def pdf_type(input_dir, input_file):
    page_prop = []
    page0 = (input_file.getPage(0))
    pdfImg = ['/PDF', '/Text', '/ImageB', '/ImageC', '/ImageI']
    pdfImgHiddenText1 = ['/PDF', '/Text', '/ImageC', '/ImageB']
    pdfImgHiddenText2 = ['/PDF', '/Text', '/ImageB']
    pdfImgHiddenText3 = ['/PDF', '/ImageC', '/ImageI']
    pdfTxtCrp1 = ['/PDF', '/Text', '/ImageC', '/ImageI']
    pdfTxtCrp2 = ['/PDF', '/Text', '/ImageC']
    pdfTxt = ['/PDF', '/Text']

    if '/ProcSet' in page0['/Resources']:
        xObject1 = page0['/Resources']['/ProcSet'].getObject()

        # print(pdfI)
        if pdfImg == xObject1:
            # print(input_dir, file, " - PDF Type: ", str(xObject1))
            pg_res = get_pdf_res(input_dir, file, page0)
            for ctr in pg_res:

                # pg=(f" W {ctr[0]} H {ctr[1]}, Error: {ctr[2]} DPI {ctr[3]} ' x ' {ctr[4]}")
                page_prop = (f"PDF Image; Dimension - W x H: {ctr[0]} x {ctr[1]}; DPI: {ctr[2]}")

        elif pdfTxtCrp1 == xObject1:
            page_prop = ("PDF Normal with Crop Image")
            # print(input_dir, file, " - PDF Type: ", str(xObject1))

        elif pdfTxtCrp2 == xObject1:
            page_prop = ("PDF Normal with Crop Image")
            # print(input_dir, file, " - PDF Type: ", str(xObject1))

        elif pdfImgHiddenText1 == xObject1:
            page_prop = ("PDF Image with Hidden Text")
            # print(input_dir, file, " - PDF Type: ", str(xObject1))

        elif pdfImgHiddenText2 == xObject1:
            page_prop = ("PDF Image with Hidden Text")

        elif pdfImgHiddenText3 == xObject1:
            page_prop = ("PDF Image with Hidden Text")

        elif pdfTxt == xObject1:
            page_prop = ("PDF Normal")
            # print(input_dir, file, " - PDF Type: ", str(xObject1))

        # else:
        #     page_prop = ("Unable to identify!")

    else:
        page_prop = ("Unable to identify!")

    return (page_prop)

if __name__ == '__main__':

    inpputpath = (r"D:\_TestBank\_Package\Python\_MyProjects\PDF_code\_Temp\_misc")
    # pdf_type(inpputpath)

    for file in os.listdir(inpputpath):
        if file.endswith('.pdf'):
            # print(os.path.join(path, file))
            PDF_open = open(inpputpath +'/'+file,'rb')
            pdfReader = pyPdf.PdfFileReader(PDF_open)

            result = pdf_type(inpputpath, pdfReader)


            print(inpputpath + '\\' + file, result)