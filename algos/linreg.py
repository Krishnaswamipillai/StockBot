from scipy import stats

def LinReg(evaldata):
    xAxis=[1]
    for x in range (len(arrayOfStockPrices)-1):
        xAxis.append((x+2))

    #start = timeit.default_timer()

    for x in range (1000):
        slope, intercept, r_value, p_value, std_err = stats.linregress(xAxis,arrayOfStockPrices)
        print((x+1), "slope:", slope, "  R-squared: ", r_value**2)

    """
    stop = timeit.default_timer()

    print("start", start, "stop:", stop)
    print("runtime: ", (stop-start))
    print ("runtime average:", ((stop-start)/1000))
    """
