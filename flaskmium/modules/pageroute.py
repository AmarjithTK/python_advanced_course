
from flaskmium import osmium
from flask import request,render_template,redirect
from flask_login import current_user,login_required
from flaskmium.modules.constants import userdata


@osmium.route('/',methods=['GET'])
def LoginPage():
    # print([loggedUser.is_authenticated,'from loginpage'],flush=True)

    if current_user.is_authenticated == True:
        return redirect('/dashboard',code=302)

    # creds = {username:request.form['username'],password:request.form['password']}
    # return render_template('index.html',title="hello world",userdata = userdata)
    # elif(request.method == 'GET'):
    return render_template("login.html")


@osmium.route('/dashboard',methods=['GET'])
@login_required
def DashPage():
    print('enter getresult', flush=True)
    return render_template('index.html',title="hello world",userdata = userdata)