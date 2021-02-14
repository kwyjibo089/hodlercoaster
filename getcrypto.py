
#!/usr/bin/env python
import time
import sys
import math
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

def percentageToAngle(percentage):
    angle = (percentage*12/5)+90
    angle = 54 if angle < 54 else angle
    angle = 126 if angle > 126 else angle
    return angle

def update_price(ticker):
    cc.cryptocompare._set_api_key_parameter(secrets.API_KEY_CRYPTOCOMPARE)
    
    prices = cc.cryptocompare.get_historical_price_minute(ticker, currency='USD', limit=60)

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
    scrollphat.write_string(ticker + ' ' + currentPrice + ' | ' + percentage, 11)

    return change


print("""
Press Ctrl+C to exit!
""")

if len(sys.argv) != 2:
    print("""
Usage: {} "ticker"
""".format(sys.argv[0]))
    sys.exit(0)

currentAngle = 90
servo.moveTo(currentAngle)
time.sleep(1)

ticker = sys.argv[1]

currentPercentage = update_price(ticker) * 100
angle = percentageToAngle(currentPercentage)
print("angle: " + str(angle))
servo.moveTo(angle)

timestamp = int(time.time())

while True:         
    try:
        scrollphat.scroll()
        time.sleep(0.15)
        if int(time.time()-timestamp) > 10:
            scrollphat.clear()
            currentPercentage = update_price(ticker) * 100
            currentPercentage = math.ceil(currentPercentage) if (currentPercentage > 1) else math.floor(currentPercentage)
            currentAngle = percentageToAngle(currentPercentage)
            print("current angle: " + str(currentAngle) + " currentPercentage: " + str(currentPercentage))
            servo.moveTo(currentAngle)
            time.sleep(1)
            timestamp = int(time.time())
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
    
