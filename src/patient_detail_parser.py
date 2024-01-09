from generic_parser import Medical_doc
import re

class patient_detail_parser(Medical_doc):
    def __init__(self, text):
        self.text=text

    def parse(self):
        #This function will return a JSON object
        return{
            'Patient Name':self.get_name(),
            'Phone-Num':self.get_ph(),
            'Vaccination-status':self.get_vaccination_status(),
            'Medical Problems':self.get_medical_problems()
        }
    def get_name(self):
        pattern='Birth Date(.*?)\d'
        match=re.findall(pattern,self.text,re.DOTALL)
        list=match[0].split()
        index_remove=len(list)-1
        list.pop(index_remove)
        name=' '.join(list)
        return name

    def get_ph(self):
        pattern='(.*) Weight'#Here we havent implemented dot matches new line
        matches=re.findall(pattern,self.text)
        return matches[0].strip()

    def get_vaccination_status(self):
        pattern='\?(.*)List'
        matches=re.findall(pattern,self.text,flags=re.DOTALL)
        vaccine=matches[0].strip()
        return vaccine

    def get_medical_problems(self):
        pattern='Problems.*:(.*)'
        matches=re.findall(pattern,self.text,flags=re.DOTALL)
        medical_problems=matches[0].strip()
        return medical_problems


#def __init__=='main':
if __name__=='__main__':

    text='''
    47/12/2020

    Patient Medical Record

    Patient Information Birth Date
    Kathy Crawford May 6 1972
    (737) 988-0851 Weight
    9264 Ash Dr 95
    New York City, 10005 .
    United States Height:
    190
    In Case of Emergency
    m _ eee ee
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    Home phone United States
    (990) 375-4621
    Work phone
    Genera! Medical History

    Chicken Pox (Varicella):

    IMMUNE IMMUNE
    Have you had the Hepatitis B vaccination?

    No
    List any Medical Problems (asthma, seizures, headaches):
    Migrane
    '''
    print(text)

    a=patient_detail_parser(text)
    print(a.parse())
    print(a.get_name())
    print(a.get_medical_problems())
    print(a.get_ph())
