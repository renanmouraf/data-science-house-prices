import os
import pandas as pd


def clean_data(df, output_file='cleaned_data.csv'):
    """Makes an initial clean in a dataframe.

    Args:
        df (pd.DataFrame): A dataframe to clean.

    Returns:
        pd.DataFrame: the cleaned dataframe.
    """

    #### Please refer to the notebook 1.0-Exploratory-Data-Analysis.ipynb to more details

    # Removes columns with missing values issues
    cols_to_be_removed = ['Id', 'PoolQC', 'MiscFeature', 'Alley', 'Fence', 'LotFrontage',
    'GarageYrBlt', 'MasVnrArea']
    df.drop(columns=cols_to_be_removed, inplace=True)

    # Transforms ordinal columns to numeric
    ordinal_cols = ['FireplaceQu', 'ExterQual', 'ExterCond', 'BsmtQual', 'BsmtCond', 
    'HeatingQC', 'KitchenQual', 'GarageQual', 'GarageCond']
    for col in ordinal_cols:
        df[col].fillna(0, inplace=True)
        df[col].replace({'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5}, inplace=True)

    # Fills NA where incorrectly pandas placed NaN
    for c in ['GarageType', 'GarageFinish', 'BsmtFinType2', 'BsmtExposure', 'BsmtFinType1']:
        df[c].fillna('NA', inplace=True)

    # Fills None where incorrectly pandas placed NaN
    df['MasVnrType'].fillna('None', inplace=True)

    # Imputes with most frequent value
    df['Electrical'].fillna('SBrkr', inplace=True)

    # Saves a copy
    #cleaned_data = os.path.join(output_file)
    df.to_csv(output_file)

    return df

if __name__ == "__main__":
    train_file = os.path.join('raw_data.csv')
    if os.path.exists(train_file):
        df = pd.read_csv(train_file)
        print(f'Original Data: {df.shape}')
        cleaned_df = clean_data(df)

        columns_with_miss = cleaned_df.isna().sum()
        columns_with_miss = columns_with_miss[columns_with_miss!=0]
        print(f'Columns with missing values: {len(columns_with_miss)}')
        print(columns_with_miss.sort_values(ascending=False))

        train = pd.read_csv('cleaned_data.csv')
        columns_with_miss = train.isna().sum()
        columns_with_miss = columns_with_miss[columns_with_miss!=0]
        print(f'Columns with missing values: {len(columns_with_miss)}')
        print(columns_with_miss.sort_values(ascending=False))

        print(f'After Cleaning: {cleaned_df.shape}')
    else:
        print(f'File not found {train_file}')
