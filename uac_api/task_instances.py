import time

from .utils import prepare_payload, prepare_query_params, prepare_query_payload

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
    class Status:
        ACTION_REQUIRED = 60
        CANCEL_PENDING = 99
        CANCELLED = 130
        CONFIRMATION_REQUIRED = 125
        DEFINED = 0
        EXCLUSIVE_REQUESTED = 22
        EXCLUSIVE_WAIT = 23
        EXECUTION_WAIT = 33
        FAILED = 140
        FINISHED = 190
        HELD = 20
        IN_DOUBT = 110
        QUEUED = 40
        RESOURCE_REQUESTED = 25
        RESOURCE_WAIT = 30
        RUNNING = 80
        RUNNING_PROBLEMS = 81
        SKIPPED = 180
        START_FAILURE = 120
        STARTED = 70
        SUBMITTED = 43
        SUCCESS = 200
        TIME_WAIT = 15
        UNDELIVERABLE = 35
        WAITING = 10

    class StatusValue:
        ACTION_REQUIRED = "ACTION_REQUIRED"
        CANCEL_PENDING = "CANCEL_PENDING"
        CANCELLED = "CANCELLED"
        CONFIRMATION_REQUIRED = "CONFIRMATION_REQUIRED"
        DEFINED = "DEFINED"
        EXCLUSIVE_REQUESTED = "EXCLUSIVE_REQUESTED"
        EXCLUSIVE_WAIT = "EXCLUSIVE_WAIT"
        EXECUTION_WAIT = "EXECUTION_WAIT"
        FAILED = "FAILED"
        FINISHED = "FINISHED"
        HELD = "HELD"
        IN_DOUBT = "IN_DOUBT"
        QUEUED = "QUEUED"
        RESOURCE_REQUESTED = "RESOURCE_REQUESTED"
        RESOURCE_WAIT = "RESOURCE_WAIT"
        RUNNING = "RUNNING"
        RUNNING_PROBLEMS = "RUNNING/PROBLEMS"
        SKIPPED = "SKIPPED"
        START_FAILURE = "START_FAILURE"
        STARTED = "STARTED"
        SUBMITTED = "SUBMITTED"
        SUCCESS = "SUCCESS"
        TIME_WAIT = "TIME_WAIT"
        UNDELIVERABLE = "UNDELIVERABLE"
        WAITING = "WAITING"

    FINAL_STATUS = [
        "SUCCESS",
        "SKIPPED",
        "FINISHED",
        "START_FAILURE",
        "UNDELIVERABLE",
        "FAILED",
        "CANCELLED",
        "RUNNING/PROBLEMS",
        "IN_DOUBT",
    ]
    FINAL_STATUS_ID = [
        Status.START_FAILURE,
        Status.SUCCESS,
        Status.UNDELIVERABLE,
        Status.RUNNING_PROBLEMS,
        Status.SKIPPED,
        Status.IN_DOUBT,
        Status.FINISHED,
        Status.FAILED,
        Status.CANCELLED,
    ]
    SUCCESS_STATUS = ["SUCCESS", "FINISHED", "SKIPPED"]
    SUCCESS_STATUS_ID = [Status.SUCCESS, Status.FINISHED, Status.SKIPPED]
    FAILED_STATUS = [
        "FINISHED",
        "START_FAILURE",
        "UNDELIVERABLE",
        "FAILED",
        "CANCELLED",
        "RUNNING/PROBLEMS",
        "IN_DOUBT",
    ]
    FAILED_STATUS_ID = [Status.FAILED, Status.CANCELLED, Status.RUNNING_PROBLEMS]

    def __init__(self, uc) -> None:
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def delete_task_instance(self, payload=None, **args):
        """
        Arguments:
        - id: id
        - operationalMemo: operationalMemo
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        - recursive: recursive
        """
        url = "/resources/taskinstance"
        field_mapping = {
            "id": "id",
            "operationalMemo": "operationalMemo",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
            "recursive": "recursive",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.delete(url, json_data=_payload, parse_response=False)

    def show_variables(self, query=None, **args):
        """
        Arguments:
        - taskinstancename: taskinstancename
        - taskinstanceid: taskinstanceid
        - workflowinstancename: workflowinstancename
        - criteria: criteria
        - fetchglobal: fetchglobal
        """
        url = "/resources/taskinstance/showvariables"
        field_mapping = {
            "taskinstancename": "taskinstancename",
            "taskinstanceid": "taskinstanceid",
            "workflowinstancename": "workflowinstancename",
            "criteria": "criteria",
            "fetchglobal": "fetchglobal",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_operational_memo(self, query=None, **args):
        """
        Arguments:
        - memo: String containing the desired memo
        - taskinstancename: taskinstancename
        - taskinstanceid: taskinstanceid
        - workflowinstancename: workflowinstancename
        - criteria: criteria
        """
        url = "/resources/taskinstance/updatememo"
        field_mapping = {
            "taskinstancename": "taskinstancename",
            "taskinstanceid": "taskinstanceid",
            "workflowinstancename": "workflowinstancename",
            "criteria": "criteria",
        }
        payload = args.pop("memo", "")
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.put(
            url,
            json_data=payload,
            query=parameters,
            headers={"Content-Type": "text/plain", "Accept": "text/plain"},
            parse_response=False,
            plaintext_instead_of_json=True,
        )

    def set_complete(self, payload=None, **args):
        """
        Arguments:
        - name
        - id
        - workflowInstanceName
        - criteria
        - operationalMemo
        """
        url = "/resources/taskinstance/setcompleted"
        field_mapping = {
            "name": "name",
            "id": "id",
            "workflowInstanceName": "workflowInstanceName",
            "criteria": "criteria",
            "operationalMemo": "operationalMemo",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def set_started(self, payload=None, **args):
        """
        Arguments:
        - name
        - id
        - workflowInstanceName
        - criteria
        - operationalMemo
        """
        url = "/resources/taskinstance/setstarted"
        field_mapping = {
            "name": "name",
            "id": "id",
            "workflowInstanceName": "workflowInstanceName",
            "criteria": "criteria",
            "operationalMemo": "operationalMemo",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def set_priority(self, payload=None, **args):
        """
        Arguments:
        - id: id
        - operationalMemo: operationalMemo
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        - priorityType: priorityType
        """
        url = "/resources/taskinstance/setpriority"
        field_mapping = {
            "id": "id",
            "operationalMemo": "operationalMemo",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
            "priorityType": "priorityType",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def set_timewait(self, payload=None, **args):
        """
        Arguments:
        - id: id
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        - delayType: delayType
        - waitType: waitType
        - waitTime: waitTime
        - waitDayConstraint: waitDayConstraint
        - waitDuration: waitDuration
        - waitSeconds: waitSeconds
        - delayDuration: delayDuration
        - delaySeconds: delaySeconds
        - operationalMemo: operationalMemo
        """
        url = "/resources/taskinstance/settimewait"
        field_mapping = {
            "id": "id",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
            "delayType": "delayType",
            "waitType": "waitType",
            "waitTime": "waitTime",
            "waitDayConstraint": "waitDayConstraint",
            "waitDuration": "waitDuration",
            "waitSeconds": "waitSeconds",
            "delayDuration": "delayDuration",
            "delaySeconds": "delaySeconds",
            "operationalMemo": "operationalMemo",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def list_dependency_list(self, query=None, **args):
        """
        Arguments:
        - taskinstancename: taskinstancename
        - taskinstanceid: taskinstanceid
        - workflowinstancename: workflowinstancename
        - criteria: criteria
        - dependencytype: dependencytype
        """
        url = "/resources/taskinstance/dependency/list"
        field_mapping = {
            "taskinstancename": "taskinstancename",
            "taskinstanceid": "taskinstanceid",
            "workflowinstancename": "workflowinstancename",
            "criteria": "criteria",
            "dependencytype": "dependencytype",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def task_insert(self, payload=None, **args):
        """
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
        - variables: variables
        """
        url = "/resources/taskinstance/ops-task-insert"
        field_mapping = {
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
            "variables": "variables",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def cancel(self, payload=None, **args):
        """
        Arguments:
        - id: id
        - operationalMemo: operationalMemo
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        """
        url = "/resources/taskinstance/cancel"
        field_mapping = {
            "id": "id",
            "operationalMemo": "operationalMemo",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def clear_dependencies(self, payload=None, **args):
        """
        Arguments:
        - id: id
        - operationalMemo: operationalMemo
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        """
        url = "/resources/taskinstance/cleardependencies"
        field_mapping = {
            "id": "id",
            "operationalMemo": "operationalMemo",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def clear_exclusive(self, payload=None, **args):
        """
        Arguments:
        - id: id
        - operationalMemo: operationalMemo
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        """
        url = "/resources/taskinstance/clearexclusive"
        field_mapping = {
            "id": "id",
            "operationalMemo": "operationalMemo",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def clear_instance_wait(self, payload=None, **args):
        """
        Arguments:
        - id: id
        - operationalMemo: operationalMemo
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        """
        url = "/resources/taskinstance/clearinstancewait"
        field_mapping = {
            "id": "id",
            "operationalMemo": "operationalMemo",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def clear_predecessors(self, payload=None, **args):
        """
        Arguments:
        - predecessorName: predecessorName
        - id: id
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        - operationalMemo: operationalMemo
        """
        url = "/resources/taskinstance/clearpredecessors"
        field_mapping = {
            "predecessorName": "predecessorName",
            "id": "id",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
            "operationalMemo": "operationalMemo",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def clear_resources(self, payload=None, **args):
        """
        Arguments:
        - id: id
        - name: name
        - workflowInstanceName: workflowInstanceName
        - criteria: criteria
        - resourceName: resourceName
        - returnInUse: returnInUse
        - operationalMemo: operationalMemo
        """
        url = "/resources/taskinstance/clearresources"
        field_mapping = {
            "id": "id",
            "name": "name",
            "workflowInstanceName": "workflowInstanceName",
            "criteria": "criteria",
            "resourceName": "resourceName",
            "returnInUse": "returnInUse",
            "operationalMemo": "operationalMemo",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def clear_timewait(self, payload=None, **args):
        """
        Arguments:
        - id: id
        - operationalMemo: operationalMemo
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        """
        url = "/resources/taskinstance/cleartimewait"
        field_mapping = {
            "id": "id",
            "operationalMemo": "operationalMemo",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def force_finish(self, payload=None, **args):
        """
        Arguments:
        - id: id
        - operationalMemo: operationalMemo
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        - halt: halt
        """
        url = "/resources/taskinstance/forcefinish"
        field_mapping = {
            "id": "id",
            "operationalMemo": "operationalMemo",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
            "halt": "halt",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def force_finish_cancel(self, payload=None, **args):
        """
        Arguments:
        - id: id
        - operationalMemo: operationalMemo
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        - halt: halt
        """
        url = "/resources/taskinstance/forcefinishcancel"
        field_mapping = {
            "id": "id",
            "operationalMemo": "operationalMemo",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
            "halt": "halt",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def hold(self, payload=None, **args):
        """
        Arguments:
        - id: id
        - operationalMemo: operationalMemo
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        - holdReason: holdReason
        """
        url = "/resources/taskinstance/hold"
        field_mapping = {
            "id": "id",
            "operationalMemo": "operationalMemo",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
            "holdReason": "holdReason",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def release(self, payload=None, **args):
        """
        Arguments:
        - id: id
        - operationalMemo: operationalMemo
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        - recursive: recursive
        """
        url = "/resources/taskinstance/release"
        field_mapping = {
            "id": "id",
            "operationalMemo": "operationalMemo",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
            "recursive": "recursive",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def rerun(self, payload=None, **args):
        """
        Arguments:
        - id: id
        - operationalMemo: operationalMemo
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        - recursive: recursive
        - taskStatus: taskStatus
        """
        url = "/resources/taskinstance/rerun"
        field_mapping = {
            "id": "id",
            "operationalMemo": "operationalMemo",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
            "recursive": "recursive",
            "taskStatus": "taskStatus",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def retrieve_output(self, query=None, **args):
        """
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
        """
        url = "/resources/taskinstance/retrieveoutput"
        field_mapping = {
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
        """
        Arguments:
        - id: id
        - operationalMemo: operationalMemo
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        """
        url = "/resources/taskinstance/skip"
        field_mapping = {
            "id": "id",
            "operationalMemo": "operationalMemo",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def skip_path(self, payload=None, **args):
        """
        Arguments:
        - id: id
        - operationalMemo: operationalMemo
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        """
        url = "/resources/taskinstance/skippath"
        field_mapping = {
            "id": "id",
            "operationalMemo": "operationalMemo",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def unskip(self, payload=None, **args):
        """
        Arguments:
        - id: id
        - operationalMemo: operationalMemo
        - name: name
        - criteria: criteria
        - workflowInstanceName: workflowInstanceName
        """
        url = "/resources/taskinstance/unskip"
        field_mapping = {
            "id": "id",
            "operationalMemo": "operationalMemo",
            "name": "name",
            "criteria": "criteria",
            "workflowInstanceName": "workflowInstanceName",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def get(self, query=None, **args):
        """
        Arguments:
        taskinstancename: taskinstancename
        taskinstanceid: taskinstanceid
        workflowinstancename: workflowinstancename
        criteria: criteria
        include_output: includeOutput
        include_sql_results: includeSqlResults
        """
        url = "/resources/taskinstance"
        field_mapping = {
            "taskinstancename": "taskinstancename",
            "taskinstanceid": "taskinstanceid",
            "workflowinstancename": "workflowinstancename",
            "criteria": "criteria",
            "includeOutput": "includeOutput",
            "includeSqlResults": "includeSqlResults",
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def list_status(self, payload=None, **args):
        """
        Arguments:
        - status = status
        - type = type
        - agent_name = agentName
        - sys_id = sysId
        - name = name
        - workflow_instance_id = workflowInstanceId
        - workflow_instance_name = workflowInstanceName
        - task_id = taskId
        - task_name = taskName
        - workflow_definition_id = workflowDefinitionId
        - workflow_definition_name = workflowDefinitionName
        - trigger_id = triggerId
        - trigger_name = triggerName
        - workflow_instance_criteria = workflowInstanceCriteria
        - business_services = businessServices
        - template_id = templateId
        - template_name = templateName
        - updated_time = updatedTime
        - updated_time_type = updatedTimeType
        - instance_number = instanceNumber
        - execution_user = executionUser
        - late_start = lateStart
        - late_finish = lateFinish
        - early_finish = earlyFinish
        - started_late = startedLate
        - finished_late = finishedLate
        - finished_early = finishedEarly
        - late = late
        - late_early = lateEarly
        - custom_field1 = customField1
        - custom_field2 = customField2
        - status_description = statusDescription
        - operational_memo = operationalMemo
        - sort = sort
        """
        url = "/resources/taskinstance/list"
        field_mapping = {
            "status": "status",
            "type": "type",
            "agentName": "agentName",
            "sysId": "sysId",
            "name": "name",
            "workflowInstanceId": "workflowInstanceId",
            "workflowInstanceName": "workflowInstanceName",
            "taskId": "taskId",
            "taskName": "taskName",
            "workflowDefinitionId": "workflowDefinitionId",
            "workflowDefinitionName": "workflowDefinitionName",
            "triggerId": "triggerId",
            "triggerName": "triggerName",
            "workflowInstanceCriteria": "workflowInstanceCriteria",
            "businessServices": "businessServices",
            "templateId": "templateId",
            "templateName": "templateName",
            "updatedTime": "updatedTime",
            "updatedTimeType": "updatedTimeType",
            "instanceNumber": "instanceNumber",
            "executionUser": "executionUser",
            "lateStart": "lateStart",
            "lateFinish": "lateFinish",
            "earlyFinish": "earlyFinish",
            "startedLate": "startedLate",
            "finishedLate": "finishedLate",
            "finishedEarly": "finishedEarly",
            "late": "late",
            "lateEarly": "lateEarly",
            "customField1": "customField1",
            "customField2": "customField2",
            "statusDescription": "statusDescription",
            "operationalMemo": "operationalMemo",
            "sort": "sort",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def list_advanced(self, payload=None, **args):
        """
        Arguments:
        - operational_memo: operationalMemo
        - name: name
        - workflow_instance_id: workflowInstanceId
        - workflow_instance_name: workflowInstanceName
        - status: status
        - type: type
        - agent_name: agentName
        - sys_id: sysId
        - task_id: taskId
        - task_name: taskName
        - workflow_definition_id: workflowDefinitionId
        - workflow_definition_name: workflowDefinitionName
        - trigger_id: triggerId
        - trigger_name: triggerName
        - workflow_instance_criteria: workflowInstanceCriteria
        - business_services: businessServices
        - template_id: templateId
        - template_name: templateName
        - updated_time: updatedTime
        - updated_time_type: updatedTimeType
        - instance_output_type: instanceOutputType
        - instance_number: instanceNumber
        - response_fields: responseFields
        - execution_user: executionUser
        - late_start: lateStart
        - late_finish: lateFinish
        - early_finish: earlyFinish
        - started_late: startedLate
        - finished_late: finishedLate
        - finished_early: finishedEarly
        - late: late
        - late_early: lateEarly
        - custom_field1: customField1
        - custom_field2: customField2
        - status_description: statusDescription
        - sort: sort
        """
        url = "/resources/taskinstance/listadv"
        field_mapping = {
            "operationalMemo": "operationalMemo",
            "name": "name",
            "workflowInstanceId": "workflowInstanceId",
            "workflowInstanceName": "workflowInstanceName",
            "status": "status",
            "type": "type",
            "agentName": "agentName",
            "sysId": "sysId",
            "taskId": "taskId",
            "taskName": "taskName",
            "workflowDefinitionId": "workflowDefinitionId",
            "workflowDefinitionName": "workflowDefinitionName",
            "triggerId": "triggerId",
            "triggerName": "triggerName",
            "workflowInstanceCriteria": "workflowInstanceCriteria",
            "businessServices": "businessServices",
            "templateId": "templateId",
            "templateName": "templateName",
            "updatedTime": "updatedTime",
            "updatedTimeType": "updatedTimeType",
            "instanceOutputType": "instanceOutputType",
            "instanceNumber": "instanceNumber",
            "responseFields": "responseFields",
            "executionUser": "executionUser",
            "lateStart": "lateStart",
            "lateFinish": "lateFinish",
            "earlyFinish": "earlyFinish",
            "startedLate": "startedLate",
            "finishedLate": "finishedLate",
            "finishedEarly": "finishedEarly",
            "late": "late",
            "lateEarly": "lateEarly",
            "customField1": "customField1",
            "customField2": "customField2",
            "statusDescription": "statusDescription",
            "sort": "sort",
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def wait_for_status(self, id, statuses=FINAL_STATUS, timeout=300, interval=10):
        """
        Arguments:
        - task_instance_id: task_instance_id
        - statuses: statuses
        - timeout: timeout
        - interval: interval
        """
        start_time = time.time()

        completed = False
        while not completed:
            response = self.list_status(sys_id=id, status=",".join(statuses))
            if len(response) > 0:
                return response[0]
            else:
                if time.time() - start_time > timeout:
                    raise Exception("Timeout")
                self.log.debug("Waiting for task instance to complete")
                time.sleep(interval)

    def set_task_instance_variable(self, query=None, **args):
        """
        Arguments:
        - variablevalue: String containing the desired value
        - taskinstancename: taskinstancename
        - taskinstanceid: taskinstanceid
        - workflowinstancename: workflowinstancename
        - criteria: criteria
        - variablename: variablename
        """
        url = "/resources/taskinstance/variable"
        field_mapping = {
            "taskinstancename": "taskinstancename",
            "taskinstanceid": "taskinstanceid",
            "workflowinstancename": "workflowinstancename",
            "criteria": "criteria",
            "variablename": "variablename",
        }
        payload = args.pop("variablevalue", "")
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.put(
            url,
            json_data=payload,
            query=parameters,
            headers={"Accept": "application/json", "Content-Type": "text/plain"},
            parse_response=True,
            plaintext_instead_of_json=True,
        )

    def patch_task_instance(
        self, query=None, payload=None, taskinstanceid=None, **args
    ):
        """
        Arguments:
        - taskinstanceid: taskInstanceId
        - scope: scope  -- Only the 'fields' scope is supported as of UC 7.9
        """
        url = f"/resources/taskinstance/{taskinstanceid}"
        query_fields = {
            "scope": "scope",
        }
        payload_fields = {
            "version": "version",
            "sysId": "sysId",
            "excludeRelated": "excludeRelated",
            "exportReleaseLevel": "exportReleaseLevel",
            "exportTable": "exportTable",
            "notes": "notes",
            "actions": "actions",
            "outputs": "outputs",
            "retainSysIds": "retainSysIds",
            "name": "name",
            "resolveNameImmediately": "resolveNameImmediately",
            "summary": "summary",
            "startHeld": "startHeld",
            "startHeldReason": "startHeldReason",
            "resPriority": "resPriority",
            "resPriorityVar": "resPriorityVar",
            "holdResources": "holdResources",
            "credentials": "credentials",
            "credentialsVar": "credentialsVar",
            "credentialsVarCheck": "credentialsVarCheck",
            "retryMaximum": "retryMaximum",
            "retryIndefinitely": "retryIndefinitely",
            "retryInterval": "retryInterval",
            "retrySuppressFailure": "retrySuppressFailure",
            "lsEnabled": "lsEnabled",
            "lsType": "lsType",
            "lsTime": "lsTime",
            "lsDayConstraint": "lsDayConstraint",
            "lsNthAmount": "lsNthAmount",
            "lsDuration": "lsDuration",
            "lfEnabled": "lfEnabled",
            "lfType": "lfType",
            "lfTime": "lfTime",
            "lfDayConstraint": "lfDayConstraint",
            "lfNthAmount": "lfNthAmount",
            "lfDuration": "lfDuration",
            "lfOffsetType": "lfOffsetType",
            "lfOffsetPercentage": "lfOffsetPercentage",
            "lfOffsetDuration": "lfOffsetDuration",
            "lfOffsetDurationUnit": "lfOffsetDurationUnit",
            "efEnabled": "efEnabled",
            "efType": "efType",
            "efTime": "efTime",
            "efDayConstraint": "efDayConstraint",
            "efNthAmount": "efNthAmount",
            "efDuration": "efDuration",
            "efOffsetType": "efOffsetType",
            "efOffsetPercentage": "efOffsetPercentage",
            "efOffsetDuration": "efOffsetDuration",
            "efOffsetDurationUnit": "efOffsetDurationUnit",
            "userEstimatedDuration": "userEstimatedDuration",
            "cpDuration": "cpDuration",
            "cpDurationUnit": "cpDurationUnit",
            "twWaitType": "twWaitType",
            "twWaitAmount": "twWaitAmount",
            "twWaitTime": "twWaitTime",
            "twWaitDuration": "twWaitDuration",
            "twWaitDayConstraint": "twWaitDayConstraint",
            "twDelayType": "twDelayType",
            "twDelayAmount": "twDelayAmount",
            "twDelayDuration": "twDelayDuration",
            "twWorkflowOnly": "twWorkflowOnly",
            "customField1": "customField1",
            "customField2": "customField2",
            "executionRestriction": "executionRestriction",
            "restrictionPeriod": "restrictionPeriod",
            "restrictionPeriodBeforeDate": "restrictionPeriodBeforeDate",
            "restrictionPeriodAfterDate": "restrictionPeriodAfterDate",
            "restrictionPeriodBeforeTime": "restrictionPeriodBeforeTime",
            "restrictionPeriodAfterTime": "restrictionPeriodAfterTime",
            "restrictionPeriodDateList": "restrictionPeriodDateList",
            "logLevel": "logLevel",
            "exclusiveWithSelf": "exclusiveWithSelf",
            "avgRunTime": "avgRunTime",
            "avgRunTimeDisplay": "avgRunTimeDisplay",
            "simulation": "simulation",
            "acquiredAgent": "acquiredAgent",
            "acquiredAgentCluster": "acquiredAgentCluster",
            "attemptCount": "attemptCount",
            "avgEstimatedEnd": "avgEstimatedEnd",
            "calendar": "calendar",
            "cpuTime": "cpuTime",
            "critical": "critical",
            "criticalEndpoint": "criticalEndpoint",
            "durationSeconds": "durationSeconds",
            "earlyFinish": "earlyFinish",
            "endTime": "endTime",
            "exclusiveState": "exclusiveState",
            "executionUser": "executionUser",
            "exitCode": "exitCode",
            "extensionStatus": "extensionStatus",
            "highEstimatedEnd": "highEstimatedEnd",
            "instanceWaitResolved": "instanceWaitResolved",
            "instanceWaitLookupResolved": "instanceWaitLookupResolved",
            "instanceWaitState": "instanceWaitState",
            "invokedBy": "invokedBy",
            "ioOther": "ioOther",
            "ioReads": "ioReads",
            "ioWrites": "ioWrites",
            "lateFinish": "lateFinish",
            "lateStart": "lateStart",
            "launchSource": "launchSource",
            "launchTime": "launchTime",
            "lfComputedTime": "lfComputedTime",
            "lowEstimatedEnd": "lowEstimatedEnd",
            "lsComputedTime": "lsComputedTime",
            "memo": "memo",
            "memoHistory": "memoHistory",
            "memoryPeak": "memoryPeak",
            "memoryUsed": "memoryUsed",
            "percentDone": "percentDone",
            "priority": "priority",
            "projectedEndTime": "projectedEndTime",
            "projectedLate": "projectedLate",
            "projectedStartTime": "projectedStartTime",
            "queuedTime": "queuedTime",
            "rdExcludeBackup": "rdExcludeBackup",
            "resState": "resState",
            "resourcesConsumed": "resourcesConsumed",
            "retentionTime": "retentionTime",
            "retryCounter": "retryCounter",
            "retryTime": "retryTime",
            "runCalled": "runCalled",
            "securityName": "securityName",
            "sourceInstance": "sourceInstance",
            "sourceVersion": "sourceVersion",
            "startTime": "startTime",
            "stateChangedTime": "stateChangedTime",
            "statusAttributes": "statusAttributes",
            "statusCode": "statusCode",
            "statusDescription": "statusDescription",
            "statusHistory": "statusHistory",
            "task": "task",
            "taskId": "taskId",
            "instanceNumber": "instanceNumber",
            "timeZone": "timeZone",
            "topLevelWorkflow": "topLevelWorkflow",
            "trigger": "trigger",
            "triggerTime": "triggerTime",
            "twState": "twState",
            "twUntilTime": "twUntilTime",
            "userEstimatedEnd": "userEstimatedEnd",
            "vertexId": "vertexId",
            "waitForExclusive": "waitForExclusive",
            "waitForResources": "waitForResources",
            "wfProgress": "wfProgress",
            "workflowDefinition": "workflowDefinition",
            "workflow": "workflow",
            "workflowStartTime": "workflowStartTime",
            "timeZonePref": "timeZonePref",
            "virtualResources": "virtualResources",
            "exclusiveRequests": "exclusiveRequests",
            "type": "type",
        }
        _query, _payload = prepare_query_payload(
            query, query_fields, payload, payload_fields, args
        )
        return self.uc.patch(
            url,
            json_data=_payload,
            query=_query,
            headers={"Content-Type": "application/json", "Accept": "application/json"},
            parse_response=True,
        )

    def approval_reject(self, query=None, **args):
        """
        Reject a Task Instance Approval

        Arguments:
        - taskinstancename: taskinstancename
        - taskinstanceid: taskinstanceid
        - workflowinstancename: workflowinstancename
        - criteria: criteria
        """

        url = "/resources/taskinstance/approval/reject"
        field_mapping = {
            "taskinstancename": "taskinstancename",
            "taskinstanceid": "taskinstanceid",
            "workflowinstancename": "workflowinstancename",
            "criteria": "criteria",
        }
        _query = prepare_query_params(query, field_mapping, args)
        return self.uc.put(url, query=_query, json_data=None, parse_response=True)

    def approval_approve(self, query=None, **args):
        """
        Approve a Task Instance Approval

        Arguments:
        - taskinstancename: taskinstancename
        - taskinstanceid: taskinstanceid
        - workflowinstancename: workflowinstancename
        - criteria: criteria
        """
        url = "/resources/taskinstance/approval/approve"
        field_mapping = {
            "taskinstancename": "taskinstancename",
            "taskinstanceid": "taskinstanceid",
            "workflowinstancename": "workflowinstancename",
            "criteria": "criteria",
        }
        _query = prepare_query_params(query, field_mapping, args)
        return self.uc.put(url, query=_query, json_data=None, parse_response=True)
