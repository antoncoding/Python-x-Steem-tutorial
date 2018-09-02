from steem import Steem
from steem.amount import Amount
from steem.account import Account
import sys
import datetime

# Example Command: python get_steem_balance_sheet.py antonsteemit 2018-08-01 2018-08-31

account_name = sys.argv[1]
start_date = datetime.datetime.strptime(sys.argv[2], '%Y-%m-%d')
end_date = datetime.datetime.strptime(sys.argv[3], '%Y-%m-%d')

print('Searching Transfer Balance: @{} from {} to {}'.format(account_name, start_date, end_date))
target_account = Account(account_name)

s = Steem()

latest_operation = s.get_account_history(account_name, index_from=-1, limit=0)
total_operations = latest_operation[0][0]
num_iteration = int(total_operations/1000) + 1 # Num of times we have to request get_account_history

transfer_file = open('output/transfers_{}.csv'.format(account_name), 'w')
vestbalance_file = open('output/reward_delegation_balance_{}.csv'.format(account_name), 'w')
transfer_file.write('Timestamp,Transfer Type,Dealer,STEEM,SBD,TX ID\n')
vestbalance_file.write('Timestamp,Type,STEEM,SBD,VEST,TX ID\n')

for i in range(1, num_iteration+1): # i =0, 1,2,3,...num_iteration
    _index_from = i*1000
    history = target_account.get_account_history(index=_index_from,limit=1000, order=1)
    for operation in history:
        # Check Transaction Timestamp
        timestamp = datetime.datetime.strptime(operation['timestamp'],"%Y-%m-%dT%H:%M:%S")
        if timestamp < start_date:
            continue
        elif timestamp > end_date:
            break

        if operation['type'] =='transfer':
            if operation['from'] == account_name:
                dealer = operation['to']
                transfer_type = 'transfer to'
                amount = -1* Amount(operation['amount']).amount
            else:
                dealer = operation['from']
                transfer_type = 'transfer from'
                amount = Amount(operation['amount']).amount
            if Amount(operation['amount']).asset =='Steem':
                transfer_file.write('{},{},{},{},{},{}\n'.format(operation['timestamp'],transfer_type, dealer, amount,0,operation['trx_id']))
            else:
                transfer_file.write('{},{},{},{},{},{}\n'.format(operation['timestamp'],transfer_type, dealer,0, amount,operation['trx_id']))
            
        elif operation['type'] == 'claim_reward_balance':
            vestbalance_file.write('{},{},{},{},{},{}\n'.format(operation['timestamp'],operation['type'], Amount(operation['reward_steem']).amount, Amount(operation['reward_sbd']).amount,Amount(operation['reward_vests']).amount,operation['trx_id']))
        elif operation['type'] == 'delegate_vesting_shares':
            vestbalance_file.write('{},{},{},{},{},{}\n'.format(operation['timestamp'],operation['type'], 0, 0,Amount(operation['vesting_shares']).amount,operation['trx_id']))



        