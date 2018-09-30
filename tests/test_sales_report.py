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


if __name__ == '__main__':
    unittest.main()
