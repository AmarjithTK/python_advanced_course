
import webbrowser
import os


class Bill:
    def __init__(self,amount,period):
        self.amount= amount
        self.period = period


class Flatmate:

    def __init__(self,name,days_in_house):
        self.name=name
        self.days_in_house = days_in_house

    def pays(self,bill,flatmate2):
        self.weight = (bill.amount) / (self.days_in_house+flatmate2.days_in_house)
        amount_to_pay = f"  {self.days_in_house * self.weight} rs"  # Gets the bill amount and generate a split between two class mates
        return amount_to_pay



    