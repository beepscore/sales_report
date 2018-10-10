#!/usr/bin/env python3

import pandas as pd
from decimal import Decimal

"""
Use pandas to read csv, parse values, generate reports.
This is an alternative solution to csv_parser.py and sales_report.py
"""


# currency use decimal for greater accuracy
def decimal_from_value(value):
    return Decimal(value)


def df_from_file(filename):
    """
    reads csv file
    :return: pandas dataframe e.g.

        Week  Product1  Product2  Product3
    0     0    568.15    180.12    513.40
    1     1    581.34    312.01    480.02
    2     2      1.00      2.00      3.00
    3    11    545.34    134.62    502.10
    """

    df = pd.read_csv(filename, converters={'Product1': decimal_from_value,
                                           'Product2': decimal_from_value,
                                           'Product3': decimal_from_value})

    return df


def total_sales_per_week(df):
    """
    :return: a dataframe e.g.

       Week    total
    0     0  1261.67
    1     1  1373.37
    2     2     6.00
    3    11  1182.06
    """
    product_columns_df = df.iloc[:, 1:]

    week_sums = product_columns_df.sum(axis=1)
    week_sums.name = 'total'
    week_sums_df = pd.concat([df['Week'], week_sums], axis=1)

    return week_sums_df


def total_sales_per_product(df):
    """
    :return: a dataframe with total sales associated with each product over the quarter e.g.

    Product    Total Sales
    Product1       1695.83
    Product2        628.75
    Product3       1498.52
    """
    product_columns_df = df.iloc[:, 1:]

    # product_column_sums is a series
    product_column_sums = product_columns_df.sum()
    product_column_sums_df = pd.DataFrame(product_column_sums, columns=['total'])

    return product_column_sums_df


def average_weekly_sales(df):
    """
    :return: a dataframe with average weekly sales associated with each product e.g.

               average
    Product1  423.9575
    Product2  157.1875
    Product3  374.6300
    """
    product_columns_df = df.iloc[:, 1:]

    # product_column_averages is a series
    product_column_averages = product_columns_df.mean()
    product_column_averages_df = pd.DataFrame(product_column_averages, columns=['average'])

    return product_column_averages_df


def week_with_highest_sales(df):
    """
    assume sales may be negative (e.g. customers returned items), 0, or positive
    :return: a series first week with maximum value e.g.

    Week        1.00
    total    1373.37
    Name: 1, dtype: float64
    """
    week_sums_df = total_sales_per_week(df)

    # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.idxmax.html
    index_total_max = week_sums_df['total'].idxmax()
    # print(index_total_max)
    # 1

    week_sums_max_row = week_sums_df.loc[index_total_max]

    return week_sums_max_row


if __name__ == '__main__':

    in_filename = './data/sales.csv'
    df = df_from_file(in_filename)

    print()
    # each product type is object, not float64 because it uses Decimal
    print('df.dtypes', '\n', df.dtypes)
    # Week int64
    # Product1 object
    # Product2 object
    # Product3 object

    print()
    print('df.head()', '\n', df.head())

    print()
    print('total_sales_per_week', '\n', total_sales_per_week(df))
    print()
    print('total_sales_per_product', '\n', total_sales_per_product(df))
    print()
    print('average_weekly_sales', '\n', average_weekly_sales(df))
    print()
    print('week_with_highest_sales', '\n', week_with_highest_sales(df))
