from .utils import prepare_payload, prepare_query_params


class EmailTemplates:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_email_template(self, query=None, **args):
        """
        Arguments:
        - templateid: templateid
        - templatename: templatename
        """
        url = "/resources/emailtemplate"
        field_mapping = {
            "templateid": "templateid",
            "templatename": "templatename",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_email_template(self, payload=None, **args):
        url = "/resources/emailtemplate"
        field_mapping = {
            "sysId": "sysId",
            "templateName": "templateName",
            "description": "description",
            "connection": "connection",
            "replyTo": "replyTo",
            "to": "to",
            "cc": "cc",
            "bcc": "bcc",
            "subject": "subject",
            "body": "body",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_email_template(self, payload=None, **args):
        """
        Arguments:
        - sysId: sysId
        - templateName: templateName
        - description: description
        - connection: connection
        - replyTo: replyTo
        - to: to
        - cc: cc
        - bcc: bcc
        - subject: subject
        - body: body
        - retainSysIds: retainSysIds
        """
        url = "/resources/emailtemplate"
        field_mapping = {
            "sysId": "sysId",
            "templateName": "templateName",
            "description": "description",
            "connection": "connection",
            "replyTo": "replyTo",
            "to": "to",
            "cc": "cc",
            "bcc": "bcc",
            "subject": "subject",
            "body": "body",
            "retainSysIds": "retainSysIds",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_email_template(self, query=None, **args):
        """
        Arguments:
        - templateid: templateid
        - templatename: templatename
        """
        url = "/resources/emailtemplate"
        field_mapping = {
            "templateid": "templateid",
            "templatename": "templatename",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_email_template(self):
        url = "/resources/emailtemplate/list"
        return self.uc.get(url)
