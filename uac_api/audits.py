from .utils import prepare_payload

class Audits:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def list_audit(self, payload=None, **args):
        '''
        Arguments:
        - auditType: auditType 
        - source: source 
        - status: status 
        - createdBy: createdBy 
        - tableName: tableName 
        - tableRecordName: tableRecordName 
        - updatedTimeType: updatedTimeType 
        - updatedTime: updatedTime 
        - tableKey: tableKey 
        - includeChildAudits: includeChildAudits 
        '''
        url="/resources/audit/list"
        field_mapping={
          "auditType": "auditType", 
          "source": "source", 
          "status": "status", 
          "createdBy": "createdBy", 
          "tableName": "tableName", 
          "tableRecordName": "tableRecordName", 
          "updatedTimeType": "updatedTimeType", 
          "updatedTime": "updatedTime", 
          "tableKey": "tableKey", 
          "includeChildAudits": "includeChildAudits", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)