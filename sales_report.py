#!/usr/bin/env python3

from csv_parser import CsvParser
from decimal import Decimal


class SalesReport:
    """
    This class holds the data returned by your generate_sales_report() method.

    # Your SalesReport must also contain:
    # * The total sales associated with each product over the quarter.
    # * The average weekly sales associated with each product.
    # * Products should be indexed by product name in the report.

    """
    # TODO: Write this class body.

    def __init__(self, ):

        # NUMBER_OF_WEEKS_IN_QUARTER = 12
        # weekly_sums = [0] * NUMBER_OF_WEEKS_IN_QUARTER
        # use dictionary to allow for possibility of missing weeks
        # key is week
        self.total_sales_per_week = {}

        # key is product
        self.total_sales_per_product = {}
        self.average_sales_per_product = {}

    def total_sales_per_week_report(self):
        """
        :return: a string e.g.
        Week Total Sales
           0     1261.67
           1     1373.37
           2        6.00
          11     1182.06
        """
        text = 'Week Total Sales\n'
        for key, value in self.total_sales_per_week.items():
            # https://docs.python.org/3/library/string.html#formatstrings
            text += str(f'{key: >4} {value: >11}\n')
        return text

    def total_sales_per_product_report(self):
        """
        :return: The total sales associated with each product over the quarter
        a string e.g.
                     Product1  Product2  Product3
        Total Sales   1695.83    628.75   1498.52
        """
        products = '             '
        for key in self.total_sales_per_product.keys():
            products += str(f'{key: >10}')
        header = products

        sum_line = 'Total Sales  '
        for value in self.total_sales_per_product.values():
            # https://docs.python.org/3/library/string.html#formatstrings
            sum_line += str(f'{value: >10}')

        return header + '\n' + sum_line + '\n'

    def total_sales_per_product_report_narrow_format(self):
        """
        :return: The total sales associated with each product over the quarter, in narrow format
        a string e.g.
        Product    Total Sales
        Product1       1695.83
        Product2        628.75
        Product3       1498.52
        """
        text = 'Product    Total Sales\n'
        for key, value in self.total_sales_per_product.items():
            # https://docs.python.org/3/library/string.html#formatstrings
            text += str(f'{key: >4} {value: >13}\n')

        return text

    def average_weekly_sales_report(self):
        """
        :return: The average weekly sales associated with each product.
        a string e.g.
                     Product1  Product2  Product3
        Total Sales   1695.83    628.75   1498.52
        """
        products = '             '
        for key in self.average_sales_per_product.keys():
            products += str(f'{key: >10}')
        header = products

        sum_line = 'Average Sales'
        for value in self.average_sales_per_product.values():
            # https://docs.python.org/3/library/string.html#formatstrings
            sum_line += str(f'{value: >10.2f}')

        return header + '\n' + sum_line + '\n'

    def week_with_highest_sales(self):
        """
        assume sales can't be negative
        :return:
        """
        max_value = 0
        week_with_max_value = None
        for key, value in self.total_sales_per_week.items():
            if value > max_value:
                week_with_max_value = key
                max_value = value
        return week_with_max_value

    def week_with_highest_sales_report(self):
        """
        :return: the week with the highest sales.
        """
        return str(f'Week with highest sales: {self.week_with_highest_sales()}\n')


def generate_sales_report(parser):
    """
    Tally up the sales results from the quarter.
    This method consumes a CSV file describing the quarterly sales report,
    and returns aggregate statistics about the input data.
    The sales report input follows a CSV format with columns like the
    following:
    Week    Product1  Product2  Product3 ...
       0      568.15    180.12    513.40
       1      581.34    312.01    480.02
       ...
       11      545.34    134.62    502.10

    For each week, we display the sales generated from each of N products
    represented in the second through N+1th columns of the CSV.
    The 1st column indicates the week number.
    Each quarter consists of 12 weeks.
    This method generates a sales report with the following aggregate data:
    * The total value associated with each week.
    * Identify the week with the highest sales.
    @param parser a CsvParser initialized with the input CSV data.
    @return a SalesReport containing the figures of merit described above.

            Product1  Product2  Product3 ...
    total     568.15    180.12    513.40
    
    """

    sales_report = SalesReport()

    total_sales_per_product = [0] * parser.number_of_products

    number_of_records = enumerate_parser(parser, sales_report, total_sales_per_product)

    for product_index in range(parser.number_of_products):
        sales_report.total_sales_per_product[parser.product_names[product_index]] = total_sales_per_product[product_index]
        sales_report.average_sales_per_product[parser.product_names[product_index]] = total_sales_per_product[product_index] / number_of_records

    return sales_report


def enumerate_parser(parser, sales_report, total_sales_per_product):
    """
    :param parser:
    :param sales_report:
    :param total_sales_per_product:
    :return: number of records processed
    """
    # iterate through parser by date
    number_of_records = 0

    for csv_line_as_array in parser:

        # pre-increment for use in average
        number_of_records += 1

        week_number_string = csv_line_as_array[0]

        # currency, use Decimal not float
        sales_per_week_per_product = [Decimal(x) for x in csv_line_as_array[1:]]

        sales_report.total_sales_per_week[week_number_string] = sum(sales_per_week_per_product)

        # increment quarterly sums
        for product_index in range(parser.number_of_products):
            product_sales = sales_per_week_per_product[product_index]
            total_sales_per_product[product_index] += product_sales

    return number_of_records


if __name__ == '__main__':

    # print("Test")

    # sales_text contains entire csv file
    filename = './data/sales.csv'
    with open(filename) as f:
        sales_text = f.read()

    # print(sales_text)
    parser = CsvParser(sales_text)

    sales_report = generate_sales_report(parser)

    print(sales_report.total_sales_per_week_report())
    print(sales_report.week_with_highest_sales_report())

    print(sales_report.total_sales_per_product_report())
    # print(sales_report.total_sales_per_product_report_narrow_format())
    print(sales_report.average_weekly_sales_report())
