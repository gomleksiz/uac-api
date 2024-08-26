from .utils import prepare_payload, prepare_query_params

class UniversalEvents:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    # def push_event(self, event_name, payload):
    #     url = f"/universalevent/push/{event_name}"
    #     self.log.debug("Launch task payload is {}".format(payload))
    #     headers = self.headers
    #     headers["Content-Type"] = "plain/text"
    #     response = self.uc.post(url, json_data=payload, parse_json=False, headers=headers)
    #     return response

    def publish(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - businessServices: businessServices 
        - ttl: ttl 
        - attributes: attributes 
        '''
        url="/resources/universalevent/publish"
        field_mapping={
          "name": "name", 
          "businessServices": "businessServices", 
          "ttl": "ttl", 
          "attributes": "attributes", 
        }
        headers = {"Accept": "*/*"}
        headers["Content-Type"] = "application/json"
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False, headers=headers)

    def pushg(self, query=None, eventName=None, **args):
        '''
        This will run a get request to push event
        Arguments:
        - payload: payload 
        - eventName: eventName 
        '''
        url=f"/resources/universalevent/push/{eventName}"
        field_mapping={
            "payload": "payload", 
            "eventName": "eventName", 
        }
        # Accept all the query parameters
        for key, value in args.items(): 
            field_mapping[key] = key

        parameters = prepare_query_params(query, field_mapping, args)
        headers = {"Accept": "*/*"}
        headers["Content-Type"] = "plain/text"
        return self.uc.get(url, query=parameters, parse_response=False, headers=headers)

    def push(self, payload=None, eventName=None, payload_format='json'):
        '''
        Payload is required
        Arguments:
        - eventName: eventName 
        - payload_format: json|xml|text
        '''
        url=f"/resources/universalevent/push/{eventName}"
        
        headers = {"Accept": "*/*"}
        if payload_format == 'json':
            headers["Content-Type"] = "application/json"
        elif payload_format == 'xml':
            headers["Content-Type"] = "application/xml"
        else:
            headers["Content-Type"] = "plain/text"
        return self.uc.post(url, json_data=payload, parse_response=False, headers=headers)