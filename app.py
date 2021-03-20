from flask import Flask
from query import runQuery
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<username>', methods=['GET'])
def get_mentor_profile(username):
    res = runQuery(username)
    if res:
        return "Exists!"
    else:
        return "Does Not Exist"