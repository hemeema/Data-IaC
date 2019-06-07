#!/bin/bash
#Turn off monitor to avoid multiple calls to this script
sudo mkdir /home/nifi/JDBC/
sudo chown -R nifi:hadoop /home/nifi/JDBC/
sudo /usr/local/bin/aws s3api get-object --bucket big-data-dependencies --key jars/ngdbc-2.1.2.jar /home/nifi/JDBC/ngdbc-2.1.2.jar
sudo systemctl stop nifi-connectors.path
sudo systemctl disable nifi-connectors.path
sudo rm /etc/systemd/system/nifi-connectors*

