import json
from unittest.mock import mock_open
from unittest.mock import patch, Mock
from src.utils import data_for_transactions


def test_data_for_transactions_valid_json_list():
    mock_file_content = '''[
        {
            "id": 441945886,
            "state": "EXECUTED",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {"code": "EUR"}
            }
        }
    ]'''

    with patch('builtins.open', mock_open(read_data=mock_file_content)), \
         patch('json.load') as mock_json_load:

        mock_json_load.return_value = [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {"code": "EUR"}
                }
            }
        ]

        result = data_for_transactions("fake_path.json")

        assert result == mock_json_load.return_value


def test_data_for_transactions_file_not_found():
    with patch('builtins.open', side_effect=FileNotFoundError):
        result = data_for_transactions("nonexistent.json")
        assert result == []


def test_data_for_transactions_invalid_json():
    with patch('builtins.open', mock_open(read_data="invalid json")), \
         patch('json.load', side_effect=json.JSONDecodeError("Expecting value", "", 0)):
        result = data_for_transactions("bad.json")
        assert result == []


def test_data_for_transactions_not_a_list():
    with patch('builtins.open', mock_open(read_data='{"not": "a list"}')), \
         patch('json.load', return_value={"not": "a list"}):
        result = data_for_transactions("object.json")
        assert result == []
