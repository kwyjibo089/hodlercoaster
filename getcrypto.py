#!/usr/bin/env python
import time
import sys
import time
import cryptocompare as cc
import scrollphat
import secrets
import servo

def get_change(current, previous):
    if current == previous:
        return 1
    try:
        return ((current - previous) / previous)
    except ZeroDivisionError:
        return 0

print("""
Press Ctrl+C to exit!
""")

cc.cryptocompare._set_api_key_parameter(secrets.API_KEY_CRYPTOCOMPARE)

cc.cryptocompare.get_price('BTC', currency='USD')

prices = cc.cryptocompare.get_historical_price_minute('BTC', currency='USD', limit=60)

price0 = prices[0]
priceN = prices[60]

change = get_change(priceN['close'], price0['close'])

currentPrice = '${}'.format(round(priceN['close']))
print('current price: ' + currentPrice)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(priceN['time'])))

print('old price: ' + '${}'.format(price0['close']))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(price0['time'])))

print(change * 100)
percentage = '{:.1%}'.format(change)
print(percentage)

scrollphat.set_brightness(55)
scrollphat.write_string('BTC ' + currentPrice + ' | ' +percentage , 11)

servo.moveTo(0)

while True:
    try:
        scrollphat.scroll()
        time.sleep(0.15)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
