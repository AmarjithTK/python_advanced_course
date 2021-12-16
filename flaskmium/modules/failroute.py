
from flask import render_template
from flaskmium import osmium

# print([current_user,'this workks'],flush=True)

@osmium.errorhandler(404)
def nopage(e):
    return render_template('exception.html',heading = 'page not found')    

@osmium.errorhandler(401)
def unauth(e):
    return render_template('exception.html',heading='Unauthorised request')


