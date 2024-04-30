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
        url="/resources/ldap"
        return self.uc.get(url)

    def update_ldap(self, payload=None, **args):
        url="/resources/ldap"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)