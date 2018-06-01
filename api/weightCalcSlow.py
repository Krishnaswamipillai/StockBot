date1 = '2000 1 1'
date2 = '2017 12 28'
import simulation as s
import random


def weightStepper():
  w90,w30,w10,AvgW,nSig,pSig = 5,10,8,1,2,8
  w90,w30,w10,AvgW,nSig,pSig = weightStep(1,w90,w30,w10,AvgW,nSig,pSig)
  #weightStep(.1)
  print(w90,w30,w10,AvgW,nSig,pSig)

def weightStep(a,w90,w30,w10,AvgW,nSig,pSig):
  #This is extremly slow, as it runs the simulation 1,200 times
  flagW90, flagW30, flagW10, flagAvgW, flagNSig, flagPSig = [False]*6 
  moneyW90P, moneyW30P, moneyW10P, moneyAvgW, moneyNSig, moneyPSig = [0]*6

  for i in range(0,10):
    for sets in range(0,10):
      print("step")
      start,end = randdate(date1,date2)
      if flagW90 == False:
        moneyW90P += s.startSimulation(start, end,w90+a,w30,w10,AvgW,nSig,pSig)
        moneyW90N += s.startSimulation(start, end,w90-a,w30,w10,AvgW,nSig,pSig)
      if flagW30 == False:
        moneyW30P += s.startSimulation(start, end,w90,w30+a,w10,AvgW,nSig,pSig)
        moneyW30N += s.startSimulation(start, end,w90,w30-a,w10,AvgW,nSig,pSig)
      if flagW10 == False:
        moneyW10P += s.startSimulation(start, end,w90,w30,w10+a,AvgW,nSig,pSig)
        moneyW10N += s.startSimulation(start, end,w90,w30,w10-a,AvgW,nSig,pSig)
      if flagAvgW == False:
        moneyAvgWP += s.startSimulation(start, end,w90,w30,w10,AvgW+a,nSig,pSig)
        moneyAvgWN += s.startSimulation(start, end,w90,w30,w10,AvgW-a,nSig,pSig)
      if flagNSig == False:
        moneyNSigP += s.startSimulation(start, end,w90,w30,w10,AvgW,nSig+a,pSig)
        moneyNSigN += s.startSimulation(start, end,w90,w30,w10,AvgW,nSig-a,pSig)
      if flagPSig == False:
        moneyPSigP += s.startSimulation(start, end,w90,w30,w10,AvgW,nSig,pSig+a)
        moneyPsigN += s.startSimulation(start, end,w90,w30,w10,AvgW,nSig,pSig-a)
  
    if moneyW90P > moneyW90N and moneyW90P/10 >= money:
      w90 = w90+a
    if moneyW90P < moneyW90N and moneyW90N/10 >= money:
      w90 = w90-a
    if  moneyW90N/10 < money:
      flagW90 = true
      
    if moneyW30P > moneyW30N and moneyW30P/10 >= money:
      w30 = w30+a
    if moneyW30P < moneyW30N and moneyW30N/10 >= money:
      w30 = w30-a 
    if  moneyW90N/10 < money:
      flagW30 = true
      
    if moneyW10P > moneyW10N and moneyW10P/10 >= money:
      w10 = w10+a
    if moneyW10P < moneyW10N and moneyW10N/10 >= money:
      w10 = w10-a  
    if  moneyW90N/10 < money:
      flagW10 = true
      
    if moneyAvgWP > moneyAvgWN and moneyAvgWP/10 >= money:
      avgW = avgW+a
    if moneyAvgWP < moneyAvgWN and moneyAvgWN/10 >= money:
      avgW = avgW-a  
    if  moneyAvgWN/10 < money:
      flagAvgW= true
      
    if moneyNSigP > moneyNSigN and moneyNSigP/10 >= money:
      nSig = nSig+a
    if moneyNSigP < moneyNSigN and moneyNSigN/10 >= money:
      nSig = nSig-a 
    if  moneyNSigN/10 < money:
      flagNSigN = true
      
    if moneyPSigP > moneyPSigN and moneyPSigP/10 >= money:
      pSig = pSig+a
    if moneyPSigP < moneyPSigN and moneyPSigN/10 >= money:
      pSig = pSig-a 
    if  moneyPSigN/10 < money:
      flagPSigN = true  
  return w90,w30,w10,AvgW,nSig,pSig   
    
      
      
      
def randdate(date1,date2):
  year1 = int(date1[0:4])
  year2 = int(date2[0:4])
  startTime = random.randint(year1,year2)
  endTime = random.randint(year1,year2)
  print(startTime)
  print(endTime)
  
  if startTime == endTime:
    randdate(date1,date2)
  if startTime < endTime:
    return str(startTime)+" 1 1", str(endTime)+" 1 1"
  else:
    return str(endTime)+" 1 1", str(startTime)+" 1 1"
weightStepper()
