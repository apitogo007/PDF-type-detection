import os
import PyPDF2 as pyPdf
from decimal import Decimal

def pdf_resolution(input_dir, input, page):

    page0 = page

    if '/XObject' in page0['/Resources']:
        size_dpi = []
        xObject = page0['/Resources']['/XObject'].getObject()

        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                sizeW = (xObject[obj]['/Width'])
                sizeH = (xObject[obj]['/Height'])
                pt_ppi = 0.01389
                width_pt = float(page0.mediaBox.getWidth())* pt_ppi
                height_pt = float(page0.mediaBox.getHeight())* pt_ppi

                # print(sizeW, ' x ', sizeH)
                # print(width_pt, ' x ',  height_pt)

                ppiw = (sizeW / width_pt)
                ppih = (sizeH / height_pt)

                roundw = (Decimal(ppiw)).quantize(Decimal('10'))
                roundh = (Decimal(ppih)).quantize(Decimal('10'))
                # print(roundw, ' x ', roundh)

                # print(input_dir, file, ' - W x H: ', sizeW,' x ', sizeH, ' - DPI: ', str(roundw),' x ',str(roundh))
                temp_output_tuple = (sizeW, sizeH, str(roundw), str(roundh))
                size_dpi.append(temp_output_tuple)


            else:
                print(input_dir, file, ' - DPI: ', 'No image found.')

        return (size_dpi)

if __name__ == '__main__':

    inpputpath = ("D:\\_TestBank\\_Package\\Python\\_MyProjects\\PDF_code\\_Temp")
    # pdf_type(inpputpath)

    for file in os.listdir(inpputpath):
        if file.endswith('.pdf'):
            # print(os.path.join(path, file))
            PDF_open = open(inpputpath +'/'+file,'rb')
            pdfReader = pyPdf.PdfFileReader(PDF_open)

            result = pdf_resolution(inpputpath, pdfReader)


            print(inpputpath, file, result)