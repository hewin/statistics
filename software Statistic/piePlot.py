import matplotlib.pyplot as plt

lables = ['USA','CHINA','INDIA','JAPAN','GERMANY','RUSSIA','BRAZIL','UK','FRANCE','ITALY']
quants = [15094025,11299967,4457784,4440376,3099080,2383402,2293954,2260803,2217900,184650]

plt.figure(1,figsize=(6,6))

def explode(lable,target = 'CHINA'):
    if lable == target:
        return 0.1
    else:
        return 0
expl = map(explode,lables)

colors = ["pink","coral","yellow","orange"]

plt.pie(quants,explode = expl,colors=colors,labels=lables,autopct='%1.1f%%',pctdistance=0.8,shadow=False)
plt.title('Topp 10 GDP Countries',bbox={'facecolor':'0.8','pad':5})
plt.show()