#!/bin/bash
# $1 : interface network
# $2 : ad hoc name
# $3 : ad hoc frequency
# $4 : ip address in new network
# $5 : netmask of network
sudo stop network-manager
sudo ifconfig $1 down
sudo iw $1 set type ibss
sudo ifconfig $1 up
sudo iw $1 ibss join $2 $3
sudo ifconfig $1 $4 netmask $5
sudo iw $1 link
sudo iw $1 info
sudo ifconfig $1
