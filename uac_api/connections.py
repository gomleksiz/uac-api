# - database_connections()
# - email_connections()
# - email_templates()
# - peoplesoft_connections()
# - sap_connections()
# - snmp_managers()

from .utils import prepare_payload, prepare_query_params

class Connections:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_database_connection(self, query=None, **args):
        '''
        Arguments:
        - connectionid: connectionid 
        - connectionname: connectionname 
        '''
        url="/resources/databaseconnection"
        field_mapping={
            "connectionid": "connectionid", 
            "connectionname": "connectionname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_database_connection(self, payload=None, **args):
        url="/resources/databaseconnection"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_database_connection(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/databaseconnection"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_database_connection(self, query=None, **args):
        '''
        Arguments:
        - connectionid: connectionid 
        - connectionname: connectionname 
        '''
        url="/resources/databaseconnection"
        field_mapping={
          "connectionid": "connectionid", 
          "connectionname": "connectionname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_database_connections(self):
        url="/resources/databaseconnection/list"
        return self.uc.get(url)

    def get_email_connection(self, query=None, **args):
        '''
        Arguments:
        - connectionid: connectionid 
        - connectionname: connectionname 
        '''
        url="/resources/emailconnection"
        field_mapping={
            "connectionid": "connectionid", 
            "connectionname": "connectionname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_email_connection(self, payload=None, **args):
        url="/resources/emailconnection"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_email_connection(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/emailconnection"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_email_connection(self, query=None, **args):
        '''
        Arguments:
        - connectionid: connectionid 
        - connectionname: connectionname 
        '''
        url="/resources/emailconnection"
        field_mapping={
          "connectionid": "connectionid", 
          "connectionname": "connectionname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_email_connections(self):
        url="/resources/emailconnection/list"
        return self.uc.get(url)
    
    def get_peoplesoft_connection(self, query=None, **args):
        '''
        Arguments:
        - connectionid: connectionid 
        - connectionname: connectionname 
        '''
        url="/resources/peoplesoftconnection"
        field_mapping={
            "connectionid": "connectionid", 
            "connectionname": "connectionname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_peoplesoft_connection(self, payload=None, **args):
        url="/resources/peoplesoftconnection"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_peoplesoft_connection(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/peoplesoftconnection"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_peoplesoft_connection(self, query=None, **args):
        '''
        Arguments:
        - connectionid: connectionid 
        - connectionname: connectionname 
        '''
        url="/resources/peoplesoftconnection"
        field_mapping={
          "connectionid": "connectionid", 
          "connectionname": "connectionname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_peoplesoft_connections(self):
        url="/resources/peoplesoftconnection/list"
        return self.uc.get(url)
    
    def get_sap_connection(self, query=None, **args):
        '''
        Arguments:
        - connectionid: connectionid 
        - connectionname: connectionname 
        '''
        url="/resources/sapconnection"
        field_mapping={
            "connectionid": "connectionid", 
            "connectionname": "connectionname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_sap_connection(self, payload=None, **args):
        url="/resources/sapconnection"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_sap_connection(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/sapconnection"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_sap_connection(self, query=None, **args):
        '''
        Arguments:
        - connectionid: connectionid 
        - connectionname: connectionname 
        '''
        url="/resources/sapconnection"
        field_mapping={
          "connectionid": "connectionid", 
          "connectionname": "connectionname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_sap_connections(self):
        url="/resources/sapconnection/list"
        return self.uc.get(url)
    
    def get_snmp_connection(self, query=None, **args):
        '''
        Arguments:
        - managerid: managerid 
        - managername: managername 
        '''
        url="/resources/snmpmanager"
        field_mapping={
            "managerid": "managerid", 
            "managername": "managername", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)

    def update_snmp_connection(self, payload=None, **args):
        url="/resources/snmpmanager"
        _payload = payload
        return self.uc.put(url, json_data=_payload, parse_response=False)

    def create_snmp_connection(self, payload=None, **args):
        '''
        Arguments:
        - retainSysIds: retainSysIds 
            False will ignore sysIds in the payload and create a new task  
        '''
        url="/resources/snmpmanager"
        field_mapping={
          "retainSysIds": "retainSysIds", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload, parse_response=False)

    def delete_snmp_connection(self, query=None, **args):
        '''
        Arguments:
        - managerid: managerid 
        - managername: managername 
        '''
        url="/resources/snmpmanager"
        field_mapping={
          "managerid": "managerid", 
          "managername": "managername", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.delete(url, query=parameters, parse_response=False)

    def list_snmp_connections(self):
        url="/resources/snmpmanager/list"
        return self.uc.get(url)