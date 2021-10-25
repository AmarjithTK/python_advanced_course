from fpdf import FPDF
from pdfgen import PDF


class Bill:
    def __init__(self,amount,period):
        self.amount= amount
        self.period = period

"""
Bill is the blue print of the object which contains the information about the bill and the period of the bill

"""

class Flatmate:

    def __init__(self,name,days_in_house):
        self.name=name
        self.days_in_house = days_in_house

    def pays(self,bill,flatmate2):
        self.weight = (bill.amount) / (self.days_in_house+flatmate2.days_in_house)
        amount_to_pay = f"  {self.days_in_house * self.weight} rs"  # Gets the bill amount and generate a split between two class mates
        return amount_to_pay







amount_input = input('Hey user , Enter the amount of bill ! \t')
period_input = input('\nEnter the period of bill \t')
flatmate1_name_input = input('Enter the name of first flatmate')

type(amount_input)

'500.0' == 500.0

bill_today = Bill(float(amount_input), 'October 2021')

arun = Flatmate('arun', 20)
kiran = Flatmate('kiran', 29)
pdfgen = PDF(bill_today,flatmate1=arun,flatmate2=kiran,)
pdfgen.generate(filename = 'report.pdf')

print(arun.pays(bill_today,kiran),kiran.pays(bill_today,arun))