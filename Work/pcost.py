# pcost.py
#
# Exercise 1.27
import csv
import report
def portfolio_cost(filename):
  
    portfolio = report.read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])
    
cost = portfolio_cost('Data/portfoliodate.csv')
print('Total cost:', cost)
 