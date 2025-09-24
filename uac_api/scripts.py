from .utils import prepare_payload, prepare_query_params


class Scripts:
    def __init__(self, uc) -> None:
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_script(self, query=None, **args):
        """
        Arguments:
        - scriptid: scriptid
        - scriptname: scriptname
        """
        url = "/resources/script"
        field_mapping = {
            "scriptid": "scriptid",
            "scriptname": "scriptname",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_script(self, payload=None, **args):
        url = "/resources/script"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_script(self, payload=None, **args):
        """
        Arguments:
        - sysId: sysId
        - scriptName: scriptName
        - scriptType: scriptType
        - description: description
        - content: content
        - resolveVariables: resolveVariables
        - retainSysIds: retainSysIds
        """
        url = "/resources/script"
        field_mapping = {
            "sysId": "sysId",
            "scriptName": "scriptName",
            "scriptType": "scriptType",
            "description": "description",
            "content": "content",
            "resolveVariables": "resolveVariables",
            "retainSysIds": "retainSysIds",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_script(self, query=None, **args):
        """
        Arguments:
        - scriptid: scriptid
        - scriptname: scriptname
        """
        url = "/resources/script"
        field_mapping = {
            "scriptid": "scriptid",
            "scriptname": "scriptname",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_scripts(self):
        url = "/resources/script/list"
        return self.uc.get(url)
