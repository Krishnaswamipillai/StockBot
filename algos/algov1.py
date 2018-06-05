import numpy as np
import math as m
import traceback
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
def setData(BigBadDataStructure):
	global m90, m30, m10, r290, r230, r210, stockPrice
	for i in BigBadDataStructure.keys():
		if i not in numStocksOwnedCompanies.keys():
			numStocksOwnedCompanies[i] = 0

	m90 = np.array([BigBadDataStructure[x]["linreg90"][0] for x in sorted(numStocksOwnedCompanies.keys()) if x])
	m30 = np.array([BigBadDataStructure[x]["linreg60"][0] for x in sorted(numStocksOwnedCompanies.keys()) if x])
	m10 = np.array([BigBadDataStructure[x]["linreg30"][0] for x in sorted(numStocksOwnedCompanies.keys()) if x])
	r290 = np.array([BigBadDataStructure[x]["linreg90"][1] for x in sorted(numStocksOwnedCompanies.keys()) if x])
	r230 = np.array([BigBadDataStructure[x]["linreg60"][1] for x in sorted(numStocksOwnedCompanies.keys()) if x])
	r210 = np.array([BigBadDataStructure[x]["linreg30"][1] for x in sorted(numStocksOwnedCompanies.keys()) if x])
	stockPrice = np.array([BigBadDataStructure[x]["price"] for x in sorted(numStocksOwnedCompanies.keys()) if x])

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
		return sigmoidValue * posSigmoidConstant
	else:
		return sigmoidValue * negSigmoidConstant
def vectorSigmoid():
	vecSigmoid = np.vectorize(sigmoid)
	#print(vecSigmoid(zCalc()))
	return vecSigmoid(zCalc())

def stockCalculator():
	global moneyOnHand, pool, stockPrice, investments
	arr = vectorSigmoid()
	for i in range(len(arr)):
		try:
			if arr[i] > 0:
				if moneyOnHand - int(pool*arr[i]/stockPrice[i])*stockPrice[i] > 0:
					moneyOnHand -= int(pool*arr[i]/stockPrice[i])*stockPrice[i]
					investments[i] += int(pool*arr[i]/stockPrice[i])
					owned = []
			else:
				if investments[i] > abs(int(investments[i]*arr[i])):
					moneyOnHand -= int(investments[i]*arr[i])*stockPrice[i]
					investments[i] += int(investments[i]*arr[i])
				else:
					moneyOnHand += investments[i] * stockPrice[i]
					investments[i] = 0
			counter = 0
			for x in sorted(numStocksOwnedCompanies.keys()):
				numStocksOwnedCompanies[x] = investments[counter]
				counter += 1
				pool = moneyOnHand + np.sum(np.multiply(stockPrice,investments))
		except Exception:
			print(traceback.format_exc())

	print("--------------------------------------------")
	print(moneyOnHand, np.sum(np.multiply(investments,stockPrice)))
	print("___________________________________________")
	return moneyOnHand, numStocksOwnedCompanies, np.sum(np.multiply(investments,stockPrice))

def main(dataBase,w9,w3,w1,avgC,negSig,posSig,bal,stocksOwned):
	global weight90, weight30, weight10, weightAvgConstant, negSigmoidConstant, posSigmoidConstant, moneyOnHand, pool, investments
	setData(dataBase)
	##INIT##
	pool = bal

	moneyOnHand = pool
	investments = np.array([numStocksOwnedCompanies[x] for x in sorted(numStocksOwnedCompanies)])
	print(investments, bal, "Here")
	##ENDINIT###

	##CONSTANTS##
	weight90 =w9
	weight30 =w3
	weight10 =w1
	weightAvgConstant =avgC
	negSigmoidConstant =negSig
	posSigmoidConstant =posSig
	##ENDCONSTANTS##


	return stockCalculator()
