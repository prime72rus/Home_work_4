from unittest.mock import mock_open, patch

from src.utils import read_from_json, create_object_from_dict


mocked_valid_json_content = '[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]'
mocked_invalid_json_content = '{"key": "value"}'
mocked_corrupted_json_content = "invalid json content"


@patch("os.path.isfile", return_value=False)
def test_read_from_json_nonexistent_file(mock_isfile):
    result = read_from_json("non_existent_file.json")
    assert result == []
    mock_isfile.assert_called_once_with("non_existent_file.json")


@patch("os.path.isfile", return_value=True)
@patch("os.path.getsize", return_value=0)
def test_read_from_json_empty_file(mock_getsize, mock_isfile):
    result = read_from_json("empty_file.json")
    assert result == []
    mock_isfile.assert_called_once_with("empty_file.json")
    mock_getsize.assert_called_once_with("empty_file.json")


@patch("os.path.isfile", return_value=True)
@patch("os.path.getsize", return_value=len(mocked_valid_json_content))
@patch("builtins.open", new_callable=mock_open, read_data=mocked_valid_json_content)
def test_read_from_json_valid_list(mock_file, mock_getsize, mock_isfile):
    result = read_from_json("valid_list.json")
    expected_result = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    assert result == expected_result
    mock_isfile.assert_called_once_with("valid_list.json")
    mock_getsize.assert_called_once_with("valid_list.json")
    mock_file.assert_called_once_with("valid_list.json", encoding="utf-8")


@patch("os.path.isfile", return_value=True)
@patch("os.path.getsize", return_value=len(mocked_invalid_json_content))
@patch("builtins.open", new_callable=mock_open, read_data=mocked_invalid_json_content)
def test_read_from_json_invalid_content(mock_file, mock_getsize, mock_isfile):
    result = read_from_json("invalid_content.json")
    assert result == []
    mock_isfile.assert_called_once_with("invalid_content.json")
    mock_getsize.assert_called_once_with("invalid_content.json")
    mock_file.assert_called_once_with("invalid_content.json", encoding="utf-8")


@patch("os.path.isfile", return_value=True)
@patch("os.path.getsize", return_value=len(mocked_corrupted_json_content))
@patch("builtins.open", new_callable=mock_open, read_data=mocked_corrupted_json_content)
def test_read_from_json_malformed_json(mock_file, mock_getsize, mock_isfile):
    result = read_from_json("malformed_json.json")
    assert result == []
    mock_isfile.assert_called_once_with("malformed_json.json")
    mock_getsize.assert_called_once_with("malformed_json.json")
    mock_file.assert_called_once_with("malformed_json.json", encoding="utf-8")


def test_create_object_from_dict(data_from_json):
    result = create_object_from_dict(data_from_json)
    assert result[0].name == "Смартфоны"
    assert (
        result[0].description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert result[0].products == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"


def test_create_object_from_dict_empty_data():
    result = create_object_from_dict([])
    assert result == []
