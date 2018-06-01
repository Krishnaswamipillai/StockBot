#!/usr/bin/env python3
import os
import sys; sys.path.append('../algos/')
import algov1 as al
from multiprocessing import Pool
import random
import copy
from concurrent.futures import ThreadPoolExecutor

def loadStocks():

    returned = []
    files = sorted(os.listdir('linregcalc'))
    for i in files:
        print(i)
        try:
            returned.append(eval(open('linregcalc/' + i, 'r').read())[1])
        except:
            pass

    return returned

def getResults(v1, v2, v3, v4, v5, v6,loadedStocks, startmoney=100000):
    money = startmoney
    stocksOwned = {}
    investments = 0
    for i in loadedStocks:
        money, stocksOwned, investments = al.main(i,v1,v2,v3,v4,v5,v6,money,stocksOwned)
<<<<<<< HEAD
# main(dataBase,w9,w3,w1,avgC,negSig,posSig,bal,stocksOwned):
=======

>>>>>>> parent of 504256c... Revert "modified things, added 1k files for precomputed linregs"
    return investments + money

def hillclimb(arg):
    failures = arg.failures
    score = arg.score
    args = arg.args
    stocks = arg.stock

    #move randomly, change all dimensions
    addr = random.randint(0, 6)
    nArgs = copy.deepcopy(arg)
    nArgs.args[addr] *= random.randint(85, 115) / 100
    currentScore = getResults(nArgs.args[0],nArgs.args[1],nArgs.args[2],nArgs.args[3],nArgs.args[4],nArgs.args[5], stocks, 100000)
    if currentScore > score:
        print('successPerturb')
        return hillclimb(nArgs)
    elif failures >= 1000:
        print('bestLocalFound -- relocating')
        return arg
    else:
        print('failedPerturb')
        arg.failures += 1
        return hillclimb(arg)


class data:
    failures = None
    score = None
    args = None
    stock = None
    def __init__(self, failures, score, args, stock):
        self.failures = failures
        self.score = score
        self.args = args
        self.stock = stock


def optimizeWeights(startingLocations):
    loadedstock = loadStocks()
    pool = Pool(4)
    args = []
    for i in range(startingLocations):
        args.append(data(0, 100000, random.sample(range(0, 26), 6), loadedstock[random.randint(0, 500):random.randint(500, 1000)]))
    results = []
    with ThreadPoolExecutor(max_workers=1) as executor:
        results = executor.map(hillclimb, args)
