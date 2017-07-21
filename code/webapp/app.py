from bottle import route, run, template
import requests

@route('/example')
def get_example():
   rows = [
       ["first","second",5],
       [1,2,5],
       ['a','b',6],
       ['n','b',7],
       ['m','b',8],
       ['k','b',9]
   ]
   return template('make_table.tpl', rows=rows)

@route('/')
def get_index():
    stream="beta"
    #return template('<b>Hello {{name}}</b>!', name=name)
    url = "http://drdelozier.pythonanywhere.com/stream/query/"
    payload = {
        'userid': 0,
        'city': 0,
        'state': 0,
        'lat': 0,
        'lon': 0,
        'temp': 0,
        'humidity': 0,
        'light': 0,
        'outdoors': 0,
    }
    response = requests.get(url + stream)
    #print(response.status_code)
    #print(response.url)
    #print(response.text)
    data = response.json()
    data = data['result']
    for key in payload.keys():
        data = [item for item in data if key in item]
    print(data)

    return template('make_dict_table.tpl', header=payload.keys(), rows=data)

run(host='localhost', port=8080, debug=True)

