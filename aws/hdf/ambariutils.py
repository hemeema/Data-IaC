import requests as req
import socket as sock
from resources import hostconfig as config

class ambariutils:
    """
    Class used to interact with Ambari REST APIs

    """
    def __init__(self, conf = config.hostconfig(sock.gethostname(), '8080', 'username', 'password')):
        self.conf = conf

    def get_request(self, url):
        return req.get(url,auth=(self.conf.username, self.conf.password))

    def get_component_hostname(self, cluster_name, service_name, component_name):
        extended_url = self.conf.get_base_url() + 'clusters/' + cluster_name + '/services/' + service_name + '/components/' + component_name
        raw_resp = self.get_request(extended_url)

        import json
        json_resp = json.loads(raw_resp)
        #Parse nested json structure for host component
        host_comp = dict(json_resp['host_components'][0])
        #Parse nest json structure for host role details
        host_role = dict(host_comp['HostRoles'])
        #Extract & return hostname
        return host_comp['host_name']
