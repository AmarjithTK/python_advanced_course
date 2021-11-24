from flask.views import MethodView
from wtforms import Form,StringField,SubmitField
from flask import Flask,render_template,request
from flatmate.main import FlatmateBackend
import os

myapp = Flask(__name__)




class HomePage(MethodView):
    def get(self):
        return render_template('index.html')
    

class BillFormPage(MethodView):
    
    def get(self):

        bill_form = BillForm()
        return render_template('bill.html',billform=bill_form)
        # return render_template()

    


class ResultsPage(MethodView):


    def post(self):
        billdata = BillForm(request.form)

        amount = billdata.amount.data
        period = billdata.period.data
        name1 = billdata.name1.data
        name2= billdata.name2.data
        days1 = billdata.days1.data
        days2 = billdata.days2.data

        flatmatebackend = FlatmateBackend(amount,period)
        filepath = flatmatebackend.generate(name1,name2, days1, days2)

        return render_template('result.html',filepath=filepath)



class BillForm(Form):

    amount = StringField('Enter the amount of bill :')
    
    period = StringField('Enter the bill Period :')

    name1 = StringField('Enter the name of of flatmate1 : ')
    days1 = StringField('Enter the days in house of flatmate1 :')

    name2 = StringField('Enter the name of of flatmate2 : ')
    days2 = StringField('Enter the days in house of flatmate2 :')

    submit = SubmitField('Calculate')

myapp.add_url_rule('/',view_func=HomePage.as_view('home_page'))
myapp.add_url_rule('/bill',view_func=BillFormPage.as_view('bill_form_page'))
myapp.add_url_rule('/results' , view_func=ResultsPage.as_view('results_page'))


myapp.run(debug=True)