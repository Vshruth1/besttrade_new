from app.src.dao.account_dao import get_account_by_id

def main():
    account = get_account_by_id(1)
    print(account)

if __name__=='__main__':
    main()

from app.src.dao.portfolio_dao import get_portfolio_by_id

def main():
    portfolio = get_portfolio_by_id(1)
    print(portfolio)

if __name__=='__main__':
    main()
    