from .utils import prepare_query_params, prepare_payload

# - create_global_variable(variable_data)
# - delete_global_variable(variable_name)
# - list_variables()
# - list_variables_advanced()
# - modify_global_variable(variable_name, **kwargs)
# - read_global_variable(variable_name)
# - set_variables(variable_data)

class Variables:
    def __init__(self, uc) -> None:
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc


    def get_variable(self, query=None, **args):
        '''
        Arguments:
        - variableid: variableid 
        - variablename: variablename 
        '''
        url="/resources/variable"
        field_mapping={
            "variableid": "variableid", 
            "variablename": "variablename", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_variable(self, payload=None, **args):
        url="/resources/variable"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_variable(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/variable"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_variable(self, query=None, **args):
        '''
        Arguments:
        - variableid: variableid 
        - variablename: variablename 
        '''
        url="/resources/variable"
        field_mapping={
          "variableid": "variableid", 
          "variablename": "variablename", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_variables(self, payload=None, **args):
        '''
        Arguments:
        - variableName: variableName 
        - scope: scope 
        - taskName: taskName 
        - triggerName: triggerName 
        '''
        url="/resources/variable/list"
        field_mapping={
          "variableName": "variableName", 
          "scope": "scope", 
          "taskName": "taskName", 
          "triggerName": "triggerName", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def list_variables_advanced(self, query=None, **args):
        '''
        Arguments:
        - scope: scope 
        - variablename: variablename 
        - taskname: taskname 
        - triggername: triggername 
        - businessServices: businessServices 
        '''
        url="/resources/variable/listadv"
        field_mapping={
            "scope": "scope", 
            "variablename": "variablename", 
            "taskname": "taskname", 
            "triggername": "triggername", 
            "businessServices": "businessServices", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def variable_set(self, payload=None, **args):
        '''
        Arguments:
        - scope: scope 
        - create: create 
        - trigger: trigger 
        - task: task 
        - variable: variable 
        '''
        url="/resources/variable/ops-variable-set"
        field_mapping={
          "scope": "scope", 
          "create": "create", 
          "trigger": "trigger", 
          "task": "task", 
          "variable": "variable", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)