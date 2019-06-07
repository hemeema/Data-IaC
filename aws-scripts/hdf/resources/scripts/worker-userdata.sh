#!/bin/bash
sudo sed -i 's/hostname=localhost/hostname=hostname/g' /etc/ambari-agent/conf/ambari-agent.ini
sudo systemctl enable nifi-connectors.path
sudo systemctl start nifi-connectors.path
#sudo systemctl enable nifi-flow.path
#sudo systemctl start nifi-flow.path
sudo systemctl enable nifi-custom-processors.path
sudo systemctl start nifi-custom-processors.path
sleep 1m
sudo ambari-agent restart

