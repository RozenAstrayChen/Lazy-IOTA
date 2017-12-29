
from calculate.calculate import Calculate


cal = Calculate()
print("Currently IOTA/USD --->" + str(cal.GotIOT2USD()))
print("Currently IOTA/BTC ---> " + str(cal.GotIOT2BTC()))
print("Currently BTC/TWD --->" + str(cal.GotSellPrice()))

try:
    select = input("choose you want \n1. Mi to TWD \n2.TWD to Mi\n")
    if select == 1:
        mi = input("your current Mi : ")
        total = cal.CountCurrentlyTWD(mi)
        print ("Count to TWD = "+str(total))
    elif select == 2:
        TWD = input("your want TWD : ")
        total = cal.WantGot(TWD)
        print ("Need total "+str(total) + " Mi")
except ValueError:
    print('Not this function')


