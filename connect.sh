#!/bin/bash
sudo stop network-manager
sudo ifconfig eth0 up
sudo ifconfig $1
