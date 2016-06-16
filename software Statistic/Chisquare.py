#-*-coding:utf-8 -*-
# 卡方优度检验
import numpy as np

class Solution:
    def chisquare(self, f_obs, f_exp=None):
        f_obs = self.splite_obs(f_obs)
        sum = self.sum(f_obs)
        result = 0.0
        for i in range(len(f_obs)):
            result += f_obs[i]**2/(sum/len(f_obs))
        result = result - sum
        return result


    def sum(self,f_obs):
        sum = 0.0
        for i in range(len(f_obs)):
            sum += f_obs[i]
        return sum

    def splite_obs(self,f_obs):
        f_obs = sorted(f_obs)
        print f_obs
        obs = []
        i = 0
        for i in range(len(f_obs)):
            if f_obs[i] >= 5:
                obs.append(f_obs[i])
            else:
                f_obs[i+1] += f_obs[i]
        return obs

f_obs = [16,18,16,14,12,12]
f_exp = [16,16,16,16,16,8]
# s = Solution()
# print s.chisquare(f_obs)

def chis_2(f_obs,f_exp = None):
    sum = 0.0
    if f_exp != None:
        for i in range(len(f_exp)):
            sum += (float)(f_obs[i]-f_exp[i])**2/f_exp[i]
    else:
        for i in range(len(f_obs)):
            sum += (f_obs[i]-np.mean(f_obs))**2/np.mean(f_obs)
    return sum

print chis_2(f_obs)



