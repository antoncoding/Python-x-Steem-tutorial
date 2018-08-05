from steem import Steem
import sys

account_name = sys.argv[1]
s = Steem()
balance = s.get_account(account_name)['sbd_balance']
print(balance)