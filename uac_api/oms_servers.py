from .utils import prepare_query_params, prepare_payload

# Missing
# - delete_oms_server(oms_id)
# - modify_oms_server(oms_id, **kwargs)


class OmsServers:
    def __init__(self, uc) -> None:
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_oms_server(self, query=None, **args):
        '''
        Arguments:
        - serveraddress: serveraddress 
        - serverid: serverid 
        '''
        url="/resources/omsserver"
        field_mapping={
            "serveraddress": "serveraddress", 
            "serverid": "serverid", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_oms_server(self, payload=None, **args):
        url="/resources/omsserver"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_oms_server(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/omsserver"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_oms_server(self, query=None, **args):
        '''
        Arguments:
        - serveraddress: serveraddress 
        - serverid: serverid 
        '''
        url="/resources/omsserver"
        field_mapping={
          "serveraddress": "serveraddress", 
          "serverid": "serverid", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_oms_servers(self):
        url="/resources/omsserver/list"
        return self.uc.get(url)
