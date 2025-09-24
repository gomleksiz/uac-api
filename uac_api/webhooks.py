# - assign_execution_user_to_webhook(webhook_id, execution_user)
# - disable_webhook(webhook_id)
# - enable_webhook(webhook_id)
# - enable_disable_multiple_webhooks(webhook_ids, enable=True)
# - list_webhooks()
# - modify_webhooks(webhook_id, **kwargs)
# - read_webhook(webhook_id)
# - register_webhook(webhook_data)
# - unassign_execution_user_from_webhook(webhook_id)
# - unregister_webhook(webhook_id)
from .utils import prepare_payload, prepare_query_params, prepare_query_payload


class Webhooks:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def enable_disable(self, payload=None, **args):
        url = "/resources/webhook/enabledisable"
        field_mapping = {
            "name": "name",
            "enable": "enable",
        }
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(
            url, json_data=_payload, headers=headers, parse_response=True
        )

    def assign_execution_user(self, query=None, payload=None, **args):
        url = "/resources/webhook/assignexecutionuser"
        query_mapping = {
            "webhookid": "webhookid",
            "webhookname": "webhookname",
        }
        payload_mapping = {
            "username": "username",
            "password": "password",
            "token": "token",
        }
        _query, _payload = prepare_query_payload(
            query, query_mapping, payload, payload_mapping, args
        )
        return self.uc.post(url, query=_query, json_data=_payload, parse_response=False)

    def unassign_execution_user(self, query=None, **args):
        """
        Arguments:
        - webhookid: webhookid
        - webhookname: webhookname
        """
        url = "/resources/webhook/unassignexecutionuser"
        field_mapping = {
            "webhookid": "webhookid",
            "webhookname": "webhookname",
        }
        _query = prepare_query_params(query, field_mapping, args)
        return self.uc.post(url, query=_query, parse_response=False)

    def get_webhook(self, query=None, **args):
        """
        Arguments:
        - webhookid: webhookid
        - webhookname: webhookname
        """
        url = "/resources/webhook"
        field_mapping = {
            "webhookid": "webhookid",
            "webhookname": "webhookname",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_webhook(self, payload=None, **args):
        url = "/resources/webhook"
        field_mapping = {
            "sysId": "sysId",
            "name": "name",
            "description": "description",
            "action": "action",
            "task": "task",
            "url": "url",
            "enabledBy": "enabledBy",
            "enabledTime": "enabledTime",
            "disabledBy": "disabledBy",
            "disabledTime": "disabledTime",
            "executionUser": "executionUser",
            "status": "status",
            "statusDescription": "statusDescription",
            "httpAuth": "httpAuth",
            "credentials": "credentials",
            "urlParametersFromString": "urlParametersFromString",
            "httpHeadersFromString": "httpHeadersFromString",
            "eventBusinessServiceCriteria": "eventBusinessServiceCriteria",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_webhook(self, payload=None, **args):
        """
        Arguments:
        - sysId: sysId
        - name: name
        - description: description
        - retainSysIds: retainSysIds
        - action: action
        - task: task
        - url: url
        - enabledBy: enabledBy
        - enabledTime: enabledTime
        - disabledBy: disabledBy
        - disabledTime: disabledTime
        - executionUser: executionUser
        - status: status
        - statusDescription: statusDescription
        - httpAuth: httpAuth
        - credentials: credentials
        - eventBusinessServiceCriteria: eventBusinessServiceCriteria
        """
        url = "/resources/webhook"
        field_mapping = {
            "sysId": "sysId",
            "name": "name",
            "description": "description",
            "retainSysIds": "retainSysIds",
            "action": "action",
            "task": "task",
            "url": "url",
            "enabledBy": "enabledBy",
            "enabledTime": "enabledTime",
            "disabledBy": "disabledBy",
            "disabledTime": "disabledTime",
            "executionUser": "executionUser",
            "status": "status",
            "statusDescription": "statusDescription",
            "httpAuth": "httpAuth",
            "credentials": "credentials",
            "eventBusinessServiceCriteria": "eventBusinessServiceCriteria",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_webhook(self, query=None, **args):
        """
        Arguments:
        - webhookid: webhookid
        - webhookname: webhookname
        """
        url = "/resources/webhook"
        field_mapping = {
            "webhookid": "webhookid",
            "webhookname": "webhookname",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def disable_webhook(self, payload=None, **args):
        """
        Arguments:
        - webhookid: webhookid
        - webhookname: webhookname
        """
        url = "/resources/webhook/disable"
        field_mapping = {
            "webhookid": "webhookid",
            "webhookname": "webhookname",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def enable_webhook(self, payload=None, **args):
        """
        Arguments:
        - webhookid: webhookid
        - webhookname: webhookname
        """
        url = "/resources/webhook/enable"
        field_mapping = {
            "webhookid": "webhookid",
            "webhookname": "webhookname",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def list_webhooks(self, query=None, **args):
        """
        Arguments:
        - webhookname: webhookname
        - action: action
        - businessServices: businessServices
        - description: description
        - event: event
        - task: task
        - taskname: taskname
        - url: url
        """
        url = "/resources/webhook/list"
        field_mapping = {
            "webhookname": "webhookname",
            "action": "action",
            "businessServices": "businessServices",
            "description": "description",
            "event": "event",
            "task": "task",
            "taskname": "taskname",
            "url": "url",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)
