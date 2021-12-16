
from flask import request,redirect,render_template
from flaskmium import osmium
from flaskmium.models.constants import userdata
from flaskmium.models.usermodel import user_loader
from flask_login import login_user,login_required,logout_user,current_user

# print([current_user,'this workks'],flush=True)



@osmium.route('/',methods=['GET'])
def LoginPage():
    # print([loggedUser.is_authenticated,'from loginpage'],flush=True)

    if  current_user.is_authenticated == True:
        return redirect('/dashboard',code=302)

    # creds = {username:request.form['username'],password:request.form['password']}
    # return render_template('index.html',title="hello world",userdata = userdata)
    # elif(request.method == 'GET'):
    return render_template("login.html")

@osmium.route('/',methods=['POST'])
def login():
    user = request.form.get('username')
    print(user)
    password = request.form.get('password')
    if user == 'amarjith@gmail.com' and password == '123456':
        UserloggedIn = user_loader(user)
        login_user(UserloggedIn,remember=True)
        # print([current_user,'from login thing',current_user.is_authenticated],flush=True)

        return redirect('/dashboard',code=302)
    else:
        return '<h1>wrong cred</h1>'

@osmium.route('/dashboard',methods=['GET'])
@login_required
def DashPage():
    print('enter getresult', flush=True)
    return render_template('index.html',title="hello world",userdata = userdata)

@osmium.route('/logout',methods=['POST'])
def logout():
    logout_user()
    return render_template('exception.html',heading='Logged out successfully')



@osmium.errorhandler(404)
def nopage(e):
    return render_template('exception.html',heading = 'page not found')    

@osmium.errorhandler(401)
def unauth(e):
    return render_template('exception.html',heading='Unauthorised request')