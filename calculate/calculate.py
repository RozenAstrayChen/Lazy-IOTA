from transaction.gotBitfinex import Bitfinex
from transaction.gotBitoEX import BitoEX

class Calculate(Bitfinex,BitoEX):
    def __init__(self):
        super(Calculate, self).__init__()
        self.Refresh()
    def CountCurrentlyTWD(self,MI):
        btcBitfinex = self.GotIOT2BTC()
        btcBitoEX = self.GotSellPrice()
        total = float(MI) * btcBitfinex * btcBitoEX
        return total

    def WantGot(self,TWD):
        btcBitfinex = self.GotIOT2BTC()
        btcBitoEX = self.GotSellPrice()
        return ((TWD / btcBitoEX) / btcBitfinex)

       
        

    