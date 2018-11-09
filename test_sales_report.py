#!/usr/bin/env python3

import unittest
import csv_parser
import sales_report
from decimal import Decimal


class TestSalesReport(unittest.TestCase):

    def setUp(self):
        filename = './data/sales.csv'
        with open(filename) as f:
            # sales_text contains entire csv file
            sales_text = f.read()

        parser = csv_parser.CsvParser(sales_text)

        self.sales_report = sales_report.generate_sales_report(parser)

    def test_total_sales_per_week(self):
        expected = {'0': Decimal('1261.67'),
                    '1': Decimal('1373.37'),
                    '11': Decimal('1182.06'),
                    '2': Decimal('6.00')}

        actual = self.sales_report.total_sales_per_week
        self.assertEqual(actual, expected)

        # total_sales_per_week maintains Decimal
        actual_week_11_total = actual['11']
        self.assertEqual(type(actual_week_11_total), Decimal)
        self.assertEqual(actual_week_11_total, Decimal('1182.06'))

    def test_total_sales_per_product(self):
        expected = {'Product1': Decimal('1695.83'),
                    'Product2': Decimal('628.75'),
                    'Product3': Decimal('1498.52')}
        actual = self.sales_report.total_sales_per_product
        self.assertEqual(actual, expected)

        # total_sales_per_product maintains Decimal
        self.assertEqual(type(actual['Product1']), Decimal)

    def test_average_sales_per_product(self):
        expected = {'Product1': Decimal('423.9575'),
                    'Product2': Decimal('157.1875'),
                    'Product3': Decimal('374.63')}

        actual = self.sales_report.average_sales_per_product
        self.assertEqual(actual, expected)

        self.assertAlmostEqual(actual['Product1'], Decimal('423.96'), delta=0.005)
        self.assertAlmostEqual(actual['Product2'], Decimal('157.19'), delta=0.005)
        self.assertAlmostEqual(actual['Product3'], Decimal('374.63'), delta=0.005)

        # average_sales_per_product maintains Decimal
        self.assertEqual(type(actual['Product1']), Decimal)

    def test_week_with_highest_sales(self):
        self.assertEqual(self.sales_report.week_with_highest_sales(), '1')


if __name__ == '__main__':
    unittest.main()
