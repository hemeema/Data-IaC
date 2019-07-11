#!/usr/bin/python
import os, mskutils, sys, time

clusterName = sys.argv[1]
kafka_path = '/lib/kafka_2.12-2.1.0/'

#Define some functions used later on
kClient = mskutils.get_client()

clusterState = mskutils.get_cluster_state_by_name(clusterName)

while clusterState != 'ACTIVE':
    clusterState = mskutils.get_cluster_state_by_name(clusterName)
    time.sleep(60)


arn = get_cluster_arn_by_name(clusterName)
zk_url = get_zk_url_by_name(clusterName)

with open(kafka_path + 'connection-url', 'w') as file:
    file.write(zk_url)

with open(kafka_path + 'cluster-arn', 'w') as file:
    file.write(arn)

os.system("sudo /custom_scripts/create-topics.py")
os.system("sudo cp /custom_scripts/create-topics.py /etc/cron.hourly/")
os.system("sudo chmod +x /etc/cron.hourly/create-topics.py")
