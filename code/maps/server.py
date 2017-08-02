from bottle import route, run, template
from bottle import static_file
import json
import get_stream

@route("/")
@route("/index")
def index():
    return template("""
        <b>
        An example weather server.
        </b>
    """)

@route("/table")
def temperature():
    data = get_stream.get_stream_data()
    print(data)
    return template("""
    <table>
    %for item in data:
        <tr>
        <td>
            {{item['lat']}}
        </td>
        <td>
            {{item['lon']}}
        </td>
        <td>
            {{item['temperature']}}
        </td>
        <td>
            {{item['windspeed']}}
        </td>
        <td>
            {{item['humidity']}}
        </td>
        <td>
            {{item['clouds']}}
        </td>
        </tr>
    %end
    </table>
    """, data=data)

@route("/graph")
def graph():
    data = get_stream.get_stream_data()
    return template("scatter_graph", data=data)

@route("/map")
def example_map():
    data = get_stream.get_stream_data()
    return template("example_map", data=data)

@route("/static/<filename:path>")
def static(filename):
    return static_file(filename, root="./Static")

run(host='localhost', port=8080, debug=True)