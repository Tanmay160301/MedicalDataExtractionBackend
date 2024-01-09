from generic_parser import Medical_doc
import re

class Prescription_Parser(Medical_doc):
    def __init__(self,text):
        self.text=text

    def parse(self):
        #This function will return a json object
        return {
            'patient_name':self.get_name(),
            'patient_address':self.get_address(),
            'medicines':self.get_medicines(),
            'directions':self.get_directions(),
            'Refill':self.get_refill()
        }

    def get_name(self):
        pattern="Name:(.*)Date"
        matches=re.findall(pattern,self.text)
        if len(matches)>0:
            return matches[0].strip()

    def get_address(self):
        pattern="Address:(.*)\n"
        matches=re.findall(pattern,self.text)
        if(len(matches)>0):
            return matches[0].strip()

    def get_medicines(self):
        pattern="Address:[^\n]*(.*)Directions"
        matches=re.findall(pattern,self.text,flags=re.DOTALL)
        if(len(matches)>0):
            return matches[0].strip()

    def get_directions(self):
        pattern="Directions:\n(.*)Refill"
        matches=re.findall(pattern,self.text,flags=re.DOTALL)
        
        if(len(matches)>0):
            return matches[0].strip()

    def get_refill(self):
        pattern="Refill:(.*)"
        matches=re.findall(pattern,self.text)
        if(len(matches)>0):
            return matches[0].strip()
        

if __name__=='__main__':
    text='''
    Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-111-2222

    Name: Marta Sharapova Date: 5/11/2022

    Address: 9 tennis court, new Russia, DC

    Prednisone 20 mg
    Lialda 2.4 gram

    Directions:

    Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month

    Refill: 2 times
    '''
    a=Prescription_Parser(text)
    print(a.get_name())
    print(a.get_address())
    print(a.get_medicines())
    print(a.parse())
