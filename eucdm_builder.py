from basestructures import BaseStructures
from graphs import Graph
from graphs import Node
import sys

def printDETable(filename):
    bs = BaseStructures()
    det = bs.constructDict(filename)
    for k in det:
        print(k, ' > ', det[k])

def printDict2(filename):
    bs = BaseStructures()
    dd = bs.constructDict2(filename)
    g = Graph([], [], dd, bs)

    for k in dd:
        g.showGraph2(dd[k])

    print(len(dd.keys()), ' keys on level 1.')

def getRelations():
    # Testdata: [parentID, childID, cardinality].
    # Define the relation table here.
    # Link parent to child node, with cardinality.
    relation = []
    relation.append([100,164,1])
    relation.append([100,107,1])
    relation.append([100,109,1])
    relation.append([100,373,1])
    relation.append([100,249,1])
    relation.append([100,171,1])
    relation.append([100,405,1])
    relation.append([100,229,1])

    return relation

def buildGraph(filename):
    bs = BaseStructures()
    DETable = bs.constructDict(filename)
    dict2 = bs.constructDict2(filename)
    mygraf = Graph(getRelations(), DETable, dict2, bs)
    root = Node()
    root.setData(100)
    mygraf.buildGraph(root)
    mygraf.showGraph(root)

def insertStatementsDE(dedict, delist):
    for r in delist:
        txt = dedict[r[4]][0]
        print("insert into dataelement (denum, denum1, denum2, denum3, denum4, key) values ('" + txt + "',", r[0],',', r[1],',', r[2],',', r[3],',',  r[4], ");");

filename = sys.argv[1]          # File containing the data elements (I use a dump of CW's Excel file).

if sys.argv[2] == 'detable':
    printDETable(filename)
elif sys.argv[2] == 'dict2':
    printDict2(filename)
elif sys.argv[2] == 'graf':
    buildGraph(filename)
else:
    print('No cmd.')


