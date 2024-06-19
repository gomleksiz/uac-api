from .utils import prepare_query_params, prepare_payload

# - create_virtual_resource(resource_data)
# - delete_virtual_resource(resource_id)
# - list_virtual_resources_advanced()
# - modify_virtual_resource(resource_id, **kwargs)
# - read_virtual_resource(resource_id)
# - set_limit_on_virtual_resource(resource_id, limit)

class VirtualResources:
    def __init__(self, uc) -> None:
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_virtual_resource(self, query=None, **args):
        '''
        Arguments:
        - resourceid: resourceid 
        - resourcename: resourcename 
        '''
        url="/resources/virtual"
        field_mapping={
            "resourceid": "resourceid", 
            "resourcename": "resourcename", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_virtual_resource(self, payload=None, **args):
        url="/resources/virtual"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_virtual_resource(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/virtual"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_virtual_resource(self, query=None, **args):
        '''
        Arguments:
        - resourceid: resourceid 
        - resourcename: resourcename 
        '''
        url="/resources/virtual"
        field_mapping={
          "resourceid": "resourceid", 
          "resourcename": "resourcename", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_virtual_resources(self, query=None, **args):
        '''
        Arguments:
        - name: name 
        - resourcename: resourcename 
        - type: type 
        '''
        url="/resources/virtual/list"
        field_mapping={
            "name": "name", 
            "resourcename": "resourcename", 
            "type": "type", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def list_virtual_resources_advanced(self, query=None, **args):
        '''
        Arguments:
        - resourcename: resourcename 
        - type: type 
        - businessServices: businessServices 
        '''
        url="/resources/virtual/listadv"
        field_mapping={
            "resourcename": "resourcename", 
            "type": "type", 
            "businessServices": "businessServices", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_limit(self, payload=None, **args):
        url="/resources/virtual/ops-update-resource-limit"
        field_mapping={
          "name": "name", 
          "limit": "limit"
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)