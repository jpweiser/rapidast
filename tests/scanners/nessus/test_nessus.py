from unittest.mock import Mock
from unittest.mock import patch

import requests

import configmodel
import rapidast
from scanners.nessus.nessus_none import Nessus


class TestNessus:
    @patch("requests.Session.request")
    def test_setup_nessus(self, mock_get):
        # All this mocking is for PyNessusPro.__init__() which attempts to connect to Nessus
        mock_get.return_value = Mock(spec=requests.Response)
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '{"token": "foo", "folders": []}'

        config_data = rapidast.load_config("config/config-template-nessus.yaml")
        config = configmodel.RapidastConfigModel(config_data)
        test_nessus = Nessus(config=config)
        assert test_nessus is not None
        assert test_nessus.nessus_client is not None
