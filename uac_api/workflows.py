# - insert_task_into_workflow_with_dependencies(workflow_id, task_data, dependencies)
# - list_predecessors_successors_of_task_instance_in_a_workflow(workflow_id, instance_id)
# - create_workflow(workflow_data)
# - list_workflow_forecast(workflow_id)
# - modify_workflow(workflow_id, **kwargs)
# - read_workflow(workflow_id)
from .utils import prepare_payload, prepare_query_params

class Workflows:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_edges(self, query=None, **args):
        '''
        Arguments:
        - workflowid: workflowid 
        - workflowname: workflowname 
        - sourceid: sourceid 
        - targetid: targetid 
        '''
        url="/resources/workflow/edges"
        field_mapping={
            "workflowid": "workflowid", 
            "workflowname": "workflowname", 
            "sourceid": "sourceid", 
            "targetid": "targetid", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_edge(self, payload=None, **args):
        url="/resources/workflow/edges"
        _payload = payload
        return self.uc.put(url, json_data=_payload)

    def add_edge(self, payload=None, **args):
        '''
        Arguments:
        - workflowid: workflowid 
        - workflowname: workflowname 
        - condition: condition 
        - straightEdge: straightEdge 
        - points: points 
        - sourceId: sourceId 
        - targetId: targetId 
        '''
        url="/resources/workflow/edges"
        field_mapping={
          "workflowid": "workflowid", 
          "workflowname": "workflowname", 
          "condition": "condition", 
          "straightEdge": "straightEdge", 
          "points": "points", 
          "sourceId": "sourceId", 
          "targetId": "targetId", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def delete_edge(self, query=None, **args):
        '''
        Arguments:
        - workflowid: workflowid 
        - workflowname: workflowname 
        - sourceid: sourceid 
        - targetid: targetid 
        '''
        url="/resources/workflow/edges"
        field_mapping={
          "workflowid": "workflowid", 
          "workflowname": "workflowname", 
          "sourceid": "sourceid", 
          "targetid": "targetid", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def get_vertices(self, query=None, **args):
        '''
        Arguments:
        - workflowid: workflowid 
        - workflowname: workflowname 
        - taskid: taskid 
        - taskname: taskname 
        - taskalias: taskalias 
        - vertexid: vertexid 
        '''
        url="/resources/workflow/vertices"
        field_mapping={
            "workflowid": "workflowid", 
            "workflowname": "workflowname", 
            "taskid": "taskid", 
            "taskname": "taskname", 
            "taskalias": "taskalias", 
            "vertexid": "vertexid", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_vertex(self, payload=None, **args):
        url="/resources/workflow/vertices"
        _payload = payload
        return self.uc.put(url, json_data=_payload)

    def add_vertex(self, payload=None, **args):
        '''
        Arguments:
        - workflowid: workflowid 
        - workflowname: workflowname 
        - task: task 
        - alias: alias 
        - vertexId: vertexId 
        - vertexX: vertexX 
        - vertexY: vertexY 
        '''
        url="/resources/workflow/vertices"
        field_mapping={
          "workflowid": "workflowid", 
          "workflowname": "workflowname", 
          "task": "task", 
          "alias": "alias", 
          "vertexId": "vertexId", 
          "vertexX": "vertexX", 
          "vertexY": "vertexY", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def delete_vertices(self, query=None, **args):
        '''
        Arguments:
        - workflowid: workflowid 
        - workflowname: workflowname 
        - taskid: taskid 
        - taskname: taskname 
        - taskalias: taskalias 
        - vertexid: vertexid 
        '''
        url="/resources/workflow/vertices"
        field_mapping={
          "workflowid": "workflowid", 
          "workflowname": "workflowname", 
          "taskid": "taskid", 
          "taskname": "taskname", 
          "taskalias": "taskalias", 
          "vertexid": "vertexid", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def get_forecast(self, query=None, **args):
        '''
        Arguments:
        - workflowid: workflowid 
        - workflowname: workflowname 
        - calendarid: calendarid 
        - calendarname: calendarname 
        - triggerid: triggerid 
        - triggername: triggername 
        - date: date 
        - time: time 
        - timezone: timezone 
        - forecastTimezone: forecastTimezone 
        - exclude: exclude 
        - variable: variable 
        '''
        url="/resources/workflow/forecast"
        field_mapping={
            "workflowid": "workflowid", 
            "workflowname": "workflowname", 
            "calendarid": "calendarid", 
            "calendarname": "calendarname", 
            "triggerid": "triggerid", 
            "triggername": "triggername", 
            "date": "date", 
            "time": "time", 
            "timezone": "timezone", 
            "forecastTimezone": "forecastTimezone", 
            "exclude": "exclude", 
            "variable": "variable", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)
