# report.py
#
# Exercise 2.4
import csv
 
def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                'name'   : row[0],
                'shares' : int(row[1]),
                'price'   : float(row[2])
            } 
            portfolio.append(holding)
    return portfolio



def read_prices(filename):
     
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices
 
portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')

total =0.0 
for s in portfolio:
        total += s['shares']*s['price']

print('Total cost', total)


total_value = 0.0
for s in portfolio:
    total_value += s['shares']*prices[s['name']]

print('Current value', total_value)
print('Gain', total_value - total)
