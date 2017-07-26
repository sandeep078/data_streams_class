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

# example page: https://developers.google.com/chart/interactive/docs/quick_start

@route('/chart')
def get_chart():
    pizzas = [
          {'type':'Mushrooms', 'count':3},
          {'type':'Onions', 'count':1},
          {'type':'Olives', 'count':1},
          {'type':'Zucchini', 'count':5},
          {'type':'Pepperoni', 'count':2},
          {'type':"Cheese",'count':10}
    ]
    return template("example_chart.tpl", rows=pizzas)
    #return template('make_dict_table.tpl', header=pizzas[0].keys(), rows=pizzas)

# example page: https://developers.google.com/chart/interactive/docs/gallery/linechart

@route('/line')
def get_chart():
    data = [          
        ['2004',  1000,      400],
        ['2005',  1170,      460],
        ['2006',  660,       1120],
        ['2007',  1030,      540],
        ['2008',  1000,      400],
        ['2009',  1170,      460],
        ['2010',  660,       1120],
        ['2011',  1030,      540],
        ['2012',  1000,      400],
        ['2013',  1170,      460],
        ['2014',  660,       1120],
        ['2015',  1030,      540]
    ]
    data = [ {'year':x, 'sales':y, 'expenses':z} for x,y,z in data ]
    return template("line_chart.tpl", rows=data)

@route('/weather')
def get_chart():
    #data = [ {'time':x, 'temp':y, 'humidity':z} for x,y,z in data ]
    stream="beta"
    #return template('<b>Hello {{name}}</b>!', name=name)
    url = "http://drdelozier.pythonanywhere.com/stream/query/"
    payload = {
        'time' : 0,
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
    data = response.json()
    data = data['result']
    for key in payload.keys():
        data = [item for item in data if key in item]
    print(data)
    data = [{'time':item['time'], 'temp':item['temp'], 'humidity':item['humidity']} for item in data]
    return template("weather_chart.tpl", rows=data)
    #return template('make_dict_table.tpl', header=['time','temp','humidity'], rows=data)

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

