# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from numpy import linalg as LA

def plot_loghist(x, bins):
  hist, bins = np.histogram(x, bins=bins)
  logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
  plt.hist(x, bins=logbins)
  plt.xscale('log')
  
G = nx.DiGraph()
f = open("532projectdataset.txt", "r", encoding='utf-8', errors='ignore')
for line in f:
    varas = line.split()
    v = varas[1]
    u = varas[2]
    if(G.has_edge(v,u)):
        G[v][u]['weight'] += 1
    else:
        G.add_node(v)
        G.add_node(u)
        G.add_edge(v, u,weight = 1)
        

geo_List = []
nodeList = list(G.nodes)
edgeList = list(G.edges)
Wu = []
isOrNo = []
for i in G:
    Gu = nx.Graph()
    mwu = 0
    neighbors_list = list(nx.neighbors(G, i))
    if(len(neighbors_list) > 1):
        for k in range(len(neighbors_list)):
            Gu.add_edge(i,neighbors_list[k])
            t = k+1
            while t < len(neighbors_list):
                u = neighbors_list[t]
                v = neighbors_list[k]
                if G.has_edge(u,v) or G.has_edge(v,u):
                    if(G.has_edge(u,v)):
                        w = G.get_edge_data(u,v)
                        Gu.add_edge(u,v,weight = w['weight'])
                        mwu += w['weight']
                    else:
                        w = G.get_edge_data(v,u)
                        Gu.add_edge(u,v,weight = w['weight'])
                        mwu += w['weight']
                t += 1 
        if(len(Gu.edges) >= len(Gu.nodes)):
           geo_List.append(Gu)  
           Wu.append(mwu)
           isOrNo.append(1)
    else:
        isOrNo.append(0)
Vu = []
Eu = []
for k in range(len(geo_List)):
     Vu.append(len(geo_List[k].edges))
     Eu.append(len(geo_List[k].nodes))
     
#    print("For Gu "+str(k)+": ")
#    print("number of edges: "+ str(len(geo_List[k].edges)))
#    print("number of nodes: "+str(len(geo_List[k].nodes)))

    

#Vu vs Eu for each Gu
#
plt.figure()
plt.plot(Eu, Vu , 'o')
plt.xlabel('total number of edges of Gu')
plt.ylabel('total number of nodes of Gu')
plt.locator_params(axis='x', nbins=15)
plt.show()

#the least squarest on the median values for each bucket of points after applying logarithmic binning on the x-axis
x = pd.Series(Eu)
plot_loghist(x, 10)
#
###value of w;u versus Wu for each egonet Gu
#
D = np.diag(Wu)
ev = LA.eigvals(D)
plt.figure()
plt.plot(ev[::-1], Wu , 'ro')

plt.xlabel('eigenvalueof Gu')
plt.ylabel('weighed of each Gu')
plt.locator_params(axis='x', nbins=15)
plt.show()

#Part two
#maxve = 0       #max(E, CVa)
#minve = 10000000#min(E, CVa)
#maxwE = 0       #max(eigen, CWa)
#minwE = 10000000#min(eigen, CWa)

#f(Vu, Eu)
pointer = 0
ou1 = [] #o(u) for each nodes
ou2 = []
for i in isOrNo:
    if i == 0:
        ou1.append(nodeList[i])
        ou2.append(0)
    else:
        v = Vu[pointer]
        e = Eu[pointer]
        w = Wu[pointer]
        eg = ev[pointer]
        pointer +=1
        answer = (max(v, e)/min(v,e) )*np.log10(np.abs(e-v)+1)
        answer2 = (max(w,eg)/min(w,eg))*np.log10(np.abs(eg-w)+1)
        ou1.append(nodeList[i])
        ou2.append(answer)
        ou1.append(nodeList[i])
        ou2.append(answer2)
        
  
## find the 20 max value
#result = ou2.sort(reverse=True)
#for i in range(20):
#    print(result[i])
    
            
            