from steem import Steem
from steem.amount import Amount
from steem.account import Account
import sys
import datetime

# Example Command: python get_steem_balance_sheet.py antonsteemit 2018-08-01 2018-08-31 <MY_PRIVATE_MEMO_KEY>
account_name = sys.argv[1]
start_date = datetime.datetime.strptime(sys.argv[2], '%Y-%m-%d')
end_date = datetime.datetime.strptime(sys.argv[3], '%Y-%m-%d')
memoPrivkey = sys.argv[4]

print('Searching Transfer Balance: @{} from {} to {}'.format(account_name, start_date, end_date))
target_account = Account(account_name)

s = Steem(keys=[memoPrivkey])

latest_operation = s.get_account_history(account_name, index_from=-1, limit=0)
total_operations = latest_operation[0][0]
num_iteration = int(total_operations/1000) + 1 # Num of times we have to request get_account_history

transfer_file = open('output/transfers_{}_memo.csv'.format(account_name), 'w')
transfer_file.write('Timestamp,Transfer Type,Dealer,STEEM,SBD,TX ID,memo\n')

for i in range(1, num_iteration+1):
    _index_from = i*1000
    history = target_account.get_account_history(index=_index_from,limit=1000, order=1)
    for operation in history:
        if operation['type'] =='transfer':
            
            # Check if Transaction Timestamp is in the given period of time
            timestamp = datetime.datetime.strptime(operation['timestamp'],"%Y-%m-%dT%H:%M:%S")
            if timestamp < start_date:
                continue
            elif timestamp > end_date:
                break

            # Classify transfers into IN transfers and OUT transfers
            if operation['from'] == account_name:
                dealer = operation['to']
                transfer_type = 'transfer to'
                amount = -1* Amount(operation['amount']).amount
            else:
                dealer = operation['from']
                transfer_type = 'transfer from'
                amount = Amount(operation['amount']).amount
            
            # Decrypt Memo if the message is decrypted
            try:
                if operation['memo'][0] == '#':
                        memo = s.decode_memo(operation['memo']).replace(',',' ').replace('\n',' ')
                else:
                    memo = operation['memo'].replace(',',' ').replace('\n',' ')
            except:
                memo = ''
            
            # Write File
            if Amount(operation['amount']).asset =='STEEM':
                transfer_file.write('{},{},{},{},{},{},{}\n'.format(operation['timestamp'],transfer_type, dealer, amount,0,operation['trx_id'], memo))
            else:
                transfer_file.write('{},{},{},{},{},{},{}\n'.format(operation['timestamp'],transfer_type, dealer,0, amount,operation['trx_id'], memo))
            
        


        