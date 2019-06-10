#!/usr/bin/python
from aws.resources import awsutils
import json
import sys
import os

subnetA = sys.argv[1]
subnetB = sys.argv[2]
subnetC = sys.argv[3]
securityGroup = sys.argv[4]

#Prepare template file for MSK cluster
#Update subnetA in msk-template
os.system("sudo sed -i 's/subnetA/" + subnetA + "/g' /tmp/aws/aws/msk/msk-cluster.json")
#Update subnetB in msk-template
os.system("sudo sed -i 's/subnetB/" + subnetB + "/g' /tmp/aws/aws/msk/msk-cluster.json")
#Update subnetC in msk-template
os.system("sudo sed -i 's/subnetC/" + subnetC + "/g' /tmp/aws/aws/msk/msk-cluster.json")
#Update securityGroup in msk-template
os.system("sudo sed -i 's/securityGroup/"+ securityGroup + "/g' /tmp/aws/aws/msk/msk-cluster.json")


# Create Session
session = get_session('us-east-1')
client = session.client('kafka')

with open('/tmp/msk-cluster.json', 'r') as file:
    conf = file.read()

# Parse JSON Configuration
conf_json = json.loads(conf)

response = client.create_cluster(BrokerNodeGroupInfo=conf_json['BrokerNodeGroupInfo'],ClusterName=conf_json['ClusterName'],
                                    EncryptionInfo=conf_json['EncryptionInfo'],EnhancedMonitoring=conf_json['EnhancedMonitoring'],
                                    KafkaVersion=conf_json['KafkaVersion'], NumberOfBrokerNodes=conf_json['NumberOfBrokerNodes'],
                                    Tags=conf_json['Tags'])
