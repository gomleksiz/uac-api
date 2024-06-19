from .utils import prepare_payload, prepare_query_params

class ClusterNodes:
    def __init__(self, uc):
        self.log = uc.log
        self.headers = uc.headers
        self.uc = uc

    def get_cluster_node(self):
        url="/resources/clusternode/info"
        return self.uc.get(url)

    def list_cluster_nodes(self):
        url="/resources/clusternode/list"
        return self.uc.get(url)