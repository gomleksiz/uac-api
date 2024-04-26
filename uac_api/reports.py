from .utils import prepare_query_params

class Reports:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def run_report(self, query=None, **args):
        '''
        Arguments:
        - reporttitle: reporttitle 
        - visibility: visibility 
        - groupname: groupname 
        '''
        url="/resources/report/run"
        field_mapping={
            "reporttitle": "reporttitle", 
            "visibility": "visibility", 
            "groupname": "groupname", 
        }
        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters)