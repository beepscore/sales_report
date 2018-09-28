class CsvParser(object):
    '''
    Parses lines from a CSV file, each representing 1 row,
    into individual columns.
    '''

    def __init__(self, data):
        '''
        Construct the CsvParser object.
        '''
        # TODO: Write this method body.
        self.data = data
        
        # can get from file number of lines
        # number_of_weeks = 52
        
        # get number of products
        header_cols = line0.split(',').strip()
        self.product_cols = header_cols[1:]
        number_of_products = len(product_cols)
        
    def __iter__(self):
        '''
        Allows this object to act like an iterator
        in list comprehensions or iteration. e.g.:
          for csv_line_as_array in my_csv_parser:
              # Use the array representing that CSV record
        '''
        # TODO: Write this method body.
        
        for row in self.data.readlines():
            # return next row
            yield next(row)


    def next(self, row):
        '''
        Returns the next line from a CSV file, as an array, with one
        column per array element (where each element is string).
        '0,568.15,'
        ['0','568.15'...]
        '''
        if row is None:
            return None
        
        # TODO: skip header row
        
        # TODO: Write this method body.
        row_list = row.split(',').strip()
        week_number = row[0].strip()

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


