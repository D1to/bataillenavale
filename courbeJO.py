import matplotlib.pyplot as plt

q = int(input("q="))
k = int(input("k="))

n = int(input("n (la dernière valeur souahaitez) = "))


x,y = [],[]
for p in range(1,n+1):
    x.append(p*q)
    y.append(int((q**(2) * p**(2))/k))

plt.plot(x,y)
plt.show()

