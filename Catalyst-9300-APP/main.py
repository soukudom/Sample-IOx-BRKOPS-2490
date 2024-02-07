from bottle import route, run

@route("/")
def hello():
    return "<b>Hello Cisco</b>!"

run(host='0.0.0.0', port=8000)

