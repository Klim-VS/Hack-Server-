from flask import Flask, render_template 
from flask import request

from storage import UserStore


app = Flask(__name__) 

@app.route('/')
def hello_world():
    return 'Hello World' 

default_login = "Hacker"
default_password = "11"
  
@app.route('/login', methods=['GET', 'POST'])
def login(): # http://127.0.0.1:5000/login?username=Hacker&password=11
    if request.method == 'GET':
            user = "Klim Sytnyk"
            return render_template('login.html',name = user)
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if default_login == username:
         if default_password == password: 
            return render_template('success.html')
        return render_template('unsuccess.html')

@app.route('/success')
def success(): 

    return render_template('success.html')

@app.route('/fail')
def fail(): 

    return render_template('unsuccess.html')

user_store=UserStore()
@app.route('/register')
def register():
    username = request.args.get('username')
    password = request.args.get('password')
    user_store.add(username,password)
    print(user_store.get(username)) #prints keys
    return 'You can sign up'

@app.route('/data')
def data():
    
    return 'Pincode'

if __name__ == '__main__':
    app.run()

