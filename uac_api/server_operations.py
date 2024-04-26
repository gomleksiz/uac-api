from .utils import prepare_payload, prepare_query_params

class ServerOperations:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def roll_log(self):
        url="/resources/serveroperation/rolllog"
        return self.uc.get(url)

    def temporary_property_change(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - value: value 
        '''
        url="/resources/serveroperation/temporarypropertychange"
        field_mapping={
          "name": "name", 
          "value": "value", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)