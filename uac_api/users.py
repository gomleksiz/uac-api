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
        """
        Arguments:
        - userId: userId
        - newPassword: newPassword
        """
        url = "/resources/user/changepassword"
        field_mapping = {
            "userId": "userId",
            "name": "userId",
            "userName": "userId",
            "newPassword": "newPassword",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def list_user_preference(self, query=None, **args):
        url = "/resources/user/preference/list"
        field_mapping = {
            "userid": "userid",
            "username": "username",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def get_user_preference(self, query=None, **args):
        url = "/resources/user/preference"
        field_mapping = {
            "userid": "userid",
            "username": "username",
            "preferencename": "preferencename",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_user_preference(self, query=None, **args):
        url = "/resources/user/preference"
        field_mapping = {
            "userid": "userid",
            "username": "username",
            "preferencename": "preferencename",
            "value": "value",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        headers = {"accept": "text/plain"}
        return self.uc.put(url, query=parameters, headers=headers, parse_response=False)

    def get_user(self, query=None, **args):
        """
        Arguments:
        - userid: userid
        - username: username
        - showTokens: showTokens
        """
        url = "/resources/user"
        field_mapping = {
            "userid": "userid",
            "username": "username",
            "showTokens": "showTokens",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_user(self, payload=None, **args):
        """
        Arguments:
        - sysId: sysId
        - userName: userName
        - userPassword: userPassword
        - firstName: firstName
        - middleName: middleName
        - lastName: lastName
        - email: email
        - title: title
        - active: active
        - lockedOut: lockedOut
        - passwordNeedsReset: passwordNeedsReset
        - businessPhone: businessPhone
        - mobilePhone: mobilePhone
        - timeZone: timeZone
        - department: department
        - manager: manager
        - browserAccess: browserAccess
        - commandLineAccess: commandLineAccess
        - webServiceAccess: webServiceAccess
        - loginMethod: loginMethod
        """
        url = "/resources/user"
        field_mapping = {
            "sysId": "sysId",
            "userName": "userName",
            "userPassword": "userPassword",
            "firstName": "firstName",
            "middleName": "middleName",
            "lastName": "lastName",
            "email": "email",
            "title": "title",
            "active": "active",
            "lockedOut": "lockedOut",
            "passwordNeedsReset": "passwordNeedsReset",
            "businessPhone": "businessPhone",
            "mobilePhone": "mobilePhone",
            "timeZone": "timeZone",
            "department": "department",
            "manager": "manager",
            "browserAccess": "browserAccess",
            "commandLineAccess": "commandLineAccess",
            "webServiceAccess": "webServiceAccess",
            "loginMethod": "loginMethod",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_user(self, payload=None, **args):
        """
        Arguments:
        - sysId: sysId
        - retainSysIds: retainSysIds
        - userName: userName
        - userPassword: userPassword
        - firstName: firstName
        - middleName: middleName
        - lastName: lastName
        - email: email
        - title: title
        - active: active
        - lockedOut: lockedOut
        - passwordNeedsReset: passwordNeedsReset
        - businessPhone: businessPhone
        - mobilePhone: mobilePhone
        - timeZone: timeZone
        - department: department
        - manager: manager
        - browserAccess: browserAccess
        - commandLineAccess: commandLineAccess
        - webServiceAccess: webServiceAccess
        - loginMethod: loginMethod
        """
        url = "/resources/user"
        field_mapping = {
            "sysId": "sysId",
            "retainSysIds": "retainSysIds",
            "userName": "userName",
            "userPassword": "userPassword",
            "firstName": "firstName",
            "middleName": "middleName",
            "lastName": "lastName",
            "email": "email",
            "title": "title",
            "active": "active",
            "lockedOut": "lockedOut",
            "passwordNeedsReset": "passwordNeedsReset",
            "businessPhone": "businessPhone",
            "mobilePhone": "mobilePhone",
            "timeZone": "timeZone",
            "department": "department",
            "manager": "manager",
            "browserAccess": "browserAccess",
            "commandLineAccess": "commandLineAccess",
            "webServiceAccess": "webServiceAccess",
            "loginMethod": "loginMethod",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_user(self, query=None, **args):
        """
        Arguments:
        - userid: userid
        - username: username
        """
        url = "/resources/user"
        field_mapping = {
            "userid": "userid",
            "username": "username",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def create_user_token(self, payload=None, **args):
        """
        Arguments:
        - retainSysIds: retainSysIds
            False will ignore sysIds in the payload and create a new task
        """
        url = "/resources/user/token"
        field_mapping = {
            "userId": "userId",
            "userName": "userName",
            "name": "name",
            "expiration": "expiration",
        }
        headers = {"accept": "text/plain", "Content-Type": "application/json"}
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(
            url, json_data=_payload, parse_response=False, headers=headers
        )

    def revoke_user_token(self, query=None, **args):
        """
        Arguments:
        - userid: userid
        - username: username
        - tokenname: tokenname
        """
        url = "/resources/user/token"
        field_mapping = {
            "userid": "userid",
            "username": "username",
            "tokenname": "tokenname",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_auth_tokens(self, query=None, **args):
        """
        Arguments:
        - userid: userid
        - username: username
        """
        url = "/resources/user/token/list"
        field_mapping = {
            "userid": "userid",
            "username": "username",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def list_users(self, query=None, **args):
        """
        Arguments:
        - showTokens: showTokens
        """
        url = "/resources/user/list"
        field_mapping = {
            "showTokens": "showTokens",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def get_groups_by_user(self, query=None, **args):
        """
        Arguments:
        - userid: userid
        - username: username
        """
        url = "/resources/user/groups"
        field_mapping = {
            "userid": "userid",
            "username": "username",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def add_user_to_group(self, query=None, **args):
        """
        Arguments:
        - userid: userid
        - username: username
        - groupid: groupid
        - groupname: groupname
        """
        url = "/resources/user/groups"
        field_mapping = {
            "userid": "userid",
            "username": "username",
            "groupid": "groupid",
            "groupname": "groupname",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.post(url, query=parameters)

    def delete_user_from_group(self, query=None, **args):
        """
        Arguments:
        - userid: userid
        - username: username
        - groupid: groupid
        - groupname: groupname
        """
        url = "/resources/user/groups"
        field_mapping = {
            "userid": "userid",
            "username": "username",
            "groupid": "groupid",
            "groupname": "groupname",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters)
