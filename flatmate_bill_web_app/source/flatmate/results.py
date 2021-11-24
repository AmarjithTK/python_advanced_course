from filestack import Client
from fpdf import FPDF

import os


class PDF:

    def __init__(self,bill,flatmate1,flatmate2):
        self.bill = bill
        self.flatmate1 = flatmate1
        self.flatmate2 = flatmate2
      

    def generate(self,filename):
        print('this is 555 - ')

        pdf = FPDF(orientation='p',unit='pt')
        pdf.add_page()

        pdf.set_font('Arial')
        pdf.set_fill_color(r=26,g=56,b=256)
        pdf.set_title('Flatmate APP')
        pdf.set_text_color(r=44,g=35,b=250)

        pdf.image('resources/brave.png',link='l1/brave.png',h=20,x=40,w=20,y=28)
        pdf.ln(10)
        pdf.r_margin
        pdf.set_x(70)
        pdf.set_font_size(10)

        pdf.cell(w=0,h=0,txt='Brave Developers',border=0,align='L',fill=0,ln=0)
        pdf.set_font_size(25)

        pdf.ln(50)
        pdf.cell(w=0,h=50,txt='Flatmate Bill split report',border=0,align='C',fill=0,ln=0)
        pdf.ln(100)
        pdf.set_font_size(14)

        pdf.cell(w=100,h=0,txt='Amount :',border=0,align='C',fill=0,ln=0)
        pdf.cell(w=150,h=0,txt=str(self.bill.amount),border=0,align='L',fill=0,ln=2)
        pdf.ln(10)

        pdf.cell(w=100,h=50,txt='Period :',border=0,align='C',fill=0,ln=0)
        pdf.cell(w=150,h=50,txt=str(self.bill.period),border=0,align='L',fill=0,ln=2)
        pdf.ln(5)


        pdf.cell(w=200,h=50,txt='Flatmate name',border=1,align='C',fill=0,ln=0)
        pdf.cell(w=350,h=50,txt='Amount to pay',border=1,align='C',fill=0,ln=2)
        pdf.ln(5)

        pdf.cell(w=200,h=50,txt=str(self.flatmate1.name),border=1,align='C',fill=0,ln=0)
        pdf.cell(w=350,h=50,txt=str(self.flatmate1.pays(self.bill,self.flatmate2)),border=1,align='C',fill=0,ln=2)
        pdf.ln(5)

        pdf.cell(w=200,h=50,txt=str(self.flatmate2.name),border=1,align='C',fill=0,ln=0)
        pdf.cell(w=350,h=50,txt=str(self.flatmate2.pays(self.bill,self.flatmate1)),border=1,align='C',fill=0,ln=0)

        print('this is - ')
        os.chdir('generated')
        pdf.output(name=f'{filename}')
        os.chdir('../')
        filepath =f"file://{os.path.realpath(f'generated/{filename}')}"
        # webbrowser.open(filepath)
        # print(filepath)
        return filepath


class Filesharer:
    def __init__(self,filename):
        self.filename =filename
    def upload(self):
        client = Client('AdjLC2cSOSxGpuW3jMLefz')
        filelink = client.upload(filepath=f'resources/{self.filename}')
        return filelink.url