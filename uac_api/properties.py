from .utils import prepare_payload, prepare_query_params

class Properties:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_property(self, query=None, **args):
        '''
        Arguments:
        - propertyname: propertyname 
        '''
        url="/resources/property"
        field_mapping={
            "propertyname": "propertyname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_property(self, payload=None, **args):
        url="/resources/property"
        _payload = payload
        return self.uc.put(url, json_data=_payload)

    def list_properties(self):
        url="/resources/property/list"
        return self.uc.get(url)
