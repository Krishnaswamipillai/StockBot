import numpy as np
#weights for weighted averages
weight90 = 
weight30 =
weight10 =

#average each company in a list
#We need to import the 90,30,10 day lists every day. 
avg90 = np.array(lnrg90)
avg30 = np.array(lnrg30)
avg10 = np.array(lnrg10)

#transaction fees
tFee = []
weightTFee =

#relative percentage growth as compared to S&P i.e 95%/115% based off of 100% so 15% decrease is equivalent to 85%
relGrowth = []
weightRelGrowth =

def stockAvg():
	return numpy.multiply(avg90,weight90) + numpy.multiply(avg30,weight30) numpy.multiply(avg10,weight10)

def sigmoid(z):
	# Z = weightAvg*stockAvg - TFee*weightTfee/stockPrice
	return 1/(1+exp(-z))
