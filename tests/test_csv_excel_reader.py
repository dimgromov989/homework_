from unittest.mock import patch

import pandas as pd

from src.csv_excel_reader import reader_for_csv
from src.csv_excel_reader import reader_for_excel


def test_reader_for_csv():
    path_of_csv = "dummy/path/to/file.csv"
    mock_dataframe = pd.DataFrame({"Column1": ["Value1"], "Column2": ["Value2"]})

    with patch("pandas.read_csv", return_value=mock_dataframe):
        result = reader_for_csv(path_of_csv)
        expected_result = mock_dataframe.to_json(orient="records")
        assert result == expected_result


def test_reader_for_excel():
    path_of_excel = "dummy/path/to/file.xlsx"
    mock_dataframe = pd.DataFrame({"Column1": ["Value1"], "Column2": ["Value2"]})

    with patch("pandas.read_excel", return_value=mock_dataframe):
        result = reader_for_excel(path_of_excel)
        expected_result = mock_dataframe.to_json(orient="records")
        assert result == expected_result
