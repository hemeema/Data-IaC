#!/usr/bin/python
import nipyapi
import boto3
import json
from hdf import ambariutils as amb
from hdf.resources import hostconfig as hc

from scripts.resources import tenant, awsutils

dev_bucket = "DEVELOPMENT"
dev_bucket_id = ""
conf = hc.hostconfig(port='8443',username='username',password='password')

cred_loc = "/tmp/creds.json"
with open(cred_loc,"r") as file:
    credentials = file.read()


cred_json = json.loads(credentials)

conf.set_password(cred_json['password'])
conf.set_username(cred_json['username'])


amb_client = amb.ambariutils(conf)
host = amb_client.get_component_hostname('AW', 'NIFI_REGISTRY', 'NIFI_REGISTRY_MASTER')


nipyapi.config.registry_config.host = 'http://'+ host +':61080/nifi-registry-api'

buckets =  nipyapi.versioning.list_registry_buckets()

for x in buckets:
    if x.name == dev_bucket:
        dev_bucket_id = x.identifier
        break

flows = nipyapi.versioning.list_flows_in_bucket(dev_bucket_id)

tenant_path = tenant("SB-AW")

session = awsutils.get_session('us-east-1')
s3_client = boto3.client('s3')
s3_bucket = "big-data-dependencies"
s3_path = "backups/" + tenant_path + "/flows/"
local_path = "/big-data/backups/"

for flow in flows:
    filename = flow.name + ".json"
    export_file = open(filename, "w+")
    contents = nipyapi.versioning.export_flow_version(flow.bucket_identifier, flow.identifier, mode='json')
    export_file.write(contents)
    export_file.close()
    s3_client.upload_file(filename, s3_bucket, s3_path+filename)
