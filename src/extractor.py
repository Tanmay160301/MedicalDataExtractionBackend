#This code will extract the data from the pdf
from xml.dom.minidom import Document
from pdf2image import convert_from_path
import pytesseract
import util
from prescription_parser import Prescription_Parser
from patient_detail_parser import patient_detail_parser

from PIL import Image

POPPLER_PATH=r'C:\poppler-22.04.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract(file_path,file_format):
    #step 1 Extract text from the document using pytesseract
    pages=convert_from_path(file_path,poppler_path=POPPLER_PATH)

    document=''
    if(len(pages)>0):
        processed_img=util.preprocess_img(pages[0])#First will get the preprocessed image and then will send that to pytesseract
        text=pytesseract.image_to_string(processed_img,lang='eng')
        document='\n'+text

# #Step 2: The condition written below will extract the information from the document
    if file_format=='prescription':
        extracted_data=Prescription_Parser(document).parse()
    elif file_format=='patient_details':
        extracted_data=patient_detail_parser(document).parse()
    else:
        raise Exception(f"File Format not supported {file_format}")
    
    return extracted_data


if __name__=='__main__':
    data=extract('E:\Projects\Backend\docs\prescription\pre_1.pdf','prescription')
    print(data)
