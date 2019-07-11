#!/usr/bin/python
import awsutils, subprocess, os, re, ec2utils

def get_zk_url(**kwargs):
    path = ''
    try:
        path = kwargs['zk_path']
    except KeyError:
        path = '/lib/kafka_2.12-2.1.0/connection-url'
    try:
        with open(path, 'r') as file:
            zk_url = file.read()
        zk_url = re.sub('\n','',zk_url)
        return zk_url
    except IOError as err:
        print("Error: File not found at: " + path + "\n\n" + err)

def get_topics(**kwargs):
    zk_url = ''
    try:
        zk_url = kwargs['zk_url']
    except KeyError:
        try:
            zk_url = get_zk_url(zk_path = kwargs['zk_path'])
        except KeyError as err:
            print("Either a zookeeper url and/or path to file containing the url\n" + err)
    cmd = ['sudo /lib/kafka_2.12-2.1.0/bin/kafka-topics.sh --list --zookeeper ' + zk_url]
    with open('/tmp/topics.txt', 'w') as out:
        return_code = subprocess.call(cmd, shell=True, stdout=out)
    #Read topics from file
    with open('/tmp/topics.txt', 'r') as file:
        topics_raw = file.read()
    os.system('sudo rm -f /tmp/topics.txt')
    #Remove excess newline & replace newline with comma to prep for being a list
    topics_raw = topics_raw[:-1]
    topics = re.sub('\n', ',', topics_raw)
    tmp_list = []
    tmp_list.append(topics)
    kafkaTopics = []
    for item in tmp_list:
        elements = item.split(',')
        for topic in range(0,len(elements)):
            kafkaTopics.append(elements[topic])
    return kafkaTopics

def get_client():
    return session.client('kafka')

def get_cluster_state(clusterName):
    resp = kClient.list_clusters(ClusterNameFilter=clusterName)
    k_conf = resp['ClusterInfoList'][0]
    return k_conf['State']

def create_topic(topic_name, zk_url, **kwargs):
    rep_factor = ''
    partition = ''
    try:
        rep_factor = kwargs['rep_factor']
    except KeyError:
        rep_factor = 3
    try:
        partition = kwargs['partition']
    except KeyError:
        partition = 3

    os.system("sudo /lib/kafka_2.12-2.1.0/bin/kafka-topics.sh --create --replication-factor " + rep_factor + " --partitions " + partition + " --topic " + topic_name + " --zookeeper " + zk_url)


session = awsutils.get_session(ec2utils.get_meta_data().get('region'))
