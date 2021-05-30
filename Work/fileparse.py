# fileparse.py
#
# Exercise 3.3

import csv
def parse_csv(filename, select=None, types=None, has_headers=True,  delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        
        headers = next(rows) if has_headers else []

       
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices ]
            if types:
                row = [func(val) for func, val in zip(types, row) ]

            # Make a dictionary
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            
            records.append(record)

    return records