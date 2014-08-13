#!/bin/bash
sudo ifconfig $1 down
sudo start network-manager
