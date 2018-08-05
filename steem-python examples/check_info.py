from steem import Steem
import sys
import math
from dateutil import parser
import datetime

account_name = sys.argv[1]
s = Steem()
account_info = s.get_account(account_name)

# for key, value in account_info.items():
# 	print('----------')
# 	print(key)
# 	print(value)

post_count = account_info['post_count']
steem_balance = account_info['balance']
voting_power = account_info['voting_power']
reputation = account_info['reputation']
last_post_date = account_info['last_root_post']

reputation = (math.log10(int(reputation))-9)*9+25
voting_power = int(voting_power)/100
last_post_date = parser.parse(last_post_date)
time_since_last_post = datetime.datetime.now() - last_post_date
days_since_last_post = time_since_last_post.days

display_message = '''
Username: \t{}
Reputation:\t{}
=============================
Total Posts:\t{}
Last Post: \t{} ({} days ago)
Voting Power:\t{} %
'''.format(account_name, reputation, post_count, last_post_date, days_since_last_post, voting_power)

print(display_message)
