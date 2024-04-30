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
from .utils import prepare_payload, prepare_query_params

class Webhooks:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def unassign_execution_user_1(self, payload=None, **args):
        '''
        Arguments:
        - webhookid: webhookid 
        - webhookname: webhookname 
        '''
        url="/resources/webhook/unassignexecutionuser"
        field_mapping={
          "webhookid": "webhookid", 
          "webhookname": "webhookname", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def get_webhook(self, query=None, **args):
        '''
        Arguments:
        - webhookid: webhookid 
        - webhookname: webhookname 
        '''
        url="/resources/webhook"
        field_mapping={
            "webhookid": "webhookid", 
            "webhookname": "webhookname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_webhook(self, payload=None, **args):
        url="/resources/webhook"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_webhook(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/webhook"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_webhook(self, query=None, **args):
        '''
        Arguments:
        - webhookid: webhookid 
        - webhookname: webhookname 
        '''
        url="/resources/webhook"
        field_mapping={
          "webhookid": "webhookid", 
          "webhookname": "webhookname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def disable_webhook(self, payload=None, **args):
        '''
        Arguments:
        - webhookid: webhookid 
        - webhookname: webhookname 
        '''
        url="/resources/webhook/disable"
        field_mapping={
          "webhookid": "webhookid", 
          "webhookname": "webhookname", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def enable_webhook(self, payload=None, **args):
        '''
        Arguments:
        - webhookid: webhookid 
        - webhookname: webhookname 
        '''
        url="/resources/webhook/enable"
        field_mapping={
          "webhookid": "webhookid", 
          "webhookname": "webhookname", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def list_webhooks(self, query=None, **args):
        '''
        Arguments:
        - webhookname: webhookname 
        - action: action 
        - businessServices: businessServices 
        - description: description 
        - event: event 
        - task: task 
        - taskname: taskname 
        - url: url 
        '''
        url="/resources/webhook/list"
        field_mapping={
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