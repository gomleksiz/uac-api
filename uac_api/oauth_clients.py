# - create_oauth_client(client_data)
# - modify_oauth_client(client_id, **kwargs)
# - read_oauth_client(client_id)
# - delete_oauth_client(client_id)
# - list_oauth_clients()

from .utils import prepare_payload, prepare_query_params

class OAuthClients:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc
    
    def get_oauth_client(self, query=None, **args):
        '''
        Arguments:
        - oauthclientid: oauthclientid 
        - oauthclientname: oauthclientname 
        '''
        url="/resources/oauthclient"
        field_mapping={
            "oauthclientid": "oauthclientid", 
            "oauthclientname": "oauthclientname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_oauth_client(self, payload=None, **args):
        url="/resources/oauthclient"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_oauth_client(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/oauthclient"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_oauth_client(self, query=None, **args):
        '''
        Arguments:
        - oauthclientid: oauthclientid 
        - oauthclientname: oauthclientname 
        '''
        url="/resources/oauthclient"
        field_mapping={
          "oauthclientid": "oauthclientid", 
          "oauthclientname": "oauthclientname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_oauth_clients(self):
        url="/resources/oauthclient/list"
        return self.uc.get(url)
