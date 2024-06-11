import requests
import sys
import json
import re

from .server_operations import ServerOperations
from .metrics import Metrics
from .audits import Audits
from .system import System
from .ldap import Ldaps
from .tasks import Tasks
from .triggers import Triggers
from .universal_events import UniversalEvents
from .bundles import Bundles
from .users import Users
from .credentials import Credentials
from .properties import Properties
from .custom_days import CustomDays
from .variables import Variables
from .connections import Connections
from .simulations import Simulations
from .business_services import BusinessServices
from .agents import Agents
from .agents import AgentClusters
from .virtual_resources import VirtualResources
from .oms_servers import OmsServers
from .universal_event_templates import UniversalEventTemplates
from .reports import Reports
from .task_instances import TaskInstances
from .workflows import Workflows
from .scripts import Scripts
from .user_groups import UserGroups
from .webhooks import Webhooks
from .cluster_nodes import ClusterNodes
from .email_templates import EmailTemplates
from .oauth_clients import OAuthClients
from .calendars import Calendars
from .universal_templates import UniversalTemplates
from .utils import strip_url, filter_secrets
import logging

__version__ = "0.4.11"

class UniversalController():
    def __init__(self, base_url, credential=None, token=None, ssl_verify=True, logger=None, headers=None) -> None:
        if logger is None:
            logger = logging.getLogger(__name__)
            logger.setLevel(logging.INFO)
            logger.addHandler(logging.StreamHandler())
            self.log = logger
        else:
            self.log = logger
        self.base_url = strip_url(base_url)
        self.token = token
        self.ssl_verify = ssl_verify
        self.cridential = credential
        self.secrets = []
        if token:
            self.secrets.append(token)
        else:
            self.secrets.append(credential[1])
        if headers:
            self.headers = headers
        else:
            self.headers = {"content-type": "application/json", "accept": "application/json"}
        self.server_operations = ServerOperations(self)
        self.metrics = Metrics(self)
        self.audits = Audits(self)
        self.system = System(self)
        self.ldap = Ldaps(self)
        self.tasks = Tasks(self)
        self.triggers = Triggers(self)
        self.universal_events = UniversalEvents(self)
        self.bundles = Bundles(self)
        self.users = Users(self)
        self.credentials = Credentials(self)
        self.properties = Properties(self)
        self.custom_days = CustomDays(self)
        self.variables = Variables(self)
        self.connections = Connections(self)
        self.simulations = Simulations(self)
        self.business_services = BusinessServices(self)
        self.agents = Agents(self)
        self.agent_clusters = AgentClusters(self)
        self.virtual_resources = VirtualResources(self)
        self.oms_servers = OmsServers(self)
        self.universal_event_templates = UniversalEventTemplates(self)
        self.reports = Reports(self)
        self.task_instances = TaskInstances(self)
        self.workflows = Workflows(self)
        self.scripts = Scripts(self)
        self.user_groups = UserGroups(self)
        self.webhooks = Webhooks(self)
        self.cluster_nodes = ClusterNodes(self)
        self.email_templates = EmailTemplates(self)
        self.oauth_clients = OAuthClients(self)
        self.calendars = Calendars(self)
        self.universal_templates = UniversalTemplates(self)


    def post(self, resource, query="", json_data=None, headers=None, parse_response=True):
        return self.call("POST", resource, query, headers, data=json_data, parse_response=parse_response)
    
    def put(self, resource, query="", json_data=None, headers=None, parse_response=True):
        return self.call("PUT", resource, query, headers, data=json_data, parse_response=parse_response)

    def get(self, resource, query="", headers=None, parse_response=True):
        return self.call("GET", resource, query, headers, data=None, parse_response=parse_response)

    def delete(self, resource, query="", json_data=None, headers=None, parse_response=True):
        return self.call("DELETE", resource, query, headers, data=json_data, parse_response=parse_response)
    
    def post_data(self, resource, query="", data=None, headers=None, parse_response=True):
        return self.call("POST", resource, query, headers, data, parse_response, binary=True)

    def call(self, method, resource, query, headers, data, parse_response, binary=False):
        self.log.debug(filter_secrets("uac_rest_call start", self.secrets))
        self.log.debug(headers)
        if headers:
            _headers = headers
        else:
            _headers = self.headers
        
        if self.token:
            _headers["Authorization"] = f"Bearer {self.token}"

        self.log.debug(filter_secrets(f"HEADERS => {_headers}", self.secrets))
        if len(query) > 0:
            query = "?" + "&".join(query)
        else:
            query = ""
        uri = f"{self.base_url}{resource}{query}"
        self.log.info(f"URL = {uri}")
        try:
            if method == "GET":
                response = requests.get(uri,
                                        headers=_headers,
                                        auth=self.cridential,
                                        verify=self.ssl_verify)
            elif method == "POST":
                if not binary:
                    self.log.debug(filter_secrets(f"Payload = {data}", self.secrets))
                    response = requests.post(uri,
                                            headers=_headers,
                                            auth=self.cridential,
                                            json=data,
                                            verify=self.ssl_verify)
                else:
                    self.log.debug(filter_secrets(f"Payload = {data}", self.secrets))
                    response = requests.post(uri,
                                            headers=_headers,
                                            auth=self.cridential,
                                            data=data,
                                            verify=self.ssl_verify)
            elif method == "DELETE":
                response = requests.delete(uri,
                                        headers=_headers,
                                        auth=self.cridential,
                                        json=data,
                                        verify=self.ssl_verify)
            elif method == "PUT":
                self.log.debug(filter_secrets(f"Payload = {data}", self.secrets))
                response = requests.put(uri,
                                        headers=_headers,
                                        auth=self.cridential,
                                        json=data,
                                        verify=self.ssl_verify)
            else:
                self.log.error(f"Unknown method {method}")
                raise
        except Exception as unknown_exception:
            self.log.error(f"Error Calling{self.base_url} API {sys.exc_info()}")
            raise
        if response.ok:
            pass
        else:
            self.log.error(f"{uri} Response Code : {response.status_code}")
            self.log.error(f"Failed with reason : {response.text}")
            response.raise_for_status()
            response = None
        # if response:
        #     self.log.debug(filter_secrets("response: " + response.text, self.secrets))
        resp_data = None
        try:
            if parse_response:
                resp_data = response.json()
                self.log.debug(filter_secrets("received data: %s..." % json.dumps(resp_data), self.secrets))
            else:
                resp_data = {"response": response.text}
                # Match anything like UUID: 0f2bd3ea0fc34da08bb668ccceee8c5a
                matched = re.search(r"([0-9a-f]{32})", response.text)
                if matched:
                    resp_data["sys_id"] = matched.group(0)

                self.log.debug(filter_secrets("received data: %s..." % resp_data, self.secrets))
        except Exception as unknown_exception:
            # no XML returned
            self.log.error("Couldn't parse the response.")
            resp_data = response.text
        # self.log.debug(filter_secrets("received data: %s..." % json.dumps(resp_data)[0:10], self.secrets))
        self.log.debug(filter_secrets("uac_rest_call end", self.secrets))
        if _headers.get("Accept") in ["application/pdf", "image/png", "application/octet-stream"]:
            return response.content
        return resp_data


    