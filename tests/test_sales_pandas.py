#!/usr/bin/env python3

import unittest
import pandas as pd
import sales_pandas
from decimal import Decimal
# import numpy as np


class TestSalesPandas(unittest.TestCase):

    def setUp(self):
        # sales_text contains entire csv file
        filename = '../data/sales.csv'
        self.df = sales_pandas.df_from_file(filename)

    def test_total_sales_per_week(self):
        # don't use Decimal here because total_sales_per_week doesn't maintain decimal
        # d = {'Week': [0, 1, 2, 11],
        #     'total': [Decimal('1261.67'), Decimal('1373.37'), Decimal('6.00'), Decimal('1182.06')]}
        d = {'Week': [0, 1, 2, 11],
             'total': [1261.67, 1373.37, 6.00, 1182.06]}
        expected = pd.DataFrame(data=d)
        # print('expected', '\n', expected)

        actual = sales_pandas.total_sales_per_week(self.df)
        # print('actual', '\n', actual)

        self.assertEqual(type(actual), pd.DataFrame)
        self.assertTrue(actual.equals(expected))

        # item() returns float not float64
        actual_week_11_total = actual.loc[actual['Week'] == 11, 'total'].item()
        self.assertEqual(type(actual_week_11_total), float)
        self.assertEqual(actual_week_11_total, 1182.06)

    def test_total_sales_per_product(self):
        expected = pd.Series({'Product1': 1695.83,
                              'Product2': 628.75,
                              'Product3': 1498.52})
        actual = sales_pandas.total_sales_per_product(self.df)
        self.assertEqual(type(actual), pd.Series)
        self.assertEqual(actual.name, 'total_sales_per_product')
        self.assertTrue(actual.equals(expected))

    def test_average_sales_per_product_per_week(self):
        # don't use Decimal here because average_sales_per_product_per_week doesn't maintain decimal
        # d = {'product': ['Product1', 'Product2', 'Product3'],
        #      'average': [Decimal('423.9575'), Decimal('157.1875'), Decimal('374.63')]}
        data = [423.9575, 157.1875, 374.63]
        index = ['Product1', 'Product2', 'Product3']
        expected = pd.DataFrame(data=data, index=index, columns=['average'])
        print('expected', '\n', expected)

        actual = sales_pandas.average_sales_per_product_per_week(self.df)
        print('actual', '\n', actual)

        # assertEqual doesn't work, ValueError: The truth value of a DataFrame is ambiguous.
        # self.assertEqual(actual, expected)
        # pandas.DataFrame.equals works
        self.assertTrue(actual.equals(expected))

        # don't use Decimal here because average_sales_per_product_per_week doesn't maintain decimal
        self.assertAlmostEqual(actual.loc['Product1', 'average'], 423.96, delta=0.005)
        self.assertAlmostEqual(actual.loc['Product2', 'average'], 157.19, delta=0.005)
        self.assertAlmostEqual(actual.loc['Product3', 'average'], 374.63, delta=0.005)

    def test_week_with_highest_sales(self):
        self.assertEqual(sales_pandas.week_with_highest_sales(self.df), 1.0)


if __name__ == '__main__':
    unittest.main()
