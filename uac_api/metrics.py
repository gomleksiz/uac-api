class Metrics:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_metrics(self):
        url="/resources/metrics"
        return self.uc.get(url, parse_response=False, headers={"content-type": "text/plain"})