#!/usr/bin/python
import boto3
import json
import sys
import os

def get_session(region):
    return boto3.session.Session(region_name=region)

subnetA = sys.argv[1]
subnetB = sys.argv[2]
subnetC = sys.argv[3]
securityGroup = sys.argv[4]
clusterName = sys.argv[5]
volume = sys.argv[6]
instanceType = sys.argv[7]


#Prepare template file for MSK cluster
#Update subnetA in msk-template
os.system("sudo sed -i 's/subnetA/" + subnetA + "/g' /custom_scripts/msk-cluster.json")
#Update subnetB in msk-template
os.system("sudo sed -i 's/subnetB/" + subnetB + "/g' /custom_scripts/msk-cluster.json")
#Update subnetC in msk-template
os.system("sudo sed -i 's/subnetC/" + subnetC + "/g' /custom_scripts/msk-cluster.json")
#Update securityGroup in msk-template
os.system("sudo sed -i 's/securityGroup/"+ securityGroup + "/g' /custom_scripts/msk-cluster.json")
#Update clusterName in msk-template
os.system("sudo sed -i 's/new-cluster-name/"+ clusterName + "/g' /custom_scripts/msk-cluster.json")
#Update clusterName in msk-template
os.system("sudo sed -i 's/msk-volume/"+ volume + "/g' /custom_scripts/msk-cluster.json")
#Update clusterName in msk-template
os.system("sudo sed -i 's/msk-instance/"+ instanceType + "/g' /custom_scripts/msk-cluster.json")

# Create Session
session = get_session('us-east-1')
client = session.client('kafka')

with open('/custom_scripts/msk-cluster.json', 'r') as file:
    conf = file.read()

# Parse JSON Configuration
conf_json = json.loads(conf)

response = client.create_cluster(BrokerNodeGroupInfo=conf_json['BrokerNodeGroupInfo'],ClusterName=conf_json['ClusterName'],
                                    EnhancedMonitoring=conf_json['EnhancedMonitoring'],KafkaVersion=conf_json['KafkaVersion'],
                                    NumberOfBrokerNodes=conf_json['NumberOfBrokerNodes'],EncryptionInfo=['EncryptionInfo'])

os.system("sudo /custom_scripts/msk-client-startup.py " + clusterName)
