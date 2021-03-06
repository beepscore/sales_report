#!/usr/bin/env python3

import pandas as pd
from decimal import Decimal
import numpy as np

"""
Use pandas to read csv, parse values, generate reports.
This is an alternative solution to csv_parser.py and sales_report.py
"""


def decimal_from_value(value):
    """
    Can use decimal for greater accuracy with currency.
    """
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
    # drop column 0 Week
    product_columns_df = df.iloc[:, 1:]

    # product_columns_df contains Decimal
    # print('product_columns_df.dtypes', '\n', product_columns_df.dtypes)
    # Product1 object
    # Product2 object
    # Product3 object

    # sum() is vectorized and fast but doesn't preserve type object (Decimal), changes to float64
    # week_sums = product_columns_df.sum(axis=1)
    # apply() may be slower than sum() but preserves type object (Decimal)
    week_sums = product_columns_df.apply(lambda x: x.sum(), axis=1)

    week_sums.name = 'total'

    week_sums_df = pd.concat([df['Week'], week_sums], axis=1)
    week_sums_df.name = 'total_sales_per_week'

    return week_sums_df


def total_sales_per_product(df):
    """
    :return: a series with total sales associated with each product over all rows e.g.

    Product1    1695.83
    Product2     628.75
    Product3    1498.52
    Name: total_sales_per_product, dtype: object
    """
    product_columns_df = df.iloc[:, 1:]

    # sum() is vectorized and fast but doesn't preserve type object (Decimal), changes to float64
    # product_column_sums = product_columns_df.sum()
    # apply() may be slower than sum() but preserves type object (Decimal)
    product_column_sums = product_columns_df.apply(lambda x: x.sum())

    product_column_sums.name = 'total_sales_per_product'

    return product_column_sums


def average_sales_per_product_per_week(df):
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
    product_column_averages_df.name = 'average_sales_per_product_per_week'

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

    # idxmax() doesn't work with type object Decimal, so convert Decimal to numpy float64
    week_sums_df['total'] = week_sums_df['total'].astype(np.float64)

    # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.idxmax.html
    index_total_max = week_sums_df['total'].idxmax()
    # print(index_total_max)
    # 1

    week_sums_max_row = week_sums_df.loc[index_total_max]

    return week_sums_max_row[0]


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
    print(total_sales_per_product(df))
    print()
    print('average_sales_per_product_per_week', '\n', average_sales_per_product_per_week(df))
    print()
    print('week_with_highest_sales', '\n', week_with_highest_sales(df))
