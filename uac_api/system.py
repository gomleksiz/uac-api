# - retrieve_system_details()
from .utils import prepare_payload, prepare_query_params

class System:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc
    
    def get_status(self):
        url="/resources/status"
        return self.uc.get(url)