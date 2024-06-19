from .utils import prepare_query_params, prepare_payload

# - create_business_service(service_data)
# - delete_business_service(service_id)
# - modify_business_service(service_id, **kwargs)
# - read_business_service(service_id)

class BusinessServices:
    def __init__(self, uc) -> None:
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_business_service(self, query=None, **args):
        '''
        Arguments:
        - busserviceid: busserviceid 
        - busservicename: busservicename 
        '''
        url="/resources/businessservice"
        field_mapping={
            "busserviceid": "busserviceid", 
            "busservicename": "busservicename", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_business_service(self, payload=None, **args):
        url="/resources/businessservice"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_business_service(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/businessservice"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def delete_business_service(self, query=None, **args):
        '''
        Arguments:
        - busserviceid: busserviceid 
        - busservicename: busservicename 
        '''
        url="/resources/businessservice"
        field_mapping={
          "busserviceid": "busserviceid", 
          "busservicename": "busservicename", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_business_services(self):
        url="/resources/businessservice/list"
        return self.uc.get(url)