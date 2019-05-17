#!/usr/bin/python
class hostconfig(object):
    """
        Class used to hold and update configuration for communicating with AMBARI Rest APIs

        Attributes:
            hostname (str): The hostname of the Ambari server
            port (int): The port for api communication
            base_url (str): The base url used for all api requests
        """
    def __init__(self, host="localhost", port=8080, username='username', password='password'):
        self.hostname = host
        self.port = port
        self.username = username
        self.password = password
        self.base_url = 'http://' + self.hostname + ':' + self.port + '/api/v1/'
    def reconfigure_port(self, port):
        self.port = port
        self.redefine_base_url()
    def reconfigure_host(self, hostname):
        self.hostname = hostname
        self.redefine_base_url()
    def set_hostname(self, hostname):
        self.hostname = hostname
        self.redefine_base_url()
    def set_username(self, username):
        self.username = username
    def set_password(self, password):
        self.password
    def get_base_url(self):
        return self.base_url
    def redefine_base_url(self):
        self.base_url = 'http://' + self.hostname + ':' + self.port + '/api/v1/'
