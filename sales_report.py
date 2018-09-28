class SalesReport:
    '''
    This class holds the data returned by your generate_sales_report() method.
    '''
    # TODO: Write this class body.

def generate_sales_report(parser):
    '''
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
    represented in the second through N+1th columns of the CSV. The 1st
    column indicates the week number.
    Each quarter consists of 12 weeks. This method generates
    a sales report with the following aggregate data:
    * The total value associated with each week.
    * Identify the week with the highest sales.
    @param parser a CsvParser initialized with the input CSV data.
    @return a SalesReport containing the figures of merit described above.
    
    
            Product1  Product2  Product3 ...
    total     568.15    180.12    513.40
    
    '''
    report = SalesReport()

    # TODO: Write this method body.
    return report


if __name__ == '__main__':
    print("Test")
    # Your SalesReport must also contain:
    # * The total sales associated with each product over the quarter.
    # * The average weekly sales associated with each product.
    # * Products should be indexed by product name in the report.
    
    parser = CsvParser('foo')
    print(parser.data)
    
    
    
pass


