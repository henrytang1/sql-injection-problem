from flask import Flask, request
from query import loginQuery, existenceQuery
from dotenv import load_dotenv

app = Flask(__name__, static_folder='./webui/build', static_url_path='/')

app.config['DEBUG'] = True

load_dotenv()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/login')
def login():
    return app.send_static_file('index.html')

@app.route('/forgot')
def forgot():
    return app.send_static_file('index.html')

@app.route('/api/login', methods=['GET'])
def check_credentials():
    params = {}
    params['username'] = request.args.get('username')
    params['password'] = request.args.get('password')

    try:
        res = loginQuery(params)
    except Exception as e:
        return "Not Correct"

    if res != None:
        return res
    else:
        return "Not Correct"


@app.route('/api/exists', methods=['GET'])
def check_username():
    params = {'username': request.args.get('username')}
    try:
        res = existenceQuery(params)
    except Exception as e:
        return "Does Not Exist"
    
    if res:
        return "Exists"
    else:
        return "Does Not Exist"