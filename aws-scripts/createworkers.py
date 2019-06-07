#!/usr/bin/python
from scripts.resources import awsutils
import json
import sys

subnet = sys.argv[1]
securityGroup[2]
keypair = sys.argv[3]
iamProfile = sys.argv[4]

networkInterface='{"SubnetId":"' + subnet + '","DeviceIndex": 0, "Groups": ["'+securityGroup+'"]}'

# Create Session
session = awsutils.get_session('us-east-1')
client = session.client('ec2')

# Read NiFi-Node Configuration (JSON) as string
with open('/tmp/nifi-node-template.json', 'r') as file:
    conf = file.read()

# Parse JSON Configuration
conf_json = json.loads(conf)

# Read NiFi-Node user data file as string
with open('/tmp/worker-userdata.sh', 'r') as file:
    userData = file.read()

# Create NiFi-Nodes
response = client.run_instances(ImageId=conf_json['ami'], InstanceType=conf_json['instanceType'],
                                MaxCount=conf_json['maxCnt'], MinCount=conf_json['minCnt'],
                                Monitoring=conf_json['monitor'], NetworkInterfaces=[networkInterface],
                                IamInstanceProfile=iamProfile, KeyName=keypair, TagSpecifications=[conf_json['tags']],
                                BlockDeviceMappings=[conf_json['blkDev']], UserData=userData)
