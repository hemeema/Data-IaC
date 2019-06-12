#!/usr/bin/python
import os
import boto3
import re
import subprocess

#Define some functions used later on
def get_session(region):
    return boto3.session.Session(region_name=region)

def diff(first, second):
        second = set(second)
        return [item for item in first if item not in second]

session = get_session('us-east-1')
s3 = session.client('s3')
bucket = 'big-data-warehousing'

tables = []

for obj in s3.list_objects_v2(Bucket=bucket)['Contents']:
    tables.append(re.sub('(\/.+)|(\/)','',obj['Key']))

s3List = []

for i in tables:
  if i not in s3List:
    s3List.append(i)

#Get topics in Kafka
#Get Kafka zookeeper String
with open('/lib/kafka_2.12-2.1.0/connection-url', 'r') as file:
    zk_url = file.read()

zk_url = re.sub('\n','',zk_url)

cmd = ['sudo /lib/kafka_2.12-2.1.0/bin/kafka-topics.sh --list --zookeeper ' + zk_url]

with open('/tmp/topics.txt', 'w') as out:
    return_code = subprocess.call(cmd, shell=True, stdout=out)

#Read topics from file
with open('/tmp/topics.txt', 'r') as file:
    topics_raw = file.read()

topics_raw = topics_raw[:-1]
topics = re.sub('\n', ',', topics_raw)
tmp_list = []
tmp_list.append(topics)
kafkaTopics = []

for item in tmp_list:
    elements = item.split(',')
    for topic in range(0,len(elements)):
        kafkaTopics.append(elements[topic])

#Find the difference between the kafka-topic list and s3 topic list
newTopics = diff(s3List,kafkaTopics)

#Create new topics in Kafka Cluster
rep_factor = "3"
partition = "3"

#Create topics
for i in range(0,len(newTopics)):
    os.system("sudo /lib/kafka_2.12-2.1.0/bin/kafka-topics.sh --create --replication-factor " + rep_factor + " --partitions " + partition + " --topic " + newTopics[i] + " --zookeeper " + zk_url)
