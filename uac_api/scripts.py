from .utils import prepare_payload, prepare_query_params

class Scripts:
    def __init__(self, uc) -> None:
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_script(self, query=None, **args):
        '''
        Arguments:
        - scriptid: scriptid 
        - scriptname: scriptname 
        '''
        url="/resources/script"
        field_mapping={
            "scriptid": "scriptid", 
            "scriptname": "scriptname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_script(self, payload=None, **args):
        url="/resources/script"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_script(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/script"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_script(self, query=None, **args):
        '''
        Arguments:
        - scriptid: scriptid 
        - scriptname: scriptname 
        '''
        url="/resources/script"
        field_mapping={
          "scriptid": "scriptid", 
          "scriptname": "scriptname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_scripts(self):
        url="/resources/script/list"
        return self.uc.get(url)