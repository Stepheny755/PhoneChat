import time,calendar

class Util():
    def __init__(self):
        pass

    def GTimeToSec(self,a):
        t = time.strptime(a)
        return calendar.timegm(t)

    def SecToGTime(self,a):
        t = time.gmtime(a)
        return time.asctime(t)

    def getGMTTime(self): #GMT == UTC
        return int(calendar.timegm(time.gmtime()))

    def getEarlier(self,a,b):
        return a if a<b else b

    def getLater(self,a,b):
        return a if a>b else b

    def ifPos(self,a):
        if a > 0:
            return "+"+str(a)
        else:
            return str(a)

    def dToS(self,num):
        return 24*60*60*num

    def sToD(self,num):
        return num/(60*60*24)

    def countPreviousDays(self,days):
        curtime = self.getGMTTime()
        curtime -= self.dToS(days)
        return self.SecToGTime(curtime)

    def countWeekSec(self):
        curtime = self.getGMTTime()
        return curtime - self.dToS(7)

    def countMonthSec(self):
        curtime = self.getGMTTime()
        return curtime - self.dToS(30)

    def round3(self,input):
        return float(format(input,'.3f'))

    def round2(self,input):
        return float(format(input,'.2f'))
