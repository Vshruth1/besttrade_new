# Investor SQL statements
investor_by_id = 'select name, address, status, id from investor where id = %s'
get_investors_by_name_sql = 'select name, address, status, id from investor where name = %s'
create_investor = 'insert into investor (name, address, status) values (%s, %s, %s)'
update_investor_name = 'update investor set name = %s where id = %s'
update_investor_address = 'update investor set address = %s where id = %s'

# Account SQL statements
get_account_by_id_sql= 'select id, investor_id, balance from account where id=%s'
get_account_by_investor_id_sql = 'select investor_id, balance, id from investor where investor_id = %s'
create_account = 'insert into account (investor_id, balance values (%s, %s)'
update_account_investor_id = 'update account set investor_id = %s where id = %s'
update_account_balance = 'update account set balance = %s where id = %s'

# Portfolio SQL statements
get_portfolio_by_id_sql = 'select id, account_id, ticker, quantity from portfolio where id=%s'
get_portfolio_by_account_id_sql = 'select account_id, ticker, quantity, id from portfolio where account_id = %s'
create_portfolio = 'insert into portfolio (account_id, ticker, quantity) values (%s, %s, %s)'
update_portfolio_account_id = 'update portfolio set account_id = %s where id = %s'
update_portfolio_ticker = 'update portfolio set ticker = %s where id = %s'
update_portfolio_quantity = 'update portfolio set quantity = %s where id = %s'

