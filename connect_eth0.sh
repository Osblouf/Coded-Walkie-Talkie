#!/bin/bash
commande='connect'
comman=$1
if [ "$comman" == "$commande" ]; then
sudo stop network-manager
sudo ifconfig eth0 up
sudo ifconfig eth0 $2
else
sudo start network-manager
fi
exit
