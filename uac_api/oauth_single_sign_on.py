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
        """
        Arguments:
        - singleSignOn: singleSignOn
        - issuerUri: issuerUri
        - scopes: scopes
        - clientId: clientId
        - clientSecret: clientSecret
        - pkce: pkce
        - userNameClaimName: userNameClaimName
        - clusterBaseRedirectUrls: clusterBaseRedirectUrls
        - userProvisioning: userProvisioning
        - attrFirstName: attrFirstName
        - attrMiddleName: attrMiddleName
        - attrLastName: attrLastName
        - attrPhone: attrPhone
        - attrHomePhone: attrHomePhone
        - attrMobilePhone: attrMobilePhone
        - attrEmail: attrEmail
        - attrTitle: attrTitle
        - attrManager: attrManager
        - attrDepartment: attrDepartment
        - attrActive: attrActive
        - attrGroups: attrGroups
        - tokenValidation: tokenValidation
        - opaqueIntrospectionUri: opaqueIntrospectionUri
        - jwtJwkSetUri: jwtJwkSetUri
        - jwtAudienceClaimValue: jwtAudienceClaimValue
        - portalClientId: portalClientId
        - portalApiScopes: portalApiScopes
        """
        field_mapping = {
            "singleSignOn": "singleSignOn",
            "issuerUri": "issuerUri",
            "scopes": "scopes",
            "clientId": "clientId",
            "clientSecret": "clientSecret",
            "pkce": "pkce",
            "userNameClaimName": "userNameClaimName",
            "clusterBaseRedirectUrls": "clusterBaseRedirectUrls",
            "userProvisioning": "userProvisioning",
            "attrFirstName": "attrFirstName",
            "attrMiddleName": "attrMiddleName",
            "attrLastName": "attrLastName",
            "attrPhone": "attrPhone",
            "attrHomePhone": "attrHomePhone",
            "attrMobilePhone": "attrMobilePhone",
            "attrEmail": "attrEmail",
            "attrTitle": "attrTitle",
            "attrManager": "attrManager",
            "attrDepartment": "attrDepartment",
            "attrActive": "attrActive",
            "attrGroups": "attrGroups",
            "tokenValidation": "tokenValidation",
            "opaqueIntrospectionUri": "opaqueIntrospectionUri",
            "jwtJwkSetUri": "jwtJwkSetUri",
            "jwtAudienceClaimValue": "jwtAudienceClaimValue",
            "portalClientId": "portalClientId",
            "portalApiScopes": "portalApiScopes",
        }
        url = "/resources/oauthsettings"
        _payload = prepare_payload(
            payload=payload, field_mapping=field_mapping, args=args
        )
        headers = {"accept": "text/plain", "Content-Type": "application/json"}
        return self.uc.put(
            url, json_data=_payload, headers=headers, parse_response=False
        )

    def read_single_sign_on_settings(self):
        url = "/resources/oauthsettings"
        return self.uc.get(url)
