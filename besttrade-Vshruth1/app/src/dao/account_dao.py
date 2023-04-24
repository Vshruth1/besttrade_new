'''
Create CRUD functions for the account data table. Example: get_account_by_id
'''
'''
CRUD operations:
C: Create
R: Read
U: Update
D: Delete
'''

import typing as t
from mysql.connector import MySQLConnection
from app.src.domain.Account import Account
from .dbutils import get_db_cnx
from .sql import get_account_by_id_sql

def get_account_by_id(id:int) -> t.optional[Account]:
    try:
        db_cnx = get_db_cnx()
        cursor = db_cnx.cursor(dictionary= True)
        cursor.execute(get_account_by_id_sql, (id,))
        result_set= cursor.fetchone()
        if result_set is None:
            return None
        return Account(result_set['investor_id'],result_set['balance'], result_set['id'])
    except Exception as e:
        print("an exception has occured while getting account with ID {id}:{str(e)}")
    finally:
        cursor.close()
        db_cnx.close()
        

def get_account_by_investor_id(id: int) -> t.List[Account]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute(sql.get_account_by_investor_id_sql, (investor_id, ))
        rs = cursor.fetchall()
        if len(rs) == 0:
            return []
        else:
            account = []
            for row in rs:
                account.append(Account(row['investor_id'], row['balance'], row['id']))
        return account
    except Exception as e:
        print(f'Unable to retrieve account investor id {investor_id}: {int(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def create_account(account: Account) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.create_account, (account.investor_id, account.balance))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to create a new account: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def update_account_investor_id(id: int, investor_id: int) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.update_account_investor_id, (investor_id, id))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to update account investor id: {int(e)}')
    finally: 
        cursor.close()
        db_cnx.close()

def update_account_balance(id: int, balance: float) -> t.Optional[Account]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.update_acccount_balance, (balance, id))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to update account balance: {float(e)}')
    finally: 
        cursor.close()
        db_cnx.close()   

