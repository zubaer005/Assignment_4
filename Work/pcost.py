# pcost.py
#
# Exercise 1.27
import csv
import report

def portfolio_cost(filename):
  
    portfolio = report.read_portfolio(filename) 
    return sum([s['shares']*s['price'] for s in portfolio])


def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    
    cost = portfolio_cost(args[1])
    print('Total cost:', cost)
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
   


 