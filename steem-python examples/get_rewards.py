from steem import Steem
s = Steem()

def get_payout_from_votes(votes):
    fund_per_share = reward_balance / float(recent_claims)
    total_reward = 0
    for vote in votes:
        rshares = vote["rshares"]
        payout = float(rshares) * fund_per_share * base_price
        total_reward += payout
    return total_reward

reward_fund = s.get_reward_fund()
reward_balance = float(reward_fund["reward_balance"].split(' ')[0])
recent_claims = float(reward_fund["recent_claims"])
base_price = float(s.get_current_median_history_price()["base"].split(' ')[0])

author = 'antonsteemit'
permlink = 'kura-sushi'

votes = s.get_active_votes(author, permlink)
total_payout = get_payout_from_votes(votes)
print(total_payout)