'''
Create CRUD functions for the portfolio data table. Example: get_portfolio_by_id
'''

import typing as t
from app.src.domain.Portfolio import Portfolio
from .dbutils import get_db_cnx
from .sql import get_portfolio_by_id_sql

def get_portfolio_by_id(id:int) -> t.optional[Portfolio]:
    try:
        db_cnx = get_db_cnx()
        cursor = db_cnx.cursor(dictionary= True)
        cursor.execute(get_portfolio_by_id_sql, (id,))
        result_set= cursor.fetchone()
        if result_set is None:
            return None
        return Portfolio(result_set['account_id'],result_set['ticker'], result_set['quantity'], result_set['id'])
    except Exception as e:
        print("an exception has occured while getting account with ID {id}:{str(e)}")
    finally:
        cursor.close()
        db_cnx.close()

def get_portfolio_by_account_id(account_id: int) -> t.List[Portfolio]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute(sql.get_portfolio_by_account_id_sql, (account_id, ))
        rs = cursor.fetchall()
        if len(rs) == 0:
            return []
        else:
            portfolio = []
            for row in rs:
                portfolio.append(portfolio(row['account_id'], row['ticker'], row['quantity'], row['id']))
        return portfolio
    except Exception as e:
        print(f'Unable to retrieve portfolio account id {account_id}: {int(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def create_portfolio(portfolio: Portfolio) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.create_portfolio, (portfolio.account_id, portfolio.ticker, portfolio.quantity))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to create a new portfolio: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def update_portfolio_account_id(id: int, account_id: int) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.update_portfolio_account_id, (account_id, id))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to update investor account_id: {int(e)}')
    finally: 
        cursor.close()
        db_cnx.close()

def update_portfolio_ticker(id: int, ticker: str) -> t.Optional[Portfolio]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.update_portfolio_ticker, (ticker, id))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to update portfolio ticker: {str(e)}')
    finally: 
        cursor.close()
        db_cnx.close()

def update_portfolio_quantity(id: int, quantity: int) -> t.Optional[Portfolio]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.update_portfolio_quantity, (quantity, id))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to update portfolio quantity: {int(e)}')
    finally: 
        cursor.close()
        db_cnx.close()

