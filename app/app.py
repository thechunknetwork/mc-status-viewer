from collections import OrderedDict
import mcstatus, yaml, time, threading
from bottle import route, run, template, static_file, error

data = {}
json_response = None

with open('config.yml', 'r') as cfg_file:
    servers_config = yaml.load(cfg_file)

c = 0.0

for category in servers_config:
    print category
    data[category] = {}
    for server in servers_config[category]:
        print "- " + server + ": " + servers_config[category][server]
        ip = servers_config[category][server]
        status = mcstatus.McServer(ip.split("/")[0], int(ip.split("/")[1]))
        c += 1
        data[category][server] = status

def update_all():
#    i = 0.0
    for category in data:
#        d = 5.0 / c
        for server in data[category]:
#            i += 1.0
            status = data[category][server]
            threading.Thread(target=lambda: status.Update()).start()

def generate_json():
    alive = "alive"
    dead = "dead"
    response = {}
    response[alive] = {}
    response[dead] = {}
    for category in data:
        response[alive][category] = {}
        response[dead][category] = []
        for server in data[category]:
            status = data[category][server]
            if status.available:
                response[alive][category][server] = str(status.num_players_online) + "/" + str(status.max_players_online)
            else:
                response[dead][category].append(server)
        response[alive][category] = OrderedDict(sorted(response[alive][category].items(), key=lambda t: t[0]))
        response[dead][category].sort()
        if len(response[alive][category]) == 0:
            del response[alive][category]
        if len(response[dead][category]) == 0:
            del response[dead][category]
    response[alive] = OrderedDict(sorted(response[alive].items(), key=lambda t: t[0]))
    response[dead] = OrderedDict(sorted(response[dead].items(), key=lambda t: t[0]))
    return response

def schedule_update():
    threading.Timer(5, schedule_update).start()
    update_all()

def schedule_json():
    threading.Timer(1.5, schedule_json).start()
    global json_response
    json_response = generate_json()

@route('/status')
def index():
    return json_response

@route('/')
def server_static():
    return static_file('index.html', '..')

@error(404)
def error404(error):
    return static_file('404.html', '..')

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root = '..')

schedule_update()
schedule_json()

try:
    run(host='localhost', port=8080)
except KeyboardInterrupt:
    sys.exit(0)
