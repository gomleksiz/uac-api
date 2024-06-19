import unittest
from unittest.mock import patch

from uac_api.agents import Agents


class TestAgents(unittest.TestCase):
    def setUp(self):
        self.uc = unittest.mock.MagicMock()
        self.agents = Agents(self.uc)

    def test_read_agent(self):
        self.agents.read_agent(agent_id="123")
        self.uc.get.assert_called_once_with("/agent", query=["agentid=123"])
    
    def test_read_agent_with_query(self):
        self.agents.read_agent(query=["agentid=123"])
        self.uc.get.assert_called_once_with("/agent", query=["agentid=123"])

    def test_read_agent_with_name(self):
        self.agents.read_agent(agent_name="test")
        self.uc.get.assert_called_once_with("/agent", query=["agentname=test"])

    def test_list_agents(self):
        self.agents.list_agents()
        self.uc.get.assert_called_once_with("/agent/list")

    def test_list_agents_with_type(self):
        self.agents.list_agents_advanced(type="1")
        self.uc.get.assert_called_once_with("/agent/listadv", query=["type=1"])

    def test_list_agents_with_name(self):
        self.agents.list_agents_advanced(agent_name="test")
        self.uc.get.assert_called_once_with("/agent/listadv", query=["agentname=test"])

    def test_list_agents_advanced(self):
        self.agents.list_agents_advanced(type="1", agent_name="test")
        self.uc.get.assert_called_once_with("/agent/listadv", query=["type=1", "agentname=test"])
    
    def test_list_agents_advanced_query(self):
        self.agents.list_agents_advanced(query=["type=1", "agentname=test"])
        self.uc.get.assert_called_once_with("/agent/listadv", query=["type=1", "agentname=test"])