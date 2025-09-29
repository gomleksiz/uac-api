# - read_ldap_settings()
# - update_ldap_settings(ldap_settings_data)
# - update_ldap_bind_password(password)

from .utils import prepare_payload, prepare_query_params


class Ldaps:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_ldap(self):
        url = "/resources/ldap"
        return self.uc.get(url)

    def update_ldap(self, payload=None, **args):
        """
        Arguments:
        - sysId: sysId
        - url: url
        - bindDn: bindDn
        - bindPassword: bindPassword
        - useForAuthentication: useForAuthentication
        - allowLocalLogin: allowLocalLogin
        - baseDn: baseDn
        - userIdAttribute: userIdAttribute
        - userFilter: userFilter
        - groupFilter: groupFilter
        - connectTimeout: connectTimeout
        - readTimeout: readTimeout
        - userMembershipAttribute: userMembershipAttribute
        - groupMemberAttribute: groupMemberAttribute
        - loginMethod: loginMethod
        """
        url = "/resources/ldap"
        field_mapping = {
            "sysId": "sysId",
            "url": "url",
            "bindDn": "bindDn",
            "bindPassword": "bindPassword",
            "useForAuthentication": "useForAuthentication",
            "allowLocalLogin": "allowLocalLogin",
            "baseDn": "baseDn",
            "userIdAttribute": "userIdAttribute",
            "userFilter": "userFilter",
            "groupFilter": "groupFilter",
            "connectTimeout": "connectTimeout",
            "readTimeout": "readTimeout",
            "userMembershipAttribute": "userMembershipAttribute",
            "groupMemberAttribute": "groupMemberAttribute",
            "loginMethod": "loginMethod",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def update_ldap_bind_password(self, password=None, **args):
        url = "/resources/ldap/changebindpwd"
        _payload = password
        headers = {"accept": "text/plain", "Content-Type": "text/plain"}
        return self.uc.post(
            url, json_data=_payload, headers=headers, parse_response=False
        )
