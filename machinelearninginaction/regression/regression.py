from numpy import *

def loadDataSet(filename):
    numFeat = len(open(filename).readline().split('\t')) -1
    dataMat =[]
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineAttr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineAttr.append(float(curLine[i]))
        dataMat.append(lineAttr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

#test
# dataMat,labelMat = loadDataSet("ex0.txt")
# print dataMat
# print labelMat

def standRegree(xArr,yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0.0:
        print "this matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws

#test
# xArr,yArr = loadDataSet("ex0.txt")
# ws = standRegree(xArr,yArr)
# xMat = mat(xArr)
# yMat = mat(yArr)
# yhat = xMat * ws

