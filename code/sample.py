from bottle import route, run, template

@route('/hello/<name>')
def get_hello(name):
    name = name.upper()
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/goodbye/<name>')
def get_goodbye(name):
    name = name.upper()
    return template('<b>If you really must leave, goodbye {{name}}!</b>!', name=name)

run(host='localhost', port=8080)
