import numpy as np
# Global Values 
numStocksOwnedCompanies = {}
for i in BigBadDataStructure.keys():
	if i not in numStocksOwnedCompanies.keys():
		numStocksOwnedCompanies[i] = 0
# pool = total ammount of money
pool = 100000
# money in investments
investments = np.array([numStocksOwnedCompanies[x] for x in sorted(numStocksOwnedCompanies)])
moneyOnHand = pool

#weights for weighted averages

weight90 =1
weight30 =1
weight10 =1
weightAvgConstant =1
negSigmoidConstant =1
posSigmoidConstant =1

#average each company in a list
#We need to import the 90,30,10 day lists every day.
def setData(BigBadDataStructure):
	for i in BigBadDataStructure.keys():
	if i not in numStocksOwnedCompanies.keys():
		numStocksOwnedCompanies[i] = 0
	m90 = np.array([BigBadDataStructure[x]["linreg90"][0] for x in sorted(numStocksOwnedCompanies)])
	m30 = np.array([BigBadDataStructure[x]["linreg30"][0] for x in sorted(numStocksOwnedCompanies)])
	m10 = np.array([BigBadDataStructure[x]["linreg10"][0] for x in sorted(numStocksOwnedCompanies)])
	r290 = np.array([BigBadDataStructure[x]["linreg90"][1] for x in sorted(numStocksOwnedCompanies)])
	r230 = np.array([BigBadDataStructure[x]["linreg30"][1] for x in sorted(numStocksOwnedCompanies)])
	r210 = np.array([BigBadDataStructure[x]["linreg10"][1] for x in sorted(numStocksOwnedCompanies)])
	stockPrice = np.array([BigBadDataStructure[x]["price"] for x in sorted(numStocksOwnedCompanies)])

#transaction fees
#tFee (InteractiveBrokers- FeePerShare)
tFeePerShare = 4.95
weightTFee =1


def zCalc():
	avgR2 = numpy.multiply(numpy.multiply(r290,r230,r210),1/3)
	based90 = numpy.multiply(m90,weight90,1/(stockPrice-m90*90))
	based30 = numpy.multiply(m30,weight30,1/(stockPrice-m30*30))
	based10 = numpy.multiply(m10,weight10,1/(stockPrice-m10*10))
	return numpy.multiply(avgR2,(1/(weight90+weight30+weight10)),weightAvgConstant,numpy.add(based90,based30,based10))
			     
def sigmoid(z):
	# Z = weightAvg*stockAvg - TFeePerShare*weightTfee/stockPrice
	# The idea is that this will output the percentage of the pool of money that we will applyto various stocks.
	sigmoidValue = 1/(1+exp(-z))
	if sigmoidVale >= 0
		return sigmoidValue * posSigmoidConstant
	else:
		return sigmoidValue * negSigmoidConstant
def vectorSimgoid():
	vecSigmoid = numpy.vectorize(sigmoid)
	return vecSigmoid(zCalc())
	
def stockCalculator():
	arr = vectorSigmoid()
	for i in len(arr):
		if arr[i] >= 0:
			if moneyOnHand - int(pool*arr[i]/stockPrice[i])*stockPrice[i] > 0:
				moneyOnHand -= int(pool*arr[i]/stockPrice[i])*stockPrice[i]
				investments[i] += int(pool*arr[i]/stockPrice[i])
		else:
			if investments[i] >= abs(int(investments[i]*arr[i])):
				moneyOnHand += abs(int(investments[i]*arr[i])stockPrice[i])
				investments[i] -= abs(int(investments[i]*arr[i]))
			else:
				moneyOnHand += investments[i]stockPrice[i]
				investments[i] = 0
		counter = 0
		for x in sorted(numStocksOwnedCompanies):
		numStocksOwnedCompanies[x] = investments[counter]
		counter += 1
		pool = moneyOnHand + np.sum(np.multiply(stockPrice,investments))
		
def main(dataBase,w9,w3,w1,avgC,negSig,posSig):
	weight90 =w9
	weight30 =w3
	weight10 =w1
	weightAvgConstant =avgC
	negSigmoidConstant =negSig
	posSigmoidConstant =posSig
	setData(dataBase)
	stockCalculator()

	
	

	
	
		
	
	
	
	
	
	
	
