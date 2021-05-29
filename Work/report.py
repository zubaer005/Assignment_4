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

def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        price_now= prices[stock['name']]
        change = price_now - stock['price']
        summary = (stock['name'], stock['shares'], price_now, change)
        report.append(summary)
    return report
 
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

report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    print('%10s %10d  $%10.2f %10.2f' % row)
