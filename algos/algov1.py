import numpy as np
import math as m
# Global Values

numStocksOwnedCompanies = {}
"""
for i in BigBadDataStructure.keys():
        if i not in numStocksOwnedCompanies.keys():
                numStocksOwnedCompanies[i] = 0
"""
# pool = total ammount of money
pool = None
# money in investments
investments = None
moneyOnHand = None

#weights for weighted averages

weight90 =1
weight30 =1
weight10 =1
weightAvgConstant =1
negSigmoidConstant =1
posSigmoidConstant =1
m90 = None
m30 = None
m10 = None
r290 = None
r230 = None
r210 = None
stockPrice = None
#average each company in a list
#We need to import the 90,30,10 day lists every day.
def setData(BigBadDataStructure,investments):
        global m90, m30, m10, r290, r230, r210, stockPrice
        for i in BigBadDataStructure.keys():
                if i not in numStocksOwnedCompanies.keys():
                        numStocksOwnedCompanies[i] = 0
        temp = sorted(numStocksOwnedCompanies.keys())
        for i in range(len(temp)):
                if temp[i] not in BigBadDataStructure.keys():
                        investments = np.delete(investments,i)
                        del numStocksOwnedCompanies[temp[i]]
                        del temp[i]
                        i -= 1

        m90 = np.array([BigBadDataStructure[x]["linreg90"][0] for x in sorted(numStocksOwnedCompanies.keys())])
        m30 = np.array([BigBadDataStructure[x]["linreg60"][0] for x in sorted(numStocksOwnedCompanies.keys())])
        m10 = np.array([BigBadDataStructure[x]["linreg30"][0] for x in sorted(numStocksOwnedCompanies.keys())])
        r290 = np.array([BigBadDataStructure[x]["linreg90"][1] for x in sorted(numStocksOwnedCompanies.keys())])
        r230 = np.array([BigBadDataStructure[x]["linreg60"][1] for x in sorted(numStocksOwnedCompanies.keys())])
        r210 = np.array([BigBadDataStructure[x]["linreg30"][1] for x in sorted(numStocksOwnedCompanies.keys())])
        stockPrice = np.array([BigBadDataStructure[x]["price"] for x in sorted(numStocksOwnedCompanies.keys())])

#transaction fees
#tFee (InteractiveBrokers- FeePerShare)
tFeePerShare = 4.95
weightTFee =1


def zCalc():
        global m90, m30, m10, r290, r230, r210
        avgR2 = np.multiply(np.multiply(r290,r230,r210),1/3)
        based90 = np.multiply(m90,weight90,1/(stockPrice-m90*90))
        based30 = np.multiply(m30,weight30,1/(stockPrice-m30*30))
        based10 = np.multiply(m10,weight10,1/(stockPrice-m10*10))
        return np.multiply(np.multiply(avgR2,(1/(weight90+weight30+weight10))),np.multiply(weightAvgConstant,np.add(based90,based30,based10)))

def sigmoid(z):
        # Z = weightAvg*stockAvg - TFeePerShare*weightTfee/stockPrice
        # The idea is that this will output the percentage of the pool of money that we will applyto various stocks.
        sigmoidValue = (1/(1+m.exp(-z))-0.5)
        if sigmoidValue >= 0:
                return (1/(1+m.exp(-(z/2.35))-0.5))*posSigmoidConstant 
        else:
                return (1/(1+m.exp(-(z/2.35))-0.5))*negSigmoidConstant
def vectorSigmoid():
        vecSigmoid = np.vectorize(sigmoid)
        #print(vecSigmoid(zCalc()))
        return vecSigmoid(zCalc())

def stockCalculator(numnumnum,day):
        global moneyOnHand, pool, stockPrice, investments
        arr = vectorSigmoid()
        tempDic = {}
        for x in arr:
                tempDic[np.nonzero(arr == x)[0][0]]=x
        sortedArrKeys = sorted(tempDic,key=tempDic.get,reverse=True)
        if(numnumnum%5 == 0):
                for i in sortedArrKeys:
                        if arr[i] >= 0:
                                if abs(moneyOnHand) - int(pool*arr[i]/stockPrice[i])*stockPrice[i] - 4.95 > 0:
                                        moneyOnHand = abs(moneyOnHand) - abs(int(pool*arr[i]/stockPrice[i])*stockPrice[i]) - 4.95
                                        investments[i] += int(pool*arr[i]/stockPrice[i])
                        else:
                                if investments[i] > abs(int(investments[i]*arr[i])):
                                        moneyOnHand = abs(moneyOnHand) + abs(int(investments[i]*arr[i])*stockPrice[i]) - 4.95
                                        investments[i] = investments[i] - abs(int(investments[i]*arr[i]))
                                else:
                                        moneyOnHand = abs(moneyOnHand) + investments[i] * stockPrice[i] -4.95
                                        investments[i] = 0
        counter = 0
        numStocksOwnedCompaniesVal = {}
        for x in sorted(numStocksOwnedCompanies.keys()):
                numStocksOwnedCompanies[x] = investments[counter]
                numStocksOwnedCompaniesVal[x] = (round(investments[counter]*stockPrice[counter],2))
                counter += 1
        pool = abs(moneyOnHand) + np.sum(np.multiply(investments,stockPrice))
        keyTemp = sorted(numStocksOwnedCompaniesVal,key=numStocksOwnedCompaniesVal.get,reverse=True)
        tDic5 = {}
        tDic2 = {}
        for i in range(5):
                tDic5[keyTemp[i]]=numStocksOwnedCompaniesVal[keyTemp[i]]
        for i in range(2):
                tDic2[keyTemp[i]]=numStocksOwnedCompaniesVal[keyTemp[i]]
        if(numnumnum%5 == 0):
                print("--------------------------------------------")
                print("--------------------------------------------")
                print("--------------------------------------------")
                print("--------------------------------------------")
                print("Day: ",day)
                print("Total: ",((abs(moneyOnHand)+np.sum(np.multiply(investments,stockPrice)))))
                print("Cash on Hand: ",abs(moneyOnHand))
                print("--------------------------------------------")
                print("--------------------------------------------")
                print(tDic2)
                print(tDic5)
                print("--------------------------------------------")
                print("--------------------------------------------")
                print("--------------------------------------------")
                print("--------------------------------------------")
        return moneyOnHand,numStocksOwnedCompanies,moneyOnHand+np.sum(np.multiply(investments,stockPrice))
def main(dataBase,w9,w3,w1,avgC,negSig,posSig,bal,stocksOwned,numnumnum,day):
        global weight90, weight30, weight10, weightAvgConstant, negSigmoidConstant, posSigmoidConstant, moneyOnHand, pool, investments
        setData(dataBase,investments)
        ##INIT##
        pool = bal
        moneyOnHand = pool
        investments = np.array([numStocksOwnedCompanies[x] for x in sorted(numStocksOwnedCompanies)])
        ##ENDINIT###

        ##CONSTANTS##
        if numnumnum < 20:
                weight90 = 60*(1/numnumnum)
        else:
                weight90 = w9
        weight30 =w3
        weight10 =w1
        weightAvgConstant =avgC
        negSigmoidConstant =negSig
        posSigmoidConstant =posSig
        ##ENDCONSTANTS##
        return stockCalculator(numnumnum,day)
