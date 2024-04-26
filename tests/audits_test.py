import unittest
from unittest.mock import patch

from uac_api.audits import Audits


class TestAudits(unittest.TestCase):

    def setUp(self):
        self.uc = unittest.mock.MagicMock()
        self.audits = Audits(self.uc)

    def test_list_audits(self):
        self.audits.list_audits()
        self.uc.post.assert_called_once_with("/audit/list", json_data={})

    def test_list_audits_with_payload(self):
        payload = {"auditType": "1", "source": "test"}
        self.audits.list_audits(payload=payload)
        self.uc.post.assert_called_once_with("/audit/list", json_data=payload)

    def test_list_audits_with_args(self):
        self.audits.list_audits(type="1", source="test")
        self.uc.post.assert_called_once_with("/audit/list", json_data={"auditType": "1", "source": "test"})
