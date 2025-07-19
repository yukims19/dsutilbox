import pandas as pd


def fill_missing_num_cols(df, strategy="mean"):
    for col in df.select_dtypes(include="number").columns:
        if strategy == "mean":
            df[col] = df[col].fillna(df[col].mean())
        elif strategy == "median":
            df[col] = df[col].fillna(df[col].median())
        else:
            raise ValueError("Unsupported strategy")
    return df


def check_missing_perc(df, only_missing=True):
    missing_pct = df.isnull().mean() * 100
    column_types = df.dtypes

    missing_info = pd.DataFrame({
        'Missing Percentage': missing_pct,
        'Data Type': column_types
    })

    if only_missing:
        missing_info = missing_info[missing_info['Missing Percentage'] > 0]

    missing_info = missing_info.sort_values(
        by='Missing Percentage', ascending=False)

    return missing_info
