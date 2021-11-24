This is flatmate bill app

Title : Flatmate bill
Description : An app which receives input from user . App collects days spent by individual roommates in the house and using a formula calculates the bill amount that each roommate has to pay depending upon the days individual roommates where at the house. This app will also generate the output amount in a nicely formatted pdf output format and also uploades the output to a cloud service providerli
Date started : 22-10-21 


"""shortcut to find the objects classes to be created ?? look for nouns in description"""

objects : 

    Bill:
        amount:
        period:
    
    Flatmate:
        name:
        days_in_house:
        pays(bill.amount)

    PDFgenerator:
        filename:  # how can you miss that one
        generate(flatmate1,flatemate2,bill_amount)


===== object oriented programming language principle ======

' Extend a class don't modify '
' Class should have only one responsibility '

Extend a class with a derived class . Don't modify if it already fullfill the requirements

Pdfgenerator class "only" generate pdf
flatmate class "only" calculate each flatmate shares

