#!/usr/bin/python
import awsutils, ec2utils, re

def get_client():
    return session.client('s3')
def get_resource():
    return session.resource('s3')

def get_s3_folders(**kwargs):
    tables = []
    s3 = ''
    try:
        s3 = kwargs['s3_client']
    except KeyError:
        s3 = get_client()
    resp = s3.list_objects_v2(Bucket=kwargs['bucket'],Delimiter='/',MaxKeys=10,StartAfter=kwargs['startAfter'])
    if resp['KeyCount'] > 0:
        resp = resp['CommonPrefixes']
        if len(resp)>1:
            for obj in resp:
                tables.append(re.sub('(\/.+)|(\/)','',obj['Prefix']))
            sub_table = get_s3_folders(startAfter=tables[len(tables)-1], bucket=kwargs['bucket'], s3_client=s3)
            tables = tables + sub_table
        else:
            for obj in resp:
                tables.append(re.sub('(\/.+)|(\/)','',obj['Prefix']))
        return tables
    else:
        return tables

session = awsutils.get_session(ec2utils.get_meta_data().get('region'))
