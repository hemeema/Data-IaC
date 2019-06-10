#!/bin/bash
#Turn off monitor to avoid multiple calls to this script
sudo mkdir /home/nifi/JDBC/
sudo chown -R nifi:hadoop /home/nifi/JDBC/
sudo mv /tmp/ngdbc-2.1.2.jar /home/nifi/JDBC/ngdbc-2.1.2.jar
sudo systemctl stop nifi-connectors.path
sudo systemctl disable nifi-connectors.path
sudo rm /etc/systemd/system/nifi-connectors*
