import matplotlib.pyplot as plt
import numpy as np
import math
import random
import csv




def data(muX,sigmaX,muY,sigmaY):
    X = np.random.normal(muX,sigmaX,100)
    Y = np.random.normal(muY,sigmaY,100)
    return X, Y


def data_csv(X, Y):
    datacsv = []#[["X", "Y"]]
    for i in range(0, len(X)):
        datacsv.append([X[i], Y[i]])
    return datacsv


def writeFile(datacsv):
    myFile = open('hw3_data.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(datacsv)

    print("Writing complete")

def draw(X, Y):
    plt.scatter(X, Y, color="black", marker='o', alpha=0.5, linestyle='None', picker=True)


def onpick(event):
    ind = event.ind
    print('onpick3 scatter:', ind)


if __name__ == '__main__':
    random.seed(2000)
    fig = plt.figure()
    fig.canvas.mpl_connect('pick_event', onpick)

    X1, Y1 = data(-2,1,2,2)
    X2, Y2 = data(5,1,1,1)
    X3, Y3 = data(10,1,4,3)
    X4, Y4 = data(4,1,12,3)
    X5, Y5 = data(4,1.3,-8,2)
    datacsv1 = data_csv(X1,Y1)
    datacsv2 = data_csv(X2,Y2)
    datacsv3 = data_csv(X3,Y3)
    datacsv4= data_csv(X4,Y4)
    datacsv5 = data_csv(X5,Y5)
    datacsv = datacsv1+datacsv2+datacsv3+datacsv4+datacsv5
    np.random.shuffle(datacsv)

    print(datacsv)
    datacsv.insert(0,["X","Y"])
    writeFile(datacsv)

    draw(X1, Y1)
    draw(X2, Y2)
    draw(X3, Y3)
    draw(X4, Y4)
    draw(X5, Y5)
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()
