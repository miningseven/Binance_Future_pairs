import ccxt,json # pip install ccxt

key = 'YOUR_API_KEY'
secret = 'YOUR_SEKRET-API-KEY'


with open ('settings.json') as config_file:
   config = json.load(config_file)
#key = config['api-key']
#secret = config['api-secret']

exchange_id = 'binance'

exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({'apiKey':key, 
 'secret':secret, 
 'timeout':30000, 
 'enableRateLimit':True, 
 'option':{'defaultMarket': 'future'}})# future or spot

account = binance.fapiPrivateGetAccount()
a = account['positions']
symbols = []
for line in a:
    symbols.append(line['symbol'])
    
print(symbols)
