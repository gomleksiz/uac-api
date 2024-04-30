from .utils import append_if_not_none, prepare_payload, prepare_query_params

# - delete_agent(agent_id)
# - modify_agent(agent_id, **kwargs)
# - resume_agent(agent_id)
# - set_agent_task_execution_limit(agent_id, limit)
# - suspend_agent(agent_id)
# - create_agent_cluster(cluster_data)
# - delete_agent_cluster(cluster_id)
# - list_agent_clusters()
# - modify_agent_cluster(cluster_id, **kwargs)
# - read_agent_cluster(cluster_id)
# - resume_agent_cluster(cluster_id)
# - resume_agent_cluster_membership(cluster_id, agent_id)
# - return_agent_from_agent_cluster(cluster_id, agent_id)
# - set_agent_cluster_task_execution_limit(cluster_id, limit)
# - suspend_agent_cluster(cluster_id)
# - suspend_agent_cluster_membership(cluster_id, agent_id)

class Agents:
    def __init__(self, uc) -> None:
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_agent(self, query=None, **args):
        '''
        Arguments:
        - agentid: agentid 
        - agentname: agentname 
        '''
        url="/resources/agent"
        field_mapping={
            "agentid": "agentid", 
            "agentname": "agentname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_agent(self, payload=None, **args):
        url="/resources/agent"
        _payload = payload
        return self.uc.put(url, json_data=_payload)

    def delete_agent(self, query=None, **args):
        '''
        Arguments:
        - agentid: agentid 
        - agentname: agentname 
        '''
        url="/resources/agent"
        field_mapping={
          "agentid": "agentid", 
          "agentname": "agentname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_agents(self):
        url="/resources/agent/list"
        return self.uc.get(url)

    def list_agents_advanced(self, query=None, **args):
        '''
        Arguments:
        - agentname: agentname 
        - type: type 
        - businessServices: businessServices 
        '''
        url="/resources/agent/listadv"
        field_mapping={
            "agentname": "agentname", 
            "type": "type", 
            "businessServices": "businessServices", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def resume_agent(self, payload=None, **args):
        '''
        Arguments:
        - agentName: agentName 
        - agentID: agentID 
        '''
        url="/resources/agent/ops-resume-agent"
        field_mapping={
          "agentName": "agentName", 
          "agentID": "agentID", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def resume_agent_cluster_membership(self, payload=None, **args):
        '''
        Arguments:
        - agentName: agentName 
        - agentClusterName: agentClusterName 
        - agentID: agentID 
        '''
        url="/resources/agent/ops-resume-agent-cluster-membership"
        field_mapping={
          "agentName": "agentName", 
          "agentClusterName": "agentClusterName", 
          "agentID": "agentID", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def set_agent_task_execution_limit(self, payload=None, **args):
        '''
        Arguments:
        - agentName: agentName 
        - agentID: agentID 
        - limitType: limitType 
        - limitAmount: limitAmount 
        '''
        url="/resources/agent/ops-set-agent-task-execution-limit"
        field_mapping={
          "agentName": "agentName", 
          "agentID": "agentID", 
          "limitType": "limitType", 
          "limitAmount": "limitAmount", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def suspend_agent(self, payload=None, **args):
        '''
        Arguments:
        - agentName: agentName 
        - agentID: agentID 
        '''
        url="/resources/agent/ops-suspend-agent"
        field_mapping={
          "agentName": "agentName", 
          "agentID": "agentID", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def suspend_agent_cluster_membership(self, payload=None, **args):
        '''
        Arguments:
        - agentName: agentName 
        - agentClusterName: agentClusterName 
        - agentID: agentID 
        '''
        url="/resources/agent/ops-suspend-agent-cluster-membership"
        field_mapping={
          "agentName": "agentName", 
          "agentClusterName": "agentClusterName", 
          "agentID": "agentID", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

class AgentClusters:
    def __init__(self, uc) -> None:
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc
    
    def get_agent_cluster(self, query=None, **args):
        '''
        Arguments:
        - agentclusterid: agentclusterid 
        - agentclustername: agentclustername 
        '''
        url="/resources/agentcluster"
        field_mapping={
            "agentclusterid": "agentclusterid", 
            "agentclustername": "agentclustername", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)
    
    def update_agent_cluster(self, payload=None, **args):
        url="/resources/agentcluster"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_agent_cluster(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/agentcluster"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_agent_cluster(self, query=None, **args):
        '''
        Arguments:
        - agentclusterid: agentclusterid 
        - agentclustername: agentclustername 
        '''
        url="/resources/agentcluster"
        field_mapping={
          "agentclusterid": "agentclusterid", 
          "agentclustername": "agentclustername", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)
    
    def list_agent_clusters(self):
        url="/resources/agentcluster/list"
        return self.uc.get(url)

    def list_agent_clusters_advanced(self, query=None, **args):
        '''
        Arguments:
        - agentclustername: agentclustername 
        - type: type 
        - businessServices: businessServices 
        '''
        url="/resources/agentcluster/listadv"
        field_mapping={
            "agentclustername": "agentclustername", 
            "type": "type", 
            "businessServices": "businessServices", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def get_selected_agent(self, query=None, **args):
        '''
        Arguments:
        - agentclustername: agentclustername 
        - ignoreexecutionlimit: ignoreexecutionlimit 
        '''
        url="/resources/agentcluster/agent"
        field_mapping={
            "agentclustername": "agentclustername", 
            "ignoreexecutionlimit": "ignoreexecutionlimit", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def resolve_cluster(self, payload=None, **args):
        url="/resources/agentcluster/resolve"
        field_mapping={
          "agentClusterName": "agentClusterName", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def resume_cluster(self, payload=None, **args):
        url="/resources/agentcluster/resume"
        field_mapping={
          "agentClusterName": "agentClusterName", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def set_cluster_task_execution_limit(self, payload=None, **args):
        url="/resources/agentcluster/taskexecutionlimit"
        field_mapping={
          "agentClusterName": "agentClusterName", 
          "limitType": "limitType", 
          "limitAmount": "limitAmount"
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)

    def suspend_cluster(self, payload=None, **args):
        url="/resources/agentcluster/suspend"
        field_mapping={
          "agentClusterName": "agentClusterName", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)