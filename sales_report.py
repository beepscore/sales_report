#!/usr/bin/env python3

from csv_parser import CsvParser


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
        self.weekly_sales = []


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

    salesReport = SalesReport()

    product_sums = [0] * parser.number_of_products
    NUMBER_OF_WEEKS_IN_QUARTER = 12
    weekly_sums = [0] * NUMBER_OF_WEEKS_IN_QUARTER
    print(product_sums)

    # iterate through parser
    for csv_line_as_array in parser:

        for product_index in range(parser.number_of_products):
            # TODO: currency, use Decimal not float
            product_sales = float(csv_line_as_array[product_index + 1])
            product_sums[product_index] += product_sales

    report_text = str(parser.header_line) + '\n' + str(product_sums)


if __name__ == '__main__':

    print("Test")

    # sales_text contains entire csv file
    filename = './data/sales.csv'
    with open(filename) as f:
        sales_text = f.read()

    # print(sales_text)
    parser = CsvParser(sales_text)

    generate_sales_report(parser)


