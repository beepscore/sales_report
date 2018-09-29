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
        self.total_sales_per_week = {}

        self.total_sales_per_product = {}


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

    # TODO: Write this method body.

    sales_report = SalesReport()

    total_sales_per_product = [0] * parser.number_of_products

    # iterate through parser by date
    for csv_line_as_array in parser:

        week_number_string = csv_line_as_array[0]

        # currency, use Decimal not float
        sales_per_week_per_product = [Decimal(x) for x in csv_line_as_array[1:]]

        sales_report.total_sales_per_week[week_number_string] = sum(sales_per_week_per_product)

        # increment quarterly sums
        for product_index in range(parser.number_of_products):
            product_sales = sales_per_week_per_product[product_index]
            total_sales_per_product[product_index] += product_sales

    for product_index in range(parser.number_of_products):
        sales_report.total_sales_per_product[parser.product_names[product_index]] = total_sales_per_product[product_index]

    return sales_report


if __name__ == '__main__':

    print("Test")

    # sales_text contains entire csv file
    filename = './data/sales.csv'
    with open(filename) as f:
        sales_text = f.read()

    # print(sales_text)
    parser = CsvParser(sales_text)

    sales_report = generate_sales_report(parser)

    print(sales_report.total_sales_per_week)
    print(sales_report.total_sales_per_product)



