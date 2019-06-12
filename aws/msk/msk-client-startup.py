#!/usr/bin/python
import os
import boto3
import sys


clusterName = sys.argv[1]
kafka_path = '/lib/kafka_2.12-2.1.0/'

#Define some functions used later on
def get_session(region):
    return boto3.session.Session(region_name=region)

session = get_session('us-east-1')
kClient = session.client('kafka')

resp = kClient.list_clusters(ClusterNameFilter=clusterName)

k_conf = resp['ClusterInfoList'][0]
arn = k_conf['ClusterArn']
zk_url = k_conf['ZookeeperConnectString']

with open(kafka_path + 'connection-url', 'w') as file:
    file.write(zk_url)

with open(kafka_path + 'cluster-arn', 'w') as file:
    file.write(arn)

clusterState = k_conf['State']

while k_conf['State'] != 'ACTIVE':
    resp = kClient.list_clusters(ClusterNameFilter='BigData-MSK')
    k_conf = resp['ClusterInfoList'][0]

os.system("sudo /custom_scripts/create-topics.py")
os.system("sudo cp /custom_scripts/create-topics.py /etc/cron.hourly/")
os.system("sudo chmod +x /etc/cron.hourly/create-topics.py")
