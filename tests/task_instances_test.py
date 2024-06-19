import unittest
from unittest.mock import patch

from uac_api.task_instances import TaskInstances


class TestTaskInstances(unittest.TestCase):

    def setUp(self):
        self.uc = unittest.mock.MagicMock()
        self.task_instances = TaskInstances(self.uc)

    def test_get_task_instance(self):
        self.task_instances.get_task_instance(task_instance_id="123")
        self.uc.post.assert_called_once_with("/taskinstance/list", json_data={"sysId": "123"})

    def test_retrieve_output(self):
        self.task_instances.retrieve_output(task_instance_id="123")
        self.uc.get.assert_called_once_with("/taskinstance/retrieveoutput", query=["taskinstanceid=123"])

    def test_rerun(self):
        self.task_instances.rerun_task_instance(task_instance_id="123")
        self.uc.post.assert_called_once_with("/taskinstance/rerun", json_data={"id": "123"})

    def test_list_task_instances(self):
        self.task_instances.list_task_instances()
        self.uc.post.assert_called_once_with("/taskinstance/list", json_data={})

    def test_list_task_instances_with_payload(self):
        payload = {"agentName": "test"}
        self.task_instances.list_task_instances(payload=payload)
        self.uc.post.assert_called_once_with("/taskinstance/list", json_data=payload)

    def test_list_task_instances_with_args(self):
        self.task_instances.list_task_instances(agent_name="test")
        self.uc.post.assert_called_once_with("/taskinstance/list", json_data={"agentName": "test"})
