# report.py
#
# Exercise 2.4

import fileparse

def read_portfolio(filename):
    '''Read portfolio file'''
     
    with open(filename) as lines:
        print( fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float]))



def read_prices(filename):
    with open(filename) as lines:
        return fileparse.parse_csv(lines, types=[str,float], has_headers=False)
    

def make_report(portfolio, prices):
    '''DO CALCULATIONA AND MAKE THE REPORT''' 
    report = []
    for stock in portfolio:
        price_now= prices[stock['name']]
        change = price_now - stock['price']
        summary = (stock['name'], stock['shares'], price_now, change)
        report.append(summary)
    return report
 
 

def print_data(report):
    '''PRINT THE REPORT''' 
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d  $%10.2f %10.2f' % row)


def read_file(portfoliofile,pricefile):
    '''READ TWO FILES AND CALL OTHER FUNTION''' 
    portfolio = read_portfolio(portfoliofile)
    prices    = read_prices(pricefile)

   # report = make_report(portfolio, prices) 
    #print_data(report)

    print(portfolio)


def main(args):
    
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
   
    read_file(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)
