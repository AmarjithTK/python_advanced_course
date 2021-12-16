from flaskmium import osmium
from flask import request,redirect,render_template
from flaskmium.modules.usermodel import user_loader
from flask_login import login_user,logout_user




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
        return render_template('exception.html', heading='Invalid credentials')
        
@osmium.route('/logout',methods=['POST'])
def logout():
    logout_user()
    return render_template('exception.html',heading='Logged out successfully')


@osmium.route('/shutdown',methods=['POST'])
def getattribute():
    data = request.form.get('data-username')
    print(f"data id is {data}",flush=True)
    return redirect('/dashboard')    