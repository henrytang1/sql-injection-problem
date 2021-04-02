from flask import Flask, request, make_response, render_template
from query import loginQuery, existenceQuery
from dotenv import load_dotenv
import json
from datetime import datetime

app = Flask(__name__, static_folder='./webui/build', static_url_path='/', template_folder='.')

app.config['DEBUG'] = True

load_dotenv()

def update_times(query_times):
    now = datetime.now()
    now = (now-datetime(1970,1,1)).total_seconds()

    if query_times is None:
        query_times = []
    else:
        query_times = json.loads(query_times)

    acc_speed = True
    if len(query_times) >= 10:
        earliest = query_times[0]
        if now - earliest < 60:
            acc_speed = False
        query_times.pop(0)

    query_times.append(now)
    return acc_speed, query_times

@app.route('/')
@app.route('/login')
@app.route('/forgot')
def index():
    query_times = request.cookies.get('queryTimes')
    acc_speed, query_times = update_times(query_times)

    if not acc_speed:
        html = render_template('overload_requests.html')
        res = make_response(html)
        res.set_cookie('queryTimes', json.dumps(query_times))
        return html
    
    res = app.send_static_file('index.html')
    res.set_cookie('queryTimes', json.dumps(query_times))
    return res


@app.route('/api/login', methods=['GET'])
def check_credentials():
    query_times = request.cookies.get('queryTimes')
    acc_speed, query_times = update_times(query_times)
    print(acc_speed, query_times)

    if not acc_speed:
        response = make_response("Too many requests", 200)
        response.mimetype = "text/plain"
        response.set_cookie('queryTimes', json.dumps(query_times))
        return response

    params = {}
    params['username'] = request.args.get('username')
    params['password'] = request.args.get('password')

    try:
        res = loginQuery(params)
    except Exception as e:
        res = None

    if res == None:
        res = "Not Correct"
    response = make_response(res, 200)
    response.mimetype = "text/plain"
    response.set_cookie('queryTimes', json.dumps(query_times))
    return response
    # if res != None:
    #     return res
    # else:
    #     return "Not Correct"


@app.route('/api/exists', methods=['GET'])
def check_username():
    query_times = request.cookies.get('queryTimes')
    acc_speed, query_times = update_times(query_times)

    if not acc_speed:
        response = make_response("Too many requests", 200)
        response.mimetype = "text/plain"
        response.set_cookie('queryTimes', json.dumps(query_times))
        return response

    params = {'username': request.args.get('username')}
    try:
        res = existenceQuery(params)
    except Exception as e:
        res = None
    
    if res == None:
        res = "Does Not Exist"
    elif res == False:
        res = "Does Not Exist"
    else:
        res = "Exists"

    response = make_response(res, 200)
    response.mimetype = "text/plain"
    response.set_cookie('queryTimes', json.dumps(query_times))
    return response
    
    # if res:
    #     return "Exists"
    # else:
    #     return "Does Not Exist"