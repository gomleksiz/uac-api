from .utils import prepare_query_params, prepare_payload

# - create_task(task_data)
# - delete_task(task_id)
# - launch_task(task_id)
# - list_tasks()
# - list_tasks_advanced()
# - modify_task(task_id, **kwargs)
# - read_task(task_id)

class Tasks:
    def __init__(self, uc) -> None:
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_task(self, query=None, **args):
        '''
        Arguments:
        - taskid: taskid 
        - taskname: taskname 
        '''
        url="/resources/task"
        field_mapping={
            "taskid": "taskid", 
            "taskname": "taskname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_task(self, payload=None, **args):
        url="/resources/task"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_task(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds - False will ignore sysIds in the payload and create a new task 
        '''
        url="/resources/task"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)
    
    def clone_task(self, task_name, new_task_name):
        '''
        Copy the source task with a new name
        Arguments:
        - task_name
        - new_task_name
        '''
        payload = self.get_task(taskname=task_name)
        payload['name'] = new_task_name
        return self.create_task(payload, retainSysIds=False)

    def delete_task(self, query=None, **args):
        '''
        Arguments:
        - taskid: taskid 
        - taskname: taskname 
        '''
        url="/resources/task"
        field_mapping={
          "taskid": "taskid", 
          "taskname": "taskname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_tasks(self, payload=None, **args):
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
        url="/resources/task/list"
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

    def list_tasks_advanced(self, query=None, **args):
        '''
        Arguments:
        - taskname: taskname 
        - agentname: agentname 
        - type: type 
        - businessServices: businessServices 
        - workflowname: workflowname 
        - workflowid: workflowid 
        - updatedTime: updatedTime 
        - updatedTimeType: updatedTimeType 
        - templateid: templateid 
        - templatename: templatename 
        '''
        url="/resources/task/listadv"
        field_mapping={
            "taskname": "taskname", 
            "agentname": "agentname", 
            "type": "type", 
            "businessServices": "businessServices", 
            "workflowname": "workflowname", 
            "workflowid": "workflowid", 
            "updatedTime": "updatedTime", 
            "updatedTimeType": "updatedTimeType", 
            "templateid": "templateid", 
            "templatename": "templatename", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def list_workflow_list(self, query=None, **args):
        '''
        Arguments:
        - taskname: taskname 
        - taskid: taskid 
        '''
        url="/resources/task/parent/list"
        field_mapping={
            "taskname": "taskname", 
            "taskid": "taskid", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def list_dependency_list_1(self, query=None, **args):
        '''
        Arguments:
        - taskinstancename: taskinstancename 
        - taskinstanceid: taskinstanceid 
        - workflowinstancename: workflowinstancename 
        - criteria: criteria 
        - dependencytype: dependencytype 
        '''
        url="/resources/task/dependency/list"
        field_mapping={
            "taskinstancename": "taskinstancename", 
            "taskinstanceid": "taskinstanceid", 
            "workflowinstancename": "workflowinstancename", 
            "criteria": "criteria", 
            "dependencytype": "dependencytype", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def task_launch(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - hold: hold 
        - holdReason: holdReason 
        - timeZone: timeZone 
        - virtualResourcePriority: virtualResourcePriority 
        - virtualResources: virtualResources 
        - launchReason: launchReason 
        - simulate: simulate 
        - variables: variables 
        - variablesMap: variablesMap 
        '''
        url="/resources/task/ops-task-launch"
        field_mapping={
          "name": "name", 
          "hold": "hold", 
          "holdReason": "holdReason", 
          "timeZone": "timeZone", 
          "virtualResourcePriority": "virtualResourcePriority", 
          "virtualResources": "virtualResources", 
          "launchReason": "launchReason", 
          "simulate": "simulate", 
          "variables": "variables", 
          "variablesMap": "variablesMap", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)
  
    def task_launch_and_wait(self, payload=None, timeout=300, interval=10, **args):
        '''
        Arguments:
        - name: name 
        - hold: hold 
        - holdReason: holdReason 
        - timeZone: timeZone 
        - virtualResourcePriority: virtualResourcePriority 
        - virtualResources: virtualResources 
        - launchReason: launchReason 
        - simulate: simulate 
        - variables: variables 
        - variablesMap: variablesMap 
        '''
        url="/resources/task/ops-task-launch"
        field_mapping={
          "name": "name", 
          "hold": "hold", 
          "holdReason": "holdReason", 
          "timeZone": "timeZone", 
          "virtualResourcePriority": "virtualResourcePriority", 
          "virtualResources": "virtualResources", 
          "launchReason": "launchReason", 
          "simulate": "simulate", 
          "variables": "variables", 
          "variablesMap": "variablesMap", 
        }
        response = self.task_launch(payload=payload, **args)
        task_instan_id = response["sysId"]
        response = self.uc.task_instances.wait_for_status(id=task_instan_id, timeout=timeout, interval=interval)
        return response
