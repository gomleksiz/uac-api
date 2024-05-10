from .utils import prepare_payload, prepare_query_params

class ServerOperations:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def roll_log(self):
        url="/resources/serveroperation/rolllog"
        return self.uc.get(url)

    def temporary_property_change(self, payload=None, **args):
        '''
        Arguments:
        - name: name 
        - value: value 
        '''
        url="/resources/serveroperation/temporarypropertychange"
        field_mapping={
          "name": "name", 
          "value": "value", 
        }
        _payload = prepare_payload(payload, field_mapping, args)
        return self.uc.post(url, json_data=_payload)
    
    def bulk_export(self):
        url="/resources/serveroperation/bulkexport"
        return self.uc.post(url)
    
    def bulk_export_with_versions(self):
        url="/resources/serveroperation/bulkexportwithversions"
        return self.uc.post(url)
    
    def bulk_import(self, path):
        url=f"/resources/serveroperation/bulkimport?path={path}"
        return self.uc.post(url)
    
    def list_log(self):
        url=f"/resources/serveroperation/listlog"
        return self.uc.get(url)
    
    def download_log(self, name):
        url=f"/resources/serveroperation/downloadlog?logName={name}"
        return self.uc.get(url, headers={"Accept": "application/octet-stream"}, parse_response=False)
