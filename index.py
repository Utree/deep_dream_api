from bottle import route, run

@route('/hello')
def index():
    return "Hello"

run(host='0.0.0.0', port=8080)
