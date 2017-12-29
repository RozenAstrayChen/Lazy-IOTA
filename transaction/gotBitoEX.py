import urllib2
from bs4 import BeautifulSoup
import json

class BitoEX(object):
    def __init__(self):
        self.url = 'https://www.bitoex.com/sync/dashboard_fixed/1514546706284'
        self.parser = 'html.parser'
        response = urllib2.urlopen(self.url)  
        self.soup = BeautifulSoup(response, self.parser)
        
        print ('Constructor BitoEX')
    def Refresh(self):
        self.url = 'https://www.bitoex.com/sync/dashboard_fixed/1514546706284'
        self.parser = 'html.parser'
        response = urllib2.urlopen(self.url)  
        self.soup = BeautifulSoup(response, self.parser)
        print ('Fresh BitoEX')
    def GotBuyPrice(self):
        newDictionary=json.loads(str(self.soup))
        re = str(newDictionary[0])
        re = re[:3]+re[:4]
        return float(re)
    def GotSellPrice(self):
        newDictionary=json.loads(str(self.soup))
        re = str(newDictionary[1])
        re = re[:3]+re[4:]
        return float(re)







