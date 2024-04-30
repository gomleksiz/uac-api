from .utils import prepare_payload, prepare_query_params

class UserGroups:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_user_group(self, query=None, **args):
        '''
        Arguments:
        - groupid: groupid 
        - groupname: groupname 
        '''
        url="/resources/usergroup"
        field_mapping={
            "groupid": "groupid", 
            "groupname": "groupname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_user_group(self, payload=None, **args):
        url="/resources/usergroup"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_user_group(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/usergroup"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_user_group(self, query=None, **args):
        '''
        Arguments:
        - groupid: groupid 
        - groupname: groupname 
        '''
        url="/resources/usergroup"
        field_mapping={
          "groupid": "groupid", 
          "groupname": "groupname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_user_groups(self):
        url="/resources/usergroup/list"
        return self.uc.get(url)