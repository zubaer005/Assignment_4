# report.py
#
# Exercise 2.4
import csv
import fileparse
def read_portfolio(filename):
    '''Read portfolio file'''
    return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])



def read_prices(filename):
    return dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))

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

    report = make_report(portfolio, prices) 
    '''print_data(report)'''


read_file('Data/portfolio.csv', 'Data/prices.csv')