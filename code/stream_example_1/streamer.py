from bottle import route, request, response, template, run

@route('/input')
def input():
    x = dict(request.query.decode())
    print(x)
    return template('<b>Hello {{name}}</b>!', name="Bob")

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
