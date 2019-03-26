#Name:  AdrianRandall
#Date:  October 2017
# 35

nombres= input("")
allnombres = nombres.split(';')

for c in allnombres:
    temp = c.split(',')
    print(temp[1],temp[0])
