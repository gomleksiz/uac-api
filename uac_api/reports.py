from .utils import prepare_query_params

class Reports:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def run_report(self, query=None, report_format="csv", **args):
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

        _headers = self.headers
        if str(report_format) == "csv":
            _headers.update({"Accept": "text/csv"})
        elif str(report_format) == "tab":
            _headers.update({"Accept": "text/tab-separated-values"})
        elif str(report_format) == "pdf":
            _headers.update({"Accept": "application/pdf"})
        elif str(report_format) == "png":
            _headers.update({"Accept": "image/png"})        
        elif str(report_format) == "xml":
            _headers.update({"Accept": "application/xml"})
        elif str(report_format) == "json":
            _headers.update({"Accept": "application/json"})

        parameters = prepare_query_params(query, field_mapping, args)
        return self.uc.get(url, query=parameters, parse_response=False, headers=_headers)