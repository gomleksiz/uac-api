# - insert_task_into_workflow_with_dependencies(workflow_id, task_data, dependencies)
# - list_predecessors_successors_of_task_instance_in_a_workflow(workflow_id, instance_id)
# - create_workflow(workflow_data)
# - list_workflow_forecast(workflow_id)
# - modify_workflow(workflow_id, **kwargs)
# - read_workflow(workflow_id)
from .utils import prepare_payload, prepare_query_params, prepare_query_payload

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

    def add_edge(self, query=None, payload=None, **args):
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
        query_fields={
          "workflowid": "workflowid", 
          "workflowname": "workflowname", 
        }
        payload_fields={
          "condition": "condition", 
          "straightEdge": "straightEdge", 
          "points": "points", 
          "sourceId": "sourceId", 
          "targetId": "targetId", 
        }
        _query, _payload = prepare_query_payload(query, query_fields, payload, payload_fields, args)
        return self.uc.post(url, query=_query, json_data=_payload, parse_response=False)

   
    def update_edge(self, query=None, payload=None, **args):
        '''
        Arguments:
        - workflowid: workflowid 
        - workflowname: workflowname 
        - sysId: sysId 
        - workflowId: workflowId 
        - condition: condition 
        - straightEdge: straightEdge 
        - points: points 
        - sourceId: sourceId 
        - targetId: targetId 
        '''
        url="/resources/workflow/edges"
        query_fields={
          "workflowid": "workflowid", 
          "workflowname": "workflowname", 
        }
        payload_fields={
          "sysId": "sysId", 
          "workflowId": "workflowId", 
          "condition": "condition", 
          "straightEdge": "straightEdge", 
          "points": "points", 
          "sourceId": "sourceId", 
          "targetId": "targetId", 
        }
        _query, _payload = prepare_query_payload(query, query_fields, payload, payload_fields, args)
        return self.uc.put(url, query=_query, json_data=_payload, parse_response=False)

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

    def update_vertex(self, query=None, payload=None, **args):
        '''
        Arguments:
        - workflowid: workflowid 
        - workflowname: workflowname 
        - sysId: sysId 
        - workflowId: workflowId 
        - task: task 
        - alias: alias 
        - vertexId: vertexId 
        - vertexX: vertexX 
        - vertexY: vertexY 
        '''
        url="/resources/workflow/vertices"
        query_fields={
          "workflowid": "workflowid", 
          "workflowname": "workflowname", 
        }
        payload_fields={
          "sysId": "sysId", 
          "workflowId": "workflowId", 
          "task": "task", 
          "alias": "alias", 
          "vertexId": "vertexId", 
          "vertexX": "vertexX", 
          "vertexY": "vertexY", 
        }
        _query, _payload = prepare_query_payload(query, query_fields, payload, payload_fields, args)
        return self.uc.put(url, query=_query, json_data=_payload, parse_response=False)

    def add_vertex(self, query=None, payload=None, **args):
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
        query_fields={
          "workflowid": "workflowid", 
          "workflowname": "workflowname", 
        }
        payload_fields={
          "task": "task", 
          "alias": "alias", 
          "vertexId": "vertexId", 
          "vertexX": "vertexX", 
          "vertexY": "vertexY", 
        }
        _query, _payload = prepare_query_payload(query, query_fields, payload, payload_fields, args)
        return self.uc.post(url, query=_query, json_data=_payload)
    
    def add_child_vertex(self, workflow_name, parent_task_name, task_name, vertexX=None, vertexY=None, vertex_x_offset=100, vertex_y_offset=100):
        '''
        Arguments:
        - workflow_name: workflowname 
        - parent_task_name
        - task_name: task 
        - vertexX: vertexX 
        - vertexY: vertexY 
        '''
        response = self.get_vertices(workflowname=workflow_name, taskname=parent_task_name)
        parent_task_vertex_id = response[0]["vertexId"]
        if vertexX is None:
            vertexX = str(int(response[0]["vertexX"]) + vertex_x_offset)
        if vertexY is None:
            vertexY = str(int(response[0]["vertexY"]) + vertex_y_offset)

        response = self.add_vertex(workflowname=workflow_name, task=task_name, vertexX=vertexX, vertexY=vertexY)
        new_vertex_id = response["vertexId"]
        
        response = self.add_edge(workflowname=workflow_name, sourceid=parent_task_vertex_id, targetid=new_vertex_id)
        return response


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
