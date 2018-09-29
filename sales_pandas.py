#!/usr/bin/env python3

import pandas as pd

"""
Use pandas to read csv, parse values, generate reports.
This is an alternative solution to csv_parser.py and sales_report.py
"""


def df_from_file(filename):
    """
    reads csv file
    :return: pandas dataframe
    """
    df = pd.read_csv(filename)
    print()
    print(df.head())
    """
       Week  Product1  Product2  Product3
    0     0    568.15    180.12    513.40
    1     1    581.34    312.01    480.02
    2     2      1.00      2.00      3.00
    3    11    545.34    134.62    502.10
    """
    return df


if __name__ == '__main__':
    in_filename = './data/sales.csv'
    df = df_from_file(in_filename)

    product_columns_df = df.iloc[:, 1:]

    # product_column_sums is a series
    product_column_sums = product_columns_df.sum()
    product_column_sums_df = pd.DataFrame(product_column_sums, columns=['total'])
    print()
    print(product_column_sums_df)
    """
                total
    Product1  1695.83
    Product2   628.75
    Product3  1498.52
    """

    # product_column_averages is a series
    product_column_averages = product_columns_df.mean()
    product_column_averages_df = pd.DataFrame(product_column_averages, columns=['average'])
    print()
    print(product_column_averages_df)
    """
               average
    Product1  423.9575
    Product2  157.1875
    Product3  374.6300
    """

    week_sums = product_columns_df.sum(axis=1)
    week_sums.name = 'total'
    week_sums_df = pd.concat([df['Week'], week_sums], axis=1)
    print()
    print(week_sums_df)
    """
       Week    total
    0     0  1261.67
    1     1  1373.37
    2     2     6.00
    3    11  1182.06
    """

    # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.idxmax.html
    index_total_max = week_sums_df['total'].idxmax()
    # print(index_total_max)
    # 1

    week_sums_max_row = week_sums_df.loc[index_total_max]
    print()
    print(week_sums_max_row)
    """
    Week        1.00
    total    1373.37
    Name: 1, dtype: float64
    """

