from bitfinex.client import Client

class Bitfinex(object):
    def __init__(self):
        self.client = Client()
        print ('Constructor Bitfinex')
    def GotIOT2USD(self):
        symbol = 'iotusd'
        iota = self.client.ticker(symbol)['ask']
        return iota
    def GotBTC2USD(self):
        symbol = 'btcusd'
        btc = self.client.ticker(symbol)['ask']
        return btc
    def GotIOT2BTC(self):
        symbol = 'iotbtc'
        btc = self.client.ticker(symbol)['ask']
        return btc
