
from flask import request,redirect,render_template

from flask import Blueprint




userdata = {

    "name":'startship',
    "status":'running',
    "uptime":50.0,
    "os":'Ubuntu Mate',
    "hostname":'Flatter',   

}


osmiumRoutes = Blueprint('osmiumRoutes',__name__)

@osmiumRoutes.route('/',methods=['GET','POST'])
def LoginPage():
    if(request.method == 'POST'):
        # creds = {username:request.form['username'],password:request.form['password']}
        user = request.form.get('username')
        password = request.form.get('password')
        if user == 'amar@gmail.com' and password == '123456':
            return redirect('/dashboard',code=302)

    elif(request.method == 'GET'):
        return render_template("login.html")


@osmiumRoutes.route('/dashboard',methods=['GET'])
def DashPage():
    print('enter getresult', flush=True)
    return render_template('index.html',title="hello world",userdata = userdata)
