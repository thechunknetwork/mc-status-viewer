import mcstatus, yaml, time

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
        status.Update()

time.sleep(2)

for category in data:
    print category
    for server in data[category]:
        print server
        status = data[category][server]
        print "available: " + str(status.available)
        print str(status.num_players_online) + "/" + str(status.max_players_online)
