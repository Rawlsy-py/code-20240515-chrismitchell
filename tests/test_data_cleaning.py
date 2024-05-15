import pandas as pd
from pandas import DataFrame
import pytest

from vamstar.data_cleaning import mean_population_data


def test_mean_population_data():
    # Create a sample DataFrame with missing values
    df = pd.DataFrame(
        {"A": [1, 2, None, 4, 5], "B": [None, 2, 3, 4, 5], "C": [1, 2, 3, None, 5]}
    )

    # Call the function to clean the DataFrame
    cleaned_df = mean_population_data(df)

    # Check if missing values are filled with mean values
    assert cleaned_df["A"].isnull().sum() == 0
    assert cleaned_df["B"].isnull().sum() == 0
    assert cleaned_df["C"].isnull().sum() == 0

    # Check if mean values are correct
    assert cleaned_df["A"].mean() == pytest.approx(3.0)
    assert cleaned_df["B"].mean() == pytest.approx(3.5)
    assert cleaned_df["C"].mean() == pytest.approx(2.75)
