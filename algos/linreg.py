from scipy import stats

def LinReg(evaldata):
#    start = timeit.default_timer()
    arrayOfStockPrices = (evaldata[ticker]['prices'])

    xAxis=[1]
    for x in range (len(arrayOfStockPrices)-1):
        xAxis.append((x+2))

    '''for x in range (1000):
        slope, intercept, r_value, p_value, std_err = stats.linregress(xAxis,arrayOfStockPrices)
        print((x+1), "slope:", slope, "  R-squared: ", r_value**2)'''

    slope, intercept, r_value, p_value, std_err = stats.linregress(xAxis,arrayOfStockPrices)
#    stop = timeit.default_timer()

    return(slope, r_value**2)
