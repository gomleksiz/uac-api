# - create_update_simulation(simulation_data)
# - delete_simulation(simulation_id)
# - list_simulations()
# - read_simulation(simulation_id)
from .utils import prepare_payload, prepare_query_params

class Simulations:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_simulation(self, query=None, **args):
        '''
        Arguments:
        - simulationid: simulationid 
        - taskname: taskname 
        - workflowname: workflowname 
        - vertexid: vertexid 
        '''
        url="/resources/simulation"
        field_mapping={
            "simulationid": "simulationid", 
            "taskname": "taskname", 
            "workflowname": "workflowname", 
            "vertexid": "vertexid", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_simulation(self, payload=None, **args):
        url="/resources/simulation"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_simulation(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/simulation"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_simulation(self, query=None, **args):
        '''
        Arguments:
        - simulationid: simulationid 
        - taskname: taskname 
        - workflowname: workflowname 
        - vertexid: vertexid 
        '''
        url="/resources/simulation"
        field_mapping={
          "simulationid": "simulationid", 
          "taskname": "taskname", 
          "workflowname": "workflowname", 
          "vertexid": "vertexid", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_simulations(self, query=None, **args):
        '''
        Arguments:
        - taskname: taskname 
        - workflowname: workflowname 
        '''
        url="/resources/simulation/list"
        field_mapping={
            "taskname": "taskname", 
            "workflowname": "workflowname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)
