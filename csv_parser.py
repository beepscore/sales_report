#!/usr/bin/env python3


class CsvParser(object):
    """
    Parses lines from a CSV file, each representing 1 row,
    into individual columns.
    """

    def __init__(self, data):
        """
        Construct the CsvParser object.
        """
        # TODO: Write this method body.
        self.data = data

        lines = self.data.split('\n')
        header_line = lines[0]
        header_cols = header_line.split(',')
        header_cols = [element.strip() for element in header_cols]
        self.product_names = header_cols[1:]
        self.number_of_products = len(self.product_names)

        self.week_lines = lines[1:]

        self.week_index = 0

    def __iter__(self):
        """
        Allows this object to act like an iterator
        in list comprehensions or iteration. e.g.:
          for csv_line_as_array in my_csv_parser:
              # Use the array representing that CSV record
        """
        # TODO: Write this method body.

        return self

    def __next__(self):
        """
        Returns the next line from a CSV file, as an array, with one
        column per array element (where each element is string).
        :row: str e.g. '0,568.15,180.12,513.40...'
        :return: list of str e.g. ['0','568.15'...]

        I needed to research how to implement __iter__ and __next__
        https://stackoverflow.com/questions/4019971/how-to-implement-iter-self-for-a-container-object-python#4019987
        https://docs.python.org/3/tutorial/classes.html#generators
        https://stackoverflow.com/questions/19151/build-a-basic-python-iterator#24377
        https://stackoverflow.com/questions/40255096/next-in-generators-and-iterators-and-what-is-a-method-wrapper
        """
        # TODO: Write this method body.

        try:
            week_line = self.week_lines[self.week_index]
            week_list = week_line.split(',')
            week_list = [element.strip() for element in week_list]
        except IndexError:
            raise StopIteration()

        self.week_index += 1
        return week_list



