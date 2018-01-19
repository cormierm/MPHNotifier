#!/usr/bin/env python3
import requests
import datetime
import pushover
import json
import time

MPH_API_KEY = ''
PUSHOVER_USER_KEY = ''
PUSHOVER_API_TOKEN = ''
coins = ['monero', 'bitcoin-gold', 'zencash', 'zcash', 'vertcoin', 'feathercoin', 'bitcoin']
coin = 'monero'
prev_balance = 0


def mph_request(coin, method):
    global prev_balance
    url = 'https://{}.miningpoolhub.com/index.php?page=api&action={}&api_key={}'.format(coin, method, MPH_API_KEY)
    result = requests.get(url).json()
    if ('getuserbalance' in result and 'data' in result['getuserbalance']
                    and 'confirmed' in result['getuserbalance']['data']):
        balance = result['getuserbalance']['data']['confirmed']
        if balance != prev_balance:
            po.send_message("Balance update: {}".format(balance))
            prev_balance = balance
        print('[{}]: Current balance: {}'.format(datetime.datetime.utcnow(), balance))


po = pushover.Client(PUSHOVER_USER_KEY, api_token=PUSHOVER_API_TOKEN)
while True:
    mph_request(coin, 'getuserbalance')
    time.sleep(60)

