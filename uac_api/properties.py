from .utils import prepare_payload, prepare_query_params, prepare_query_payload

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

    def update_property(self, payload=None, query=None, **args):
        url="/resources/property"
        query_fields={
            "propertyname": "propertyname", 
            "value": "value"
        }
        payload_fields = {
        }
        _query, _payload = prepare_query_payload(query, query_fields, payload, payload_fields, args)
        return self.uc.put(url, query=_query, json_data=_payload, parse_response=False)

    def list_properties(self):
        url="/resources/property/list"
        return self.uc.get(url)
