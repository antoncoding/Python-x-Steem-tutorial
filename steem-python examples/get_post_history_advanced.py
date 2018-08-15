from steem import Steem
import sys

s = Steem()

# author = 'antonsteemit'
# permlink = 'kura-sushi'

# content = s.get_content(author, permlink)
# for _key, _value in content.items():
# 	print('[{}]\n {}'.format(_key, _value))

def get_post_detail(author, permlink):
	content = s.get_content(author, permlink)
	title = content['title']
	created = content['created']
	count_votes = content['net_votes']
	count_replies = content['children']
	total_payout_value = content['total_payout_value']
	pending_payout_value = content['pending_payout_value']

	reblogs = s.get_reblogged_by(author, permlink)
	count_reblogs = len(reblogs) -1

	return {'title':title, 'created':created, 'count_votes':count_votes, 'count_replies':count_replies, 'total_payout_value':total_payout_value, 'pending_payout_value':pending_payout_value, 'count_reblogs':count_reblogs}


#### Code From get_post_history.py ####

account_name = sys.argv[1]

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
		op = operation[1]['op'] 
		if op[0] == 'comment':
			if op[1]['parent_author'] == '':
				
				_permlink = op[1]['permlink']
				_title = op[1]['title']

				if _permlink not in permlink_list:
					permlink_list.append(_permlink)
					title_list.append(_title)
					
					# print('[Title] {}\n   [Permlink] {}'.format(_title, _permlink))

print('@{} have authored {} posts on Steemit!'.format(account_name, len(permlink_list)))


## Write Output
file_name = '{}_post_history.csv'.format(account_name)
file = open(file_name, 'w', encoding='utf-8')
file.write('title,permlink,created,votes,replies,reblogs,payout\n')

for permlink in permlink_list:
	detail = get_post_detail(account_name, permlink)
	file.write('{},{},{},{},{},{},{}\n'.format(detail['title'].replace(',',' '), permlink, detail['created'], detail['count_votes'], detail['count_replies'], detail['count_reblogs'], detail['total_payout_value'] ))

