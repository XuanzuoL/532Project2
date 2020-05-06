import networkx as nx
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np
import time

G = nx.DiGraph()
f = open("/Users/christianliu/Desktop/CSI532/project/532projectdataset.txt", "r", encoding='utf-8', errors='ignore')
for line in f:
    date_week = time.strftime("%A", time.gmtime(int(line.split(' ')[0]) / 1000))
    if date_week != "Sunday" or date_week != "Saturday":
    G.add_node(line.split(' ')[1])
    G.add_node(line.split(' ')[2])
    G.add_edge(line.split(' ')[1], line.split(' ')[2].strip('\n'))
    # print(line.split(' ')[2].strip('\n'))

degree_vals = G.degree()
in_degree_vals = G.in_degree()
out_degree_vals = G.out_degree()
deg_uniq = sorted(dict(degree_vals).values())
deg_hist = [list(dict(degree_vals).values()).count(x) for x in deg_uniq]
X = np.log10(deg_uniq)
Y = np.log10(deg_hist)
X_para = []
Y_para = []
for single_square_feet, single_price_value in zip(X, Y):
    X_para.append([float(single_square_feet)])
    Y_para.append(float(single_price_value))
regr = linear_model.LinearRegression()
regr.fit(X_para, Y_para)


in_deg_uniq = sorted(dict(in_degree_vals).values())
in_deg_hist = [list(dict(in_degree_vals).values()).count(x) for x in in_deg_uniq]
in_X = np.log10(in_deg_uniq)
in_Y = np.log10(in_deg_hist)
in_X_para = []
in_Y_para = []
for single_square_feet, single_price_value in zip(in_X, in_Y):
    in_X_para.append([float(single_square_feet)])
    in_Y_para.append(float(single_price_value))
regr = linear_model.LinearRegression()
regr.fit(in_X_para, in_Y_para)


out_deg_uniq = sorted(dict(out_degree_vals).values())
out_deg_hist = [list(dict(out_degree_vals).values()).count(x) for x in out_deg_uniq]
out_X = np.log10(out_deg_uniq)
out_Y = np.log10(out_deg_hist)
out_X_para = []
out_Y_para = []
for single_square_feet, single_price_value in zip(out_X, out_Y):
    out_X_para.append([float(single_square_feet)])
    out_Y_para.append(float(single_price_value))
regr = linear_model.LinearRegression()
regr.fit(out_X_para, out_Y_para)


plt.figure()
plt.loglog(deg_uniq, deg_hist, 'ro-')
plt.plot(X_para, regr.predict(X_para), color='red',linewidth=3)

plt.loglog(in_deg_uniq, in_deg_hist, 'go-')
plt.plot(in_X_para, regr.predict(in_X_para), color='green',linewidth=3)

plt.loglog(out_deg_uniq, out_deg_hist, 'yo-')
plt.plot(out_X_para, regr.predict(out_X_para), color='yellow',linewidth=3)

plt.xlabel('Degree/Out_Degree/In_Degree')
plt.ylabel('Number of nodes')
plt.show()