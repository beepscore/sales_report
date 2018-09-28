#!/usr/bin/env python3


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
        number_of_products = len(self.product_cols)
        
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



