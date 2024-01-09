#We have to make this class as an abstract class wherein the child classes of it should override the methods present in this 
#parent class
import abc
class Medical_doc(metaclass=abc.ABCMeta):
    def __init__(self,text):# A constructor which will take a text from the pytesseract
        self.text=text
    
    @abc.abstractmethod
    def parse(text):
        pass