from flask import Flask, render_template 
from flask import request

from storage import UserStore


app = Flask(__name__) 

@app.route('/')
def hello_world():
    return 'Hello World' 

default_login = "Hacker"
default_password = "11"
  
@app.route('/login')
def login(): # http://127.0.0.1:5000/login?username=Hacker&password=11
    username = request.args.get('username')
    password = request.args.get('password')
   # if default_login == username:
    # if default_password == password: 
    #         return "True"
    #return "False"
    user = "Klim Sytnyk"
    return render_template('login.html',name = user)

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

