import mcstatus, yaml, time, threading
from bottle import route, run, template, static_file

data = {}

with open('config.yml', 'r') as cfg_file:
    servers_config = yaml.load(cfg_file)

for category in servers_config:
    print category
    data[category] = {}
    for server in servers_config[category]:
        print "- " + server + ": " + servers_config[category][server]
        ip = servers_config[category][server]
        status = mcstatus.McServer(ip.split("/")[0], int(ip.split("/")[1]))
        data[category][server] = status

def update_all():
    i = 0
    for category in data:
        d = 0.005
        for server in data[category]:
            i += 1
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
        return response

def schedule():
    threading.Timer(3, schedule).start()
    update_all()

@route('/status')
def index():
    return generate_json()

@route('/')
def server_static():
    return static_file('index.html', '..')

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root = '..')

schedule()
try:
    run(host='0.0.0.0', port=8080)
except KeyboardInterrupt:
    sys.exit(0)

