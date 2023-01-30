import ccxt
import config

kucoin = ccxt.kucoin()
exchange_id = 'kucoin'
exchange_class = getattr(ccxt, exchange_id)
kucoin = exchange_class({
    'rateLimit': 899,
    'enableRateLimit': True,
    'apiKey': config.KUCOIN_API_KEY,
    'secret': config.KUCOIN_SECRET_KEY,
    'password': config.KUCOIN_PASSWORD,
})

symbol = 'BTC/USDT'
base = 'BTC'
quote = 'USDT'
amount = 0.000039

order_book = kucoin.fetch_order_book(symbol)
ask = order_book['asks'][0][0]
bid = order_book['bids'][0][0]
spread = ask - bid
new_bid = bid + (bid * spread)
new_ask = ask - (ask * spread)

buy_order = kucoin.create_order(symbol, 'limit', 'buy', new_ask)
sell_order = kucoin.create_order(symbol, 'limit', 'sell', new_bid)
