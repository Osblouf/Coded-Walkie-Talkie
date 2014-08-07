# This example shows how we use the network

# Last modification : Loic
from net_class import Net_manager

def r_func(data):
	print 'Received : ', data

not_get_all = True
ip_list = list()

while not_get_all:
	ip = raw_input()
	if ip == '':
		not_get_all = False

	else:
		ip_list.append(ip)

net = Net_manager(15000, r_func)
for ip in ip_list:
	net.Connect_to(ip)

net.Start_listening()
	
not_get_all = True
while not_get_all:
	message = raw_input()

	if message == 'stop':
		not_get_all = False
	else:
		net.Send_to_all(message)

net.Close()


