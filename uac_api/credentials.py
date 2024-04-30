from .utils import prepare_payload, prepare_query_params

# - create_credential(credential_data)
# - delete_credential(credential_id)
# - list_credentials()
# - modify_credential(credential_id, **kwargs)
# - read_credential(credential_id)

class Credentials:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def change_password(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - newRuntimePassword: newRuntimePassword 
        '''
        url="/resources/credential/ops-change-password"
        field_mapping={
          "name": "name", 
          "newRuntimePassword": "newRuntimePassword", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def get_credential(self, query=None, **args):
        '''
        Arguments:
        - credentialid: credentialid 
        - credentialname: credentialname 
        '''
        url="/resources/credential"
        field_mapping={
            "credentialid": "credentialid", 
            "credentialname": "credentialname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_credential(self, payload=None, **args):
        url="/resources/credential"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_credential(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/credential"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_credential(self, query=None, **args):
        '''
        Arguments:
        - credentialid: credentialid 
        - credentialname: credentialname 
        '''
        url="/resources/credential"
        field_mapping={
          "credentialid": "credentialid", 
          "credentialname": "credentialname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_credentials(self):
        url="/resources/credential/list"
        return self.uc.get(url)

    def test_provider(self, query=None, **args):
        '''
        Arguments:
        - credentialid: credentialid 
        - credentialname: credentialname 
        '''
        url="/resources/credential/testprovider"
        field_mapping={
          "credentialid": "credentialid", 
          "credentialname": "credentialname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.post(url, query=parameters, json_data=None)