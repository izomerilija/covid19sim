import matplotlib.pyplot as plt

plt.ion()

x1 = [1,2,3,4,5]
y1 = [1,1,2,3,5]
y2 = [1,2,4,8,16]

for i in range(50):
    plt.figure(1)
    plt.plot(x1,y1)
    plt.show()
    plt.figure(3)
    plt.plot(x1,y2)
    plt.show()
    plt.pause(0.001)
    if i !=49:
        plt.clf()
    x1.append(i+6)
    y1.append(y1[i+4]+y1[i+3])
    y2.append(y2[i+4]*2)

nesto = input()