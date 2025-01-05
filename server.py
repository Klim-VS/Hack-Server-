from flask import Flask 

app = Flask(__name__) 

@app.route('/')
def hello_world():
    return 'Hello World' 

@app.route('/login')
def login():
    return 'You can login'

@app.route('/register')
def register():
    
    return 'You can sign up'

@app.route('/data')
def data():
    
    return 'Pincode'

if __name__ == '__main__':
    app.run()

