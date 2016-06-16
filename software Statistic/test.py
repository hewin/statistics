# from scipy.stats import norm as N
import urllib
import json
import scipy.stats
class Solution():
    def describe(self, a):
        assert(len(a) != 0)
        for i in range(len(a)):
            assert(self.isNum(a[i]))
        mean = self.mean(a)
        var = self.D(a,2)
        skew = 0.0
        kurt = 0.0
        try:
            skew = self.D(a,3)/(self.D(a,2)**1.5)
            kurt = self.D(a,4)/(self.D(a,2)**2)
        except ZeroDivisionError, e:
            print 'except', e
        return [mean,var,skew,kurt]

    def mean(self, a):
        sum = 0.0
        for i in range(len(a)):
            sum += a[i]
        return sum/len(a)

    def D(self, a, n):
        sum = 0.0
        mean = self.mean(a)
        for i in range(len(a)):
            sum += (a[i]-mean)**n
        return sum/len(a)

    def isNum(self,value):
        try:
            value + 1
        except TypeError:
            return False
        else:
            return True
a = range(15)[5:8]

s = Solution()
# print scipy.stats.describe(a)
# print s.describe(a)
URL='http://112.124.1.3:8050/getData/101'
request = urllib.urlopen(URL)
content = request.read()
data = json.loads(content)['data']
for i in range(len(data)):
    if data[i][2] <= 5 or data[i][2]>=49 or (data[i][2]>10 and data[i][2]<=25) :
        print data[i]
