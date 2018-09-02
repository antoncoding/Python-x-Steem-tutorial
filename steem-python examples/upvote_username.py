from steem import Steem
import sys

def upvote(account_name ,post, weight):
    try:
        s.commit.vote(post["identifier"], weight, account=account_name)
        print("Casted vote({}%) on: {}.".format(weight,post["identifier"]))
    except Exception as error:
        print("Error : {}".format(error))


target_username = sys.argv[1]
account_name = sys.argv[2]
account_postkey = sys.argv[3]
vote_weight = sys.argv[4]

s = Steem("https://api.steemit.com", keys=[account_postkey])

target_post = {}

history = s.get_account_history(target_username, index_from=-1, limit=1000)
for operation in reversed(history):
    op = operation[1]['op']
    if op[0] == 'comment':
        if op[1]['parent_author'] == '':
            _permlink = op[1]['permlink']

            # Check if the Post has already been upvoted by my account
            if account_name in [v["voter"] for v in s.get_active_votes(target_username, _permlink)]:
                print("Already voted on this. Skipping... {}".format(op[1]['title']))
                continue
            
            # Save target vote in a dictionary structure
            target_post["permlink"] = _permlink
            target_post["title"] = op[1]['title']
            target_post["identifier"] = '@{}/{}'.format(target_username, target_post["permlink"])
            print('Target Post: {}'.format(target_post["identifier"]))
            upvote(account_name, target_post, 5)
            break