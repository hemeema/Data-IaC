#!/usr/bin/python
import os
import s3utils, awsutils, ec2utils, mskutils, listutils
import subprocess

s3 = s3utils.get_client()
bucket_basename = '-bigdata-warehousing-'
zk_url_path = '/lib/kafka_2.12-2.1.0/connection-url'

#Determine appropriate bucket name based on EC2 instance tags
bucket = ec2utils.get_tag_value('Tenant Name') + bucket_basename + ec2utils.get_tag_value('Environment')

#Get folders in bucket
tables =  s3utils.get_s3_folders(startAfter="",bucket=bucket)
tables = listutils.deduplicate_list(tables)
#Get topics in Kafka
topics = mskutils.get_topics(zk_path = zk_url_path)

#Find the difference between the kafka-topic list and s3 topic list
new_topics = listutils.diff_list(tables,topics)

#Create topics
for i in range(0,len(new_topics)):
    mskutils.create_topic(new_topics[i], mskutils.get_zk_url(zk_path = zk_url_path), rep_factor='3', partition='3')
