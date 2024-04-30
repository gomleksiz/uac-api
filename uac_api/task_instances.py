from .utils import prepare_payload, prepare_query_params
import time

# - cancel_task_instance(instance_id)
# - clear_all_dependencies(instance_id)
# - clear_exclusive_dependencies(instance_id)
# - clear_instance_wait_dependencies(instance_id)
# - clear_predecessor_dependencies(instance_id)
# - clear_time_dependency(instance_id)
# - clear_virtual_resource_dependencies(instance_id)
# - delete_task_instance(instance_id)
# - force_finish_task_instance(instance_id)
# - force_finish_cancel_task_instance(instance_id)
# - hold_task_instance(instance_id)
# - issue_set_completed_command_for_manual_task_instance(instance_id)
# - issue_set_started_command_for_manual_task_instance(instance_id)
# - list_task_instances_advanced()
# - list_task_instance_variables_show_variables(instance_id)
# - release_task_from_hold(instance_id)
# - retrieve_task_instance_output(instance_id)
# - set_or_modify_wait_time_duration_for_task_instance(instance_id, wait_time)
# - set_priority_for_task_instance(instance_id, priority)
# - skip_task_instance(instance_id)
# - skip_task_instance_path(instance_id)
# - unskip_task_instance(instance_id)

class TaskInstances:
    FINAL_STATUS = ["SUCCESS", "FAILED", "CANCELLED", "SKIPPED", "FINISHED"]
    SUCCESS_STATUS = ["SUCCESS", "FINISHED", "SKIPPED"]
    FAILED_STATUS = ["FAILED", "CANCELLED"]
    def __init__(self, uc) -> None:
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc
        
    def delete_task_instance(self, query=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def show_variables(self, query=None, **args):
        '''
        Arguments:
        - taskinstancename: taskinstancename 
        - taskinstanceid: taskinstanceid 
        - workflowinstancename: workflowinstancename 
        - criteria: criteria 
        - fetchglobal: fetchglobal 
        '''
        url="/resources/taskinstance/showvariables"
        field_mapping={
            "taskinstancename": "taskinstancename", 
            "taskinstanceid": "taskinstanceid", 
            "workflowinstancename": "workflowinstancename", 
            "criteria": "criteria", 
            "fetchglobal": "fetchglobal", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_operational_memo(self, query=None, **args):
        url="/resources/taskinstance/updatememo"
        field_mapping={
            "taskinstancename": "taskinstancename", 
            "taskinstanceid": "taskinstanceid", 
            "workflowinstancename": "workflowinstancename", 
            "criteria": "criteria"
        }
        parameters = prepare_query_params(query, field_mapping, args)
        print(args)
        payload = args.pop("memo", "")
        return self.uc.put(url, json_data=payload, query=parameters, headers={"Content-Type": "text/plain", "Accept": "text/plain"}, parse_response=False)

    def set_priority(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/setpriority"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def set_timewait(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/settimewait"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def list_dependency_list(self, query=None, **args):
        '''
        Arguments:
        - taskinstancename: taskinstancename 
        - taskinstanceid: taskinstanceid 
        - workflowinstancename: workflowinstancename 
        - criteria: criteria 
        - dependencytype: dependencytype 
        '''
        url="/resources/taskinstance/dependency/list"
        field_mapping={
            "taskinstancename": "taskinstancename", 
            "taskinstanceid": "taskinstanceid", 
            "workflowinstancename": "workflowinstancename", 
            "criteria": "criteria", 
            "dependencytype": "dependencytype", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def task_insert(self, payload=None, **args):
        '''
        Arguments:
        - id: id 
        - name: name 
        - alias: alias 
        - workflowInstanceId: workflowInstanceId 
        - workflowInstanceName: workflowInstanceName 
        - workflowInstanceCriteria: workflowInstanceCriteria 
        - predecessors: predecessors 
        - successors: successors 
        - vertexX: vertexX 
        - vertexY: vertexY 
        - inheritTriggerTime: inheritTriggerTime 
        '''
        url="/resources/taskinstance/ops-task-insert"
        field_mapping={
          "id": "id", 
          "name": "name", 
          "alias": "alias", 
          "workflowInstanceId": "workflowInstanceId", 
          "workflowInstanceName": "workflowInstanceName", 
          "workflowInstanceCriteria": "workflowInstanceCriteria", 
          "predecessors": "predecessors", 
          "successors": "successors", 
          "vertexX": "vertexX", 
          "vertexY": "vertexY", 
          "inheritTriggerTime": "inheritTriggerTime", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def cancel(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/cancel"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def clear_dependencies(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/cleardependencies"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def clear_exclusive(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/clearexclusive"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def clear_instance_wait(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/clearinstancewait"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def clear_predecessors(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/clearpredecessors"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def clear_resources(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/clearresources"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def clear_timewait(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/cleartimewait"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def force_finish(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/forcefinish"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def force_finish_cancel(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/forcefinishcancel"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def hold(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/hold"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def release(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/release"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def rerun(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/rerun"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def retrieve_output(self, query=None, **args):
        '''
        Arguments:
        - taskinstancename: taskinstancename 
        - taskinstanceid: taskinstanceid 
        - workflowinstancename: workflowinstancename 
        - criteria: criteria 
        - outputtype: outputtype 
        - startline: startline 
        - numlines: numlines 
        - scantext: scantext 
        - operationalMemo: operationalMemo 
        '''
        url="/resources/taskinstance/retrieveoutput"
        field_mapping={
            "taskinstancename": "taskinstancename", 
            "taskinstanceid": "taskinstanceid", 
            "workflowinstancename": "workflowinstancename", 
            "criteria": "criteria", 
            "outputtype": "outputtype", 
            "startline": "startline", 
            "numlines": "numlines", 
            "scantext": "scantext", 
            "operationalMemo": "operationalMemo", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def skip(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/skip"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def skip_path(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/skippath"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def unskip(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: id 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        '''
        url="/resources/taskinstance/unskip"
        field_mapping={
          "name": "name", 
          "id": "id", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def list_status(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - id: sysId 
        - criteria: criteria 
        - workflowInstanceName: workflowInstanceName 
        - resourceName: resourceName 
        - recursive: recursive 
        - predecessorName: predecessorName 
        - waitType: waitType 
        - waitTime: waitTime 
        - waitDuration: waitDuration 
        - waitSeconds: waitSeconds 
        - waitDayConstraint: waitDayConstraint 
        - delayType: delayType 
        - delayDuration: delayDuration 
        - delaySeconds: delaySeconds 
        - halt: halt 
        - priorityType: priorityType 
        - taskStatus: taskStatus 
        - operationalMemo: operationalMemo 
        - holdReason: holdReason 
        - agentName: agentName 
        - workflowInstanceCriteria: workflowInstanceCriteria 
        - workflowInstanceId: workflowInstanceId 
        - status: status 
        - type: type 
        - executionUser: executionUser 
        - lateStart: lateStart 
        - lateFinish: lateFinish 
        - earlyFinish: earlyFinish 
        - startedLate: startedLate 
        - finishedLate: finishedLate 
        - finishedEarly: finishedEarly 
        - late: late 
        - lateEarly: lateEarly 
        - businessServices: businessServices 
        - updatedTimeType: updatedTimeType 
        - updatedTime: updatedTime 
        - sysId: sysId 
        - instanceNumber: instanceNumber 
        - taskId: taskId 
        - taskName: taskName 
        - customField1: customField1 
        - customField2: customField2 
        - triggerId: triggerId 
        - triggerName: triggerName 
        - workflowDefinitionId: workflowDefinitionId 
        - workflowDefinitionName: workflowDefinitionName 
        - statusDescription: statusDescription 
        - templateId: templateId 
        - templateName: templateName 
        - responseFields: responseFields 
        - instanceOutputType: instanceOutputType 
        '''
        url="/resources/taskinstance/list"
        field_mapping={
          "name": "name", 
          "id": "sysId", 
          "criteria": "criteria", 
          "workflowInstanceName": "workflowInstanceName", 
          "resourceName": "resourceName", 
          "recursive": "recursive", 
          "predecessorName": "predecessorName", 
          "waitType": "waitType", 
          "waitTime": "waitTime", 
          "waitDuration": "waitDuration", 
          "waitSeconds": "waitSeconds", 
          "waitDayConstraint": "waitDayConstraint", 
          "delayType": "delayType", 
          "delayDuration": "delayDuration", 
          "delaySeconds": "delaySeconds", 
          "halt": "halt", 
          "priorityType": "priorityType", 
          "taskStatus": "taskStatus", 
          "operationalMemo": "operationalMemo", 
          "holdReason": "holdReason", 
          "agentName": "agentName", 
          "workflowInstanceCriteria": "workflowInstanceCriteria", 
          "workflowInstanceId": "workflowInstanceId", 
          "status": "status", 
          "type": "type", 
          "executionUser": "executionUser", 
          "lateStart": "lateStart", 
          "lateFinish": "lateFinish", 
          "earlyFinish": "earlyFinish", 
          "startedLate": "startedLate", 
          "finishedLate": "finishedLate", 
          "finishedEarly": "finishedEarly", 
          "late": "late", 
          "lateEarly": "lateEarly", 
          "businessServices": "businessServices", 
          "updatedTimeType": "updatedTimeType", 
          "updatedTime": "updatedTime", 
          "sysId": "sysId", 
          "instanceNumber": "instanceNumber", 
          "taskId": "taskId", 
          "taskName": "taskName", 
          "customField1": "customField1", 
          "customField2": "customField2", 
          "triggerId": "triggerId", 
          "triggerName": "triggerName", 
          "workflowDefinitionId": "workflowDefinitionId", 
          "workflowDefinitionName": "workflowDefinitionName", 
          "statusDescription": "statusDescription", 
          "templateId": "templateId", 
          "templateName": "templateName", 
          "responseFields": "responseFields", 
          "instanceOutputType": "instanceOutputType", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)
    
  
    def wait_for_status(self, id, statuses=FINAL_STATUS, timeout=300, interval=10):
        '''
        Arguments:
        - task_instance_id: task_instance_id 
        - statuses: statuses 
        - timeout: timeout 
        - interval: interval 
        '''
        start_time = time.time()
        
        completed = False
        while not completed:
            response = self.list_status(id=id, status=",".join(statuses))
            if len(response) > 0:
                return response[0]
            else:
                if time.time() - start_time > timeout:
                    raise Exception("Timeout")
                self.log.debug("Waiting for task instance to complete")
                time.sleep(interval)
                