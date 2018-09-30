#!/usr/bin/env python3

import unittest
import csv_parser
import sales_report
from decimal import Decimal


class TestSalesReport(unittest.TestCase):

    def setUp(self):
        # sales_text contains entire csv file
        filename = '../data/sales.csv'
        with open(filename) as f:
            sales_text = f.read()

        parser = csv_parser.CsvParser(sales_text)

        self.sales_report = sales_report.generate_sales_report(parser)

    def test_total_sales_per_week(self):
        expected = {'0': Decimal('1261.67'),
                    '1': Decimal('1373.37'),
                    '11': Decimal('1182.06'),
                    '2': Decimal('6.00')}
        self.assertEqual(self.sales_report.total_sales_per_week, expected)

    def test_total_sales_per_product(self):
        expected = {'Product1': Decimal('1695.83'),
                    'Product2': Decimal('628.75'),
                    'Product3': Decimal('1498.52')}
        self.assertEqual(self.sales_report.total_sales_per_product, expected)

    def test_average_sales_per_product(self):
        expected = {'Product1': Decimal('423.9575'),
                    'Product2': Decimal('157.1875'),
                    'Product3': Decimal('374.63')}
        self.assertEqual(self.sales_report.average_sales_per_product, expected)

        self.assertAlmostEqual(self.sales_report.average_sales_per_product['Product1'],
                               Decimal('423.96'),
                               delta=0.005)
        self.assertAlmostEqual(self.sales_report.average_sales_per_product['Product2'],
                               Decimal('157.19'),
                               delta=0.005)
        self.assertAlmostEqual(self.sales_report.average_sales_per_product['Product3'],
                               Decimal('374.63'),
                               delta=0.005)

    def test_week_with_highest_sales(self):
        self.assertEqual(self.sales_report.week_with_highest_sales(), '1')


if __name__ == '__main__':
    unittest.main()
