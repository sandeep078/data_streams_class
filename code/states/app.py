
# A very simple Bottle Hello World app for you to get started with...
from bottle import run, default_app, route, template, static_file
import get_weather

@route('/')
def hello_world():
    return 'Hello from Bottle!'

@route('/map')
def map_route():
    list = get_weather.get_weather_list()
    states = []
    reds = []
    greens = []
    blues = []
    for item in list:
        states.append(item)
        blues.append(list[item]['humidity']*2)
        greens.append(0)
        reds.append(int(list[item]['temp']-273)*5)
    return template("map", states = states, reds = reds, greens = greens, blues = blues)

@route('/sample0')
def sample_route():
    return template("sample0")

@route('/sample')
def sample_route():
    list = get_weather.get_weather_list()
    i = 10
    states = ''
    colors = ''
    for item in list:
        states = states + '"' + item + '",'
        colors = colors + '' + str(i) + ','
        i = i + 4
    return template("sample",states=states,colors=colors)

@route("/static/<filename:path>")
def static(filename):
    return static_file(filename, root="./Static")

# application = default_app()
run(host='localhost', port=8080)
