import time
from flatmate.flat import Flatmate,Bill
from flatmate.results import PDF

# from datetime import datetime


# def FlatmateBackend(amount,period,name1,name2):

class FlatmateBackend:
    
    def __init__(self,amount,period):
        self.bill_today = Bill(float(amount), period)

    def generate(self,name1,name2,days1,days2):
        file_name = f"{name1}-{time.strftime('%I-%M-%p')}.pdf"


        flatmate1 = Flatmate(name1, int(days1))
        flatmate2 = Flatmate(name2, int(days2))
        pdfgen = PDF(self.bill_today,flatmate1=flatmate1,flatmate2=flatmate2)
        filepath = pdfgen.generate(filename = file_name)
        return filepath







# link = uploader.upload()

