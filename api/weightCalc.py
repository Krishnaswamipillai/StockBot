day1 = '1 1 2000'
day2 = '1 1 2018'
import simulation as s
w90,w30,w10,AvgW,nSig,pSig = 5,10,8,.1,2.5,0.5 

def weightStep(a,w90,w30,w10,AvgW,nSig,pSig):
  #Dont worry about this function, it should be fine for w90 right now
  if a == none:
    a = 1
  
  for sets in range(0,10):
    s,e = randDay(date1,day2)
    
    moneyW90P += startSimulation(s, e, initalprice = 100000,w90+a,w30,w10,AvgW,nSig,pSig)
    moneyW90N += startSimulation(s, e, initalprice = 100000,w90-a,w30,w10,AvgW,nSig,pSig)
    
    moneyW30P += startSimulation(s, e, initalprice = 100000,w90,w30+a,w10,AvgW,nSig,pSig)
    moneyW30N += startSimulation(s, e, initalprice = 100000,w90,w30-a,w10,AvgW,nSig,pSig)
    
    moneyW10P += startSimulation(s, e, initalprice = 100000,w90,w30,w10+a,AvgW,nSig,pSig)
    moneyW10N += startSimulation(s, e, initalprice = 100000,w90,w30,w10-a,AvgW,nSig,pSig)
    
    moneyAvgWP += startSimulation(s, e, initalprice = 100000,w90,w30,w10,AvgW+a,nSig,pSig)
    moneyAvgWN += startSimulation(s, e, initalprice = 100000,w90,w30,w10,AvgW-a,nSig,pSig)
    
    moneyNSigP += startSimulation(s, e, initalprice = 100000,w90,w30,w10,AvgW,nSig+a,pSig)
    moneyNSigN += startSimulation(s, e, initalprice = 100000,w90,w30,w10,AvgW,nSig-a,pSig)
    
    moneyPSigP += startSimulation(s, e, initalprice = 100000,w90,w30,w10,AvgW,nSig,pSig+a)
    moneyPsigN += startSimulation(s, e, initalprice = 100000,w90,w30,w10,AvgW,nSig,pSig-a)
  
  if moneyW90P > moneyW90N and moneyW90P/10 > money:
    w90 = w90+a
  if moneyW90P < moneyW90N and moneyW90N/10 > money:
    w90 = w90-a
  if moneyW30P > moneyW30N and moneyW30P/10 > money:
    w30 = w30+a
  if moneyW30P < moneyW30N and moneyW30N/10 > money:
    w30 = w30-a    
  if moneyW10P > moneyW10N and moneyW10P/10 > money:
    w10 = w10+a
  if moneyW10P < moneyW10N and moneyW10N/10 > money:
    w10 = w10-a  
    
  if moneyAvgWP > moneyAvgWN and moneyAvgWP/10 > money:
    avgW = avgW+a
  if moneyAvgWP < moneyAvgWN and moneyAvgWN/10 > money:
    avgW = avgW-a  
  if moneyNSigP > moneyNSigN and moneyNSigP/10 > money:
    nSig = nSig+a
  if moneyNSigP < moneyNSigN and moneyNSigN/10 > money:
    nSig = nSig-a 
  if moneyPSigP > moneyPSigN and moneyPSigP/10 > money:
    pSig = pSig+a
  if moneyPSigP < moneyPSigN and moneyPSigN/10 > money:
    pSig = pSig-a 
  
    
      
      
      
def randDay(day1,day2):
  year1 = day1[-4:]
  year2 = day2[-4:]
  startTime = math.random.randint(year1,year2)
  endTime = math.random.randint(year1,year2)
  if startTime = endTime:
    randDay(day1,day2)
  if startTime < endTime:
    reutrn startTime,endTime
  else:
    return endTime,startTime


    

