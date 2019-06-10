import requests as req
import socket as sock
from resources import hostconfig as config

class ambariutils:
    """
    Class used to interact with Ambari REST APIs

    """
    def __init__(self, conf):
        self.conf = conf

    def get_request(self, url):
        return req.get(url,auth=(self.conf.username, self.conf.password))

    def get_component_hostname(self, cluster_name, service_name, component_name):
        extended_url = self.conf.get_base_url() + 'clusters/' + cluster_name + '/services/' + service_name + '/components/' + component_name
        raw_resp = self.get_request(extended_url)
        host = raw_resp.json()['host_components'][0]['HostRoles']['host_name']
        return host
