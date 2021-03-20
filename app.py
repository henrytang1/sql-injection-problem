from flask import Flask
from query import runQuery
from dotenv import load_dotenv
from query import getConn

app = Flask(__name__)
app.config['DEBUG'] = True

load_dotenv()

pool = getConn()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<username>', methods=['GET'])
def get_mentor_profile(username):
    try:
        res = runQuery(username, pool)
    except Exception as e:
        return "Database error"

    if res:
        return "Exists!"
    else:
        return "Does Not Exist"