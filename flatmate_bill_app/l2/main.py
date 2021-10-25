
from flat import Flatmate,Bill
from results import PDF,Uploader


pdfbool_input = False
pdfopenbool_input = False
pdfname_input = 'report.pdf'
amount_input = input('Hey user , Enter the amount of bill : ')
period_input = input('\nEnter the period of bill : ')
name1_input = input('Who is the first flatmate : ')
days1_input = input(f'How many days did {name1_input} stayed in house : ')
name2_input = input('what is the name of other flatmate : ')
days2_input = input(f'How many days did {name2_input} stayed in house : ')
pdfbool_input = input(" Do you want a pdf report of this bill split : ")
if pdfbool_input == True or pdfbool_input.upper() == 'YES'  :
    pdfname_input = input("Enter the name of file to store pdf report :")
    pdfopenbool_input = input("Would you like to view the output pdf in browser automatically :")



bill_today = Bill(float(amount_input), period_input)

flatmate1 = Flatmate(name1_input, int(days1_input))
flatmate2 = Flatmate(name2_input, int(days2_input))
pdfgen = PDF(bill_today,flatmate1=flatmate1,flatmate2=flatmate2)
pdfgen.generate(filename = f'{pdfname_input}.pdf',show_bool= pdfopenbool_input)
uploader = Uploader(f'{pdfname_input}.pdf')
uploader.upload()

print(flatmate1.pays(bill_today,flatmate2),flatmate2.pays(bill_today,flatmate1))