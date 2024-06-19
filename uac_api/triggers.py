# - assign_execution_user_to_trigger(trigger_id, user_name)
# - create_trigger(trigger_data)
# - delete_trigger(trigger_id)
# - enable_disable_trigger(trigger_id, enable=True)
# - list_trigger_qualifying_times(trigger_id)
# - list_triggers()
# - list_triggers_advanced()
# - modify_trigger(trigger_id, **kwargs)
# - modify_time_of_time_trigger(trigger_id, new_time)
# - read_trigger(trigger_id)
# - trigger_now(trigger_id)
# - unassign_execution_user_from_trigger(trigger_id)
from .utils import prepare_payload, prepare_query_params, prepare_query_payload

class Triggers:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def list_qualifying_times(self, query=None, **args):
        '''
        Arguments:
        - triggerid: triggerid 
        - triggername: triggername 
        - count: count 
        - startdate: startdate 
        '''
        url="/resources/trigger/qualifyingtimes"
        field_mapping={
            "triggerid": "triggerid", 
            "triggername": "triggername", 
            "count": "count", 
            "startdate": "startdate", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def unassign_execution_user(self, query=None, **args):
        '''
        Arguments:
        - triggerid: triggerid 
        - triggername: triggername 
        '''
        url="/resources/trigger/unassignexecutionuser"
        field_mapping={
          "triggerid": "triggerid", 
          "triggername": "triggername", 
        }
        _query = prepare_query_params(query, field_mapping, args)
        return self.uc.post(url, query=_query, json_data=None, parse_response=False)

    def assign_execution_user_to_trigger(self, query=None, payload=None, **args):
        '''
        Arguments:
        - triggerid: triggerid 
        - triggername: triggername 
        '''
        url="/resources/trigger/assignexecutionuser"
        query_fields = {
            "triggername": "triggername",
            "triggerid": "triggerid"
        }

        payload_fields={
          "username": "username", 
          "username": "username", 
        }
        _query, _payload = prepare_query_payload(query, query_fields, payload, payload_fields, args)
        return self.uc.post(url, query=_query, json_data=_payload, parse_response=False)

    def create_temp_trigger(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/trigger/ops-create-temp-trigger"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def get_trigger(self, query=None, **args):
        '''
        Arguments:
        - triggerid: triggerid 
        - triggername: triggername 
        '''
        url="/resources/trigger"
        field_mapping={
            "triggerid": "triggerid", 
            "triggername": "triggername", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_trigger(self, payload=None, **args):
        url="/resources/trigger"
        field_mapping={
          "enabled": "enabled", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_trigger(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/trigger"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_trigger(self, query=None, **args):
        '''
        Arguments:
        - triggerid: triggerid 
        - triggername: triggername 
        '''
        url="/resources/trigger"
        field_mapping={
          "triggerid": "triggerid", 
          "triggername": "triggername", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_triggers(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - enabled: enabled 
        - type: type 
        - businessServices: businessServices 
        - updatedTimeType: updatedTimeType 
        - updatedTime: updatedTime 
        - workflowId: workflowId 
        - workflowName: workflowName 
        - agentName: agentName 
        - description: description 
        - tasks: tasks 
        - templateId: templateId 
        - templateName: templateName 
        '''
        url="/resources/trigger/list"
        field_mapping={
          "name": "name", 
          "enabled": "enabled", 
          "type": "type", 
          "businessServices": "businessServices", 
          "updatedTimeType": "updatedTimeType", 
          "updatedTime": "updatedTime", 
          "workflowId": "workflowId", 
          "workflowName": "workflowName", 
          "agentName": "agentName", 
          "description": "description", 
          "tasks": "tasks", 
          "templateId": "templateId", 
          "templateName": "templateName", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def list_triggers_advanced(self, query=None, **args):
        '''
        Arguments:
        - triggername: triggername 
        - type: type 
        - businessServices: businessServices 
        - enabled: enabled 
        - tasks: tasks 
        - description: description 
        '''
        url="/resources/trigger/listadv"
        field_mapping={
            "triggername": "triggername", 
            "type": "type", 
            "businessServices": "businessServices", 
            "enabled": "enabled", 
            "tasks": "tasks", 
            "description": "description", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)
    
    def enable_disable(self, payload=None, **args):
        url="/resources/trigger/ops-enable-disable-trigger"
        field_mapping={
          "enable": "enable", 
          "name": "name", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)