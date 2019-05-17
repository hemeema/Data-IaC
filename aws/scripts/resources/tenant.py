#!/usr/bin/python
import json
class tenant(object):
    def __init__(self):
        tenant_info = open("/big-data/tenant-info.json", "r")
        tnt_info = json.loads(tenant_info)
        self.tenant_id = tnt_info['tenant_id']
        self.env_id = tnt_info['env_id']
        self.dependency_path = self.env_id + "-" + self.tenant_id
