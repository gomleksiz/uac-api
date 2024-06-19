from .utils import prepare_payload, prepare_query_params, prepare_query_payload, safe_str_to_int

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
    
    def add_child_vertex(self, workflow_name, task_name, parent_task_name=None, parent_vertex_id=None, vertex_id=None, auto_arrange=True):
        '''
        Arguments:
        - workflow_name: workflowname 
        - parent_task_name
        - task_name: task 
        - auto_arrange: True
        '''
        if parent_vertex_id:
          parent_vertex_id = str(parent_vertex_id)
          response = self.get_vertices(workflowname=workflow_name, vertex_id=parent_vertex_id)
        else:
          response = self.get_vertices(workflowname=workflow_name, taskname=parent_task_name)
          parent_vertex_id = response[0]["vertexId"]
        
        if vertex_id:
          new_vertex_id = str(vertex_id)
          response = self.add_vertex(workflowname=workflow_name, task=task_name, vertex_id=new_vertex_id)
        else:
          response = self.add_vertex(workflowname=workflow_name, task=task_name)
          new_vertex_id = response["vertexId"]
        
        response = self.add_edge(workflowname=workflow_name, sourceid=parent_vertex_id, targetid=new_vertex_id)
        if auto_arrange:
            _ = self.auto_arrange_vertices(workflow_name=workflow_name)
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
        return self.uc.delete(url, query=parameters)
  
    def auto_arrange_vertices(self, workflow_name=None, payload=None):
        if payload:
            workflow = payload
        else:
            workflow = self.uc.tasks.get_task(task_name=workflow_name)
        
        from .utils_workflow import WorkflowsVertexPositions
        positions = WorkflowsVertexPositions(workflow.get("workflowEdges", [])).get_vertex_positions()

        vertices = workflow.get("workflowVertices", [])
        large = (150, 135)
        compact = (130, 100)
        spacing = large
        for vertex in vertices:
            id = vertex['vertexId']
            current_x = safe_str_to_int(vertex['vertexX'])
            current_y = safe_str_to_int(vertex['vertexY'])
            x = int(positions[id][0] * spacing[0] + 45)
            y = int(positions[id][1] * spacing[1] + 30)
            if current_x != x or current_y != y:
                self.log.debug(f"VertexId {id} X: {vertex['vertexX']}=>{x} Y: {vertex['vertexY']}=>{y}")
                vertex['vertexX'] = str(x)
                vertex['vertexY'] = str(y)
        if payload:
            return workflow
        else:
            return self.uc.tasks.update_task(payload=workflow)

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
