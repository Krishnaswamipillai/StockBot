import numpy as np
#weights for weighted averages
weight90 =
weight30 =
weight10 =
weightAvgConstant =

#average each company in a list
#We need to import the 90,30,10 day lists every day.
def setData(BigBadDataStructure):
	m90 = np.array([BigBadDataStructure[x]["linreg90"][0] for x in BigBadDataStructure.keys()])
	m30 = np.array([BigBadDataStructure[x]["linreg30"][0] for x in BigBadDataStructure.keys()])
	m10= np.array([BigBadDataStructure[x]["linreg10"][0] for x in BigBadDataStructure.keys()])
	r290 = np.array([BigBadDataStructure[x]["linreg90"][1] for x in BigBadDataStructure.keys()])
	r230 = np.array([BigBadDataStructure[x]["linreg30"][1] for x in BigBadDataStructure.keys()])
	r210 = np.array([BigBadDataStructure[x]["linreg10"][1] for x in BigBadDataStructure.keys()])
	stockPrice = np.array([BigBadDataStructure[x]["price"] for x in BigBadDataStructure.keys()])

#transaction fees
#tFee (InteractiveBrokers- FeePerShare)
tFeePerShare = 4.95
weightTFee =

#relative percentage growth as compared to S&P i.e 95%/115% based off of 100% so 15% decrease is equivalent to 85%
relGrowth = []
weightRelGrowth =

def zCalc():
	return numpy.multiply((1/(weight90+weight30+weight10)),weightAvgConstant,numpy.add(numpy.multiply(m90,weight90,1/(stockPrice-m90*90)),numpy.multiply(m30,weight30,1/(stockPrice-m30*30)),numpy.multiply(m10,weight10,1/(stockPrice-m10*10))))

def sigmoid(z):
	# Z = weightAvg*stockAvg - TFeePerShare*weightTfee/stockPrice
	return 1/(1+exp(-z))
