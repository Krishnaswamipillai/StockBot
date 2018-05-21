import numpy as np
#weights for weighted averages
weight90 = 
weight30 =
weight10 =

#average each company in a list
#We need to import the 90,30,10 day lists every day. 
def setData(lnrg90,lnrg30,lnrg10,ofLnrg90,ofLnrg30,ofLnrg10):
	avg90 = np.array(lnrg90)
	avg30 = np.array(lnrg30)
	avg10= np.array(lnrg10)
	r290 = np.array(ofLnrg90)
	r230 = np.array(ofLnrg30)
	r210 = np.array(ofLnrg10)

#transaction fees
#tFee (InteractiveBrokers- FeePerShare)
tFeePerShare = 4.95
weightTFee = 

#relative percentage growth as compared to S&P i.e 95%/115% based off of 100% so 15% decrease is equivalent to 85%
relGrowth = []
weightRelGrowth =

def zCalc():
	return numpy.multiply((1/(weight90+weight30+weight10)),weightAvg,numpy.add(numpy.multiply(avg90,weight90),numpy.multiply(avg30,weight30),numpy.multiply(avg10,weight10)))

def sigmoid(z):
	# Z = weightAvg*stockAvg - TFeePerShare*weightTfee/stockPrice
	return 1/(1+exp(-z))
