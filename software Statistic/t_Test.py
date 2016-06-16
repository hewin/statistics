#-*-coding:utf-8 -*-
# 计算t分布置信区间
import math
class Solution:
  def confidence_interval(self, obs):
    #t value is 2.1315 t0.95(15)
    mean = self.Mean(obs)
    var  = self.Var(obs)
    a = round(mean-2.1315/4*var,3)
    b = round(mean+2.1315/4*var,3)
    return (a,b)
    
  def Var(self, obs):
      sum = 0.0
      for i in range(len(obs)):
          sum += (obs[i]-self.Mean(obs))**2
      return math.pow(sum/(len(obs) - 1), 0.5)

  def Mean(self, obs):
      sum = 0.0
      for i in range(len(obs)):
          sum += obs[i]
      return sum/len(obs)


obs = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
s = Solution()
print s.Mean(obs)
print s.Var(obs)
print s.confidence_interval(obs)

