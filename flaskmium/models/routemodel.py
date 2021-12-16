
from flask import request,redirect,render_template
from flaskmium import osmium
from flaskmium.models.constants import userdata
from flaskmium.models.usermodel import user_loader
from flask_login import login_user,login_required,logout_user



@osmium.route('/',methods=['GET','POST'])
def LoginPage():
    # creds = {username:request.form['username'],password:request.form['password']}
    # return render_template('index.html',title="hello world",userdata = userdata)
    # elif(request.method == 'GET'):
    return render_template("login.html")

@osmium.route('/',methods=['POST'])
def login():
    user = request.form.get('username')
    password = request.form.get('password')
    if user == 'amar@gmail.com' and password == '123456':
        UserloggedIn = user_loader(user)
        login_user(UserloggedIn)
        return redirect('/dashboard',code=302)


@osmium.route('/dashboard',methods=['GET'])
@login_required
def DashPage():
    print('enter getresult', flush=True)
    return render_template('index.html',title="hello world",userdata = userdata)

@osmium.route('/logout')
def logout():
    logout_user()
    return 'Logged out'