#!/usr/bin/python
import awsutils, requests as req, boto3

def get_client():
    return session.client('ec2')

def get_resource():
    return boto3.resource('ec2',get_meta_data().get('region'))

def get_meta_data():
    r = req.get("http://169.254.169.254/latest/dynamic/instance-identity/document")
    return r.json()

def get_instance(instance_Id):
    return get_resource().Instance(instance_Id)

def get_tag_value(key):
    tag = get_instance(get_meta_data().get('instanceId')).tags
    for i in range(0,len(tag)):
        if tag[i]['Key'] == key:
            return tag[i]['Value']


session = awsutils.get_session(get_meta_data().get('region'))
