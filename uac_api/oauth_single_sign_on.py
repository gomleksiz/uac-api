# - create_oauth_client(client_data)
# - modify_oauth_client(client_id, **kwargs)
# - read_oauth_client(client_id)
# - delete_oauth_client(client_id)
# - list_oauth_clients()

from .utils import prepare_payload, prepare_query_params


class OAuthSingleSignOn:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def update_single_sign_on_settings(self, payload=None, **args):
        url = "/resources/oauthsettings"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def read_single_sign_on_settings(self):
        url = "/resources/oauthsettings"
        return self.uc.get(url)
