from bottle import route, run, debug, template, request, response, default_app
import time
import pickle

data=[]

@route('/stream/store/<name>', method='GET')
def store(name):
    item = dict(request.query)
    item['name'] = name
    item['time'] = int(time.time())
    data.append(item)
    with open("/home/drdelozier/mysite/data.pkl","wb") as f:
        pickle.dump(data, f)
    return str(item)

@route('/stream/query/<name>', method='GET')
def query(name):
    query = dict(request.query)
    start = None
    end = None
    query_data = [ item for item in data if item['name'] == name ]
    for name in query:
        if name == 'start':
            start = int(query['start'])
            query_data = [ item for item in query_data if item['time'] >= start ]
            continue
        if name == 'end':
            end = int(query['end'])
            query_data = [ item for item in query_data if item['time'] <= end ]
            continue
        target = query[name]
        query_data = [item for item in query_data
                           if name in item and target in item[name] ]
    return str(query_data)

try:
    with open("/home/drdelozier/mysite/data.pkl","rb") as f:
     data = pickle.load(f)
except:
    pass

debug(True)
application = default_app()
