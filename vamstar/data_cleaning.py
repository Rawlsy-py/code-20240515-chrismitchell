import pandas as pd
from pandas import DataFrame

df = pd.read_csv("Interview Analysis Molecule.tsv", sep="\t")


def mean_population_data(df: DataFrame) -> DataFrame:
    """Populate missing values with the mean of the column

    Args:
        df (DataFrame): DataFrame to be cleaned

    Returns:
        DataFrame: Cleaned DataFrame
    """
    # grab a list of all the columns in the dataframe
    columns = df.columns

    # Itterate through each column to find values that are missing
    for column in columns:
        missing_values = df[column].isnull().sum()
        if missing_values > 0:
            print(f"{column} has {missing_values} missing values")

    # populate missing values with the mean of the column
    for column in columns:
        df[column].fillna(df[column].mean(), inplace=True)

    return df
