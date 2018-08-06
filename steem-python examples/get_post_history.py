from steem import Steem
import sys

account_name = sys.argv[1]
s = Steem()
latest_operation = s.get_account_history(account_name, index_from=-1, limit=0)
total_operations = latest_operation[0][0]
print('This user has {} operations on STEEM'.format(total_operations))

num_iteration = int(total_operations/1000) + 1 # Num of times we have to request get_account_history

permlink_list = []
title_list = []

for i in range(1, num_iteration+1): # i = 1,2,3,...num_iteration
	_index_from = i*1000
	history = s.get_account_history(account_name, index_from=_index_from, limit=1000)
	for operation in history:
		op = operation[1]['op'] # 取出大List
		if op[0] == 'comment':
			if op[1]['parent_author'] == '':
				
				_permlink = op[1]['permlink']
				_title = op[1]['title']

				if _permlink not in permlink_list:
					permlink_list.append(_permlink)
					title_list.append(_title)
					
					print('[Title] {}\n   [Permlink] {}'.format(_title, _permlink))

print('You have authored {} posts on Steemits!'.format(len(permlink_list)))