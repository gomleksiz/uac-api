# - create_user(user_data)
# - create_personal_access_token(user_name)
# - delete_user(user_name)
# - list_personal_access_tokens(user_name)
# - list_users()
# - modify_user(user_name, **kwargs)
# - read_user(user_name)
# - revoke_personal_access_token(user_name, token_id)

from .utils import prepare_payload, prepare_query_params

class Users:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def change_user_password(self, payload=None, **args):
        '''
        Arguments:
        - userId: userId 
        - newPassword: newPassword 
        '''
        url="/resources/user/changepassword"
        field_mapping={
          "userId": "userId", 
          "name": "userId", 
          "newPassword": "newPassword", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def get_user(self, query=None, **args):
        '''
        Arguments:
        - userid: userid 
        - username: username 
        - showTokens: showTokens 
        '''
        url="/resources/user"
        field_mapping={
            "userid": "userid", 
            "username": "username", 
            "showTokens": "showTokens", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_user(self, payload=None, **args):
        url="/resources/user"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_user(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/user"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_user(self, query=None, **args):
        '''
        Arguments:
        - userid: userid 
        - username: username 
        '''
        url="/resources/user"
        field_mapping={
          "userid": "userid", 
          "username": "username", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def create_user_token(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/user/token"
        field_mapping={
          "retainSysIds": "retainSysIds", 
          "userId":'userId',
          "userName": "userName",
          "name": "name",
          "expiration": "expiration"
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def revoke_user_token(self, query=None, **args):
        '''
        Arguments:
        - userid: userid 
        - username: username 
        - tokenname: tokenname 
        '''
        url="/resources/user/token"
        field_mapping={
          "userid": "userid", 
          "username": "username", 
          "tokenname": "tokenname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_auth_tokens(self, query=None, **args):
        '''
        Arguments:
        - userid: userid 
        - username: username 
        '''
        url="/resources/user/token/list"
        field_mapping={
            "userid": "userid", 
            "username": "username", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def list_users(self, query=None, **args):
        '''
        Arguments:
        - showTokens: showTokens 
        '''
        url="/resources/user/list"
        field_mapping={
            "showTokens": "showTokens", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)