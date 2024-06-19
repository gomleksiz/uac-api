# - create_universal_event_template(template_data)
# - delete_universal_event_template(template_id)
# - list_universal_event_templates()
# - modify_universal_event_template(template_id, **kwargs)
# - read_universal_event_template(template_id)
from .utils import prepare_payload, prepare_query_params

class UniversalEventTemplates:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc
    
    def get_universal_event_template(self, query=None, **args):
        '''
        Arguments:
        - templateid: templateid 
        - templatename: templatename 
        '''
        url="/resources/universaleventtemplate"
        field_mapping={
            "templateid": "templateid", 
            "templatename": "templatename", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_universal_event_template(self, payload=None, **args):
        url="/resources/universaleventtemplate"
        _payload = payload
        return self.uc.put(url, json_data=_payload)

    def create_universal_event_template(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/universaleventtemplate"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_universal_event_template(self, query=None, **args):
        '''
        Arguments:
        - templateid: templateid 
        - templatename: templatename 
        '''
        url="/resources/universaleventtemplate"
        field_mapping={
          "templateid": "templateid", 
          "templatename": "templatename", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_universal_event_templates(self, query=None, **args):
        '''
        Arguments:
        - templatename: templatename 
        '''
        url="/resources/universaleventtemplate/list"
        field_mapping={
            "templatename": "templatename", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)