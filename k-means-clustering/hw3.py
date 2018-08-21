import matplotlib.pyplot as plt
import random
import csv
import math


def iniCenters(points, k):
    idxs = []
    while len(idxs) < k:
        r = random.randrange(0, len(points))
        if r not in idxs:
            idxs.append(r)
    print(idxs)
    centers = []
    for idx in idxs:
        centers.append(points[idx])
    return centers


def d(point,center):
    x2 = math.pow(point["x"]-center["x"],2)
    y2 = math.pow(point["y"]-center["y"],2)
    dis = math.pow(x2+y2,0.5)
    return dis


def group(points,centers):
    for point in points:
        small_dis = math.inf
        small_idx = -1
        for idx,center in enumerate(centers):
            dis = d(point,center)
            if dis <small_dis:
                small_dis = dis
                small_idx = idx
        point["group"] = small_idx

def newCenter(points,k):
    # centers = [{
    #         "x": 0,
    #         "y": 0
    #     }]*k
    centers = []
    for i in range(0,k):
        centers.append({
            "x": 0,
            "y": 0
        })
    count = [0]*k
    print(centers)
    for point in points:
        group_idx = point["group"]
        # print(group_idx,point["x"],point["y"])
        centers[group_idx]["x"] = centers[group_idx]["x"]+point["x"]
        centers[group_idx]["y"] = centers[group_idx]["y"]+point["y"]
        count[group_idx] += 1
    for idx,center in enumerate(centers):
        center["x"] = center["x"]/count[idx]
        center["y"] = center["y"]/count[idx]
    print(count)
    print(centers)
    return centers

def drawGroup(points,colors):
    X = []
    Y = []
    color = []
    for point in points:
        X.append(point["x"])
        Y.append(point["y"])
        if len(colors)==1:
            color.append(colors[0])
        else:
            color.append(colors[point["group"]])
    plt.scatter(X, Y, color=color, marker='o', alpha=0.3, linestyle='None', picker=True)
def save(imgIdx):
    plt.savefig(imgName+str(imgIdx))
    plt.clf()
    imgIdx+=1
    return imgIdx

def draw(X, Y, color):
    plt.scatter(X, Y, color=color, marker='o', alpha=0.5, linestyle='None', picker=True)


def drawCenters(centers, colors,symbol):
    X = []
    Y = []
    for point in centers:
        X.append(point["x"])
        Y.append(point["y"])
    plt.scatter(X, Y, color=colors, marker=symbol, alpha=1, linestyle='None', picker=True, s=10**3, edgecolor='black')


if __name__ == '__main__':
    random.seed(500)
    csvfile = open('hw3_data.csv', newline="\n")
    reader = csv.DictReader(csvfile, delimiter=',')
    X = []
    Y = []
    points = []
    for row in reader:
        x = float(row["X"])
        y = float(row["Y"])
        # X.append(x)
        # Y.append(y)
        points.append({
            "x": x,
            "y": y
        })
    imgName = "img"
    imgIdx = 1
    # 1. draw all points
    drawGroup(points,["black"])
    imgIdx = save(imgIdx)

    k = 5
    colors = ["black","red","yellow","blue","brown"]

    centers = iniCenters(points, 5)
    for i in range(0,100):
        # 2. assign points to nearest group
        print(centers)
        group(points,centers)
        # drawGroup(points,colors)
        # drawCenters(centers,colors,"*")
        # imgIdx = save(imgIdx)

        # 3. create new centers

        centers = newCenter(points, k)
        if i%10 ==0:
            drawGroup(points,colors)
            drawCenters(centers,colors,"*")
            imgIdx = save(imgIdx)

