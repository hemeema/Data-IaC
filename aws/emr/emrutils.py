#!/usr/bin/python
import awsutils, ec2utils

def get_client():
    return session.client('emr')

def get_meta_data():
    return get_client()



session = awsutils.get_session(ec2utils.get_meta_data().get('region'))
