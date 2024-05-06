import pandas as pd

def function1():
    df = pd.read_csv('./Advertising.csv')
    print(df)
    print(f"columns = {df.columns}")
    print(f"shape = {df.shape}")
    print('-' * 80)

    print(df.head(5))
    print('-' * 80)
    print(df.tail(5))
    print('-' * 80)
    print(df.columns)
    print('-' * 80)
    print(df.tail(3))
    print('-' * 80)
    print(df.describe())
    print('-' * 80)
    df.info()
    print('-' * 80)
    print(df.isna())
    print('-' * 80)
    print(df.isna().sum())
    print('-' * 80)
    df.dropna(axis=0, inplace=True)
    print('-' * 80)
    df.drop('radio',axis=1, inplace=True)
    print(df.head(10))
    print('-' * 80)
    df['updated_sales'] = df['sales'] + df['sales'] * 0.10
    print(df)
    print('-' * 80)
    print(df.shape)
    print('-' * 80)


function1()

