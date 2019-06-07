#!/bin/bash
sudo sed -i 's/hostname=localhost/hostname=hostname/g' /etc/ambari-agent/conf/ambari-agent.ini
sudo wget https://raw.githubusercontent.comadammichalsky/Data-IaC/blob/master/aws-scripts/hdf/resources/jars/ngdbc-2.1.2.jar
sudo wget https://raw.githubusercontent.com/adammichalsky/Data-IaC/blob/master/aws-scripts/hdf/resources/jars/nifi-hana-custom-processor-2.0.jar
sudo wget https://raw.githubusercontent.com/adammichalsky/Data-IaC/blob/master/aws-scripts/hdf/resources/scripts/nifi-connectors.path
sudo wget https://raw.githubusercontent.com/adammichalsky/Data-IaC/blob/master/aws-scripts/hdf/resources/scripts/nifi-connectors.svc
sudo wget https://raw.githubusercontent.com/adammichalsky/Data-IaC/blob/master/aws-scripts/hdf/resources/scripts/nifi-move-connectors.sh
sudo wget https://raw.githubusercontent.com/adammichalsky/Data-IaC/blob/master/aws-scripts/hdf/resources/scripts/nifi-custom-processors.path
sudo wget https://raw.githubusercontent.com/adammichalsky/Data-IaC/blob/master/aws-scripts/hdf/resources/scripts/nifi-custom-processors.svc
sudo wget https://raw.githubusercontent.com/adammichalsky/Data-IaC/blob/master/aws-scripts/hdf/resources/scripts/nifi-custom-processors.sh
mv /tmp/nifi-connectors.path /etc/systemd/system/nifi-connectors.path
mv /tmp/nifi-connectors.svc /etc/systemd/system/nifi-connectors.service
mv /tmp/nifi-custom-processors.path /etc/systemd/system/nifi-custom-processors.path
mv /tmp/nifi-custom-processors.svc /etc/systemd/system/nifi-custom-processors.service
sudo chmod 777 /tmp/n*
sudo systemctl start nifi-connectors.path
sudo systemctl enable nifi-custom-processors.path
sudo systemctl start nifi-custom-processors.path
sudo systemctl enable nifi-custom-processors.path
sleep 1m
sudo ambari-agent restart
