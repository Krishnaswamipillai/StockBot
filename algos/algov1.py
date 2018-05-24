import numpy as np
# Global Values 
numStocksOwnedCompanies = {}
for i in BigBadDataStructure.keys():
	numStocksOwnedCompanies[i] = 0
# pool = total ammount of money
pool = 100000
# money in investments
investments = np.array([numStocksOwnedCompanies[x] for x in numStocksOwnedCompanies.keys()])
moneyOnHand = pool

#weights for weighted averages

weight90 =
weight30 =
weight10 =
weightAvgConstant =
negSigmoidConstant =
posSigmoidConstant =

#average each company in a list
#We need to import the 90,30,10 day lists every day.
def setData(BigBadDataStructure):
	m90 = np.array([BigBadDataStructure[x]["linreg90"][0] for x in numStocksOwnedCompanies.keys()])
	m30 = np.array([BigBadDataStructure[x]["linreg30"][0] for x in numStocksOwnedCompanies.keys()])
	m10 = np.array([BigBadDataStructure[x]["linreg10"][0] for x in numStocksOwnedCompanies.keys()])
	r290 = np.array([BigBadDataStructure[x]["linreg90"][1] for x in numStocksOwnedCompanies.keys()])
	r230 = np.array([BigBadDataStructure[x]["linreg30"][1] for x in numStocksOwnedCompanies.keys()])
	r210 = np.array([BigBadDataStructure[x]["linreg10"][1] for x in numStocksOwnedCompanies.keys()])
	stockPrice = np.array([BigBadDataStructure[x]["price"] for x in numStocksOwnedCompanies.keys()])\
	counter = 0

#transaction fees
#tFee (InteractiveBrokers- FeePerShare)
tFeePerShare = 4.95
weightTFee =

#relative percentage growth as compared to S&P i.e 95%/115% based off of 100% so 15% decrease is equivalent to 85%
relGrowth = []
weightRelGrowth =

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
		for x in numStocksOwnedCompanies.keys():
		numStocksOwnedCompanies[x] = investments[counter]
		counter += 1
		pool = moneyOnHand + np.sum(np.multiply(stockPrice,investments))
		
	
	
	
	
	
	
	
