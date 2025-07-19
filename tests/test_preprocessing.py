import pandas as pd
import numpy as np
from dsutilbox.preprocessing import fill_missing_num_cols, check_missing_perc


def test_fill_missing_num_cols():
    df = pd.DataFrame({'a': [1, None, 3]})
    filled = fill_missing_num_cols(df)
    assert not filled.isnull().any().any()


def test_check_missing_perc():
    # Create a sample DataFrame
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4],
        'B': [None, 'x', 'y', 'z'],
        'C': [10.0, 20.0, 30.0, 40.0],
        'D': [np.nan, np.nan, np.nan, np.nan],
    })

    # Run function with only_missing=True
    result = check_missing_perc(df, only_missing=True)

    # Expected columns with missing values: A, B, D
    assert set(result.index) == {'A', 'B', 'D'}

    # D should have highest missing % (100%)
    assert result.iloc[0].name == 'D'

    # Result should contain correct columns
    assert 'Missing Percentage' in result.columns
    assert 'Data Type' in result.columns

    # Check data types are correctly reported
    assert result.loc['A', 'Data Type'] == 'float64'
    assert result.loc['B', 'Data Type'].name in (
        'object', 'string')  # dtype may vary by pandas version

    # Check the percentage values
    assert result.loc['A', 'Missing Percentage'] == 25.0
    assert result.loc['D', 'Missing Percentage'] == 100.0

    # Test with only_missing=False
    result_all = check_missing_perc(df, only_missing=False)
    assert set(result_all.index) == {'A', 'B', 'C', 'D'}
