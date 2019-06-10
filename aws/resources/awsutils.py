#!/usr/bin/python
import boto3

def __init__(self, region):
    self.region = region

def set_region(self, new_region):
    self.region = new_region

def get_region(self):
    return self.region

def get_session(region):
    return boto3.session.Session(region_name=region)
