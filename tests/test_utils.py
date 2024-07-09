from unittest.mock import mock_open, patch
from src.utils import read_transactions_from_json


def test_read_transactions_from_json():
    with patch("builtins.open", mock_open(read_data="[]")) as mock_file:
        assert read_transactions_from_json("test_file.json") == []
        mock_file.assert_called_once_with("test_file.json", "r", encoding="utf-8")
