import networkx as nx
import matplotlib.pyplot as plt
import time

G = nx.DiGraph()
f = open("/Users/christianliu/Desktop/CSI532/project/532projectdataset.txt", "r", encoding='utf-8', errors='ignore')
weakly_con_compo = []
strongly_con_compo = []
density = []
clustering = []
current_day = "Sunday"
day = []

for line in f:
    # print(time.strftime("%A", time.gmtime(int(line.split(' ')[0])/1000)))
    date_week = time.strftime("%A", time.gmtime(int(line.split(' ')[0])/1000))
    if date_week != "Sunday" or date_week != "Saturday":
        G.add_node(line.split(' ')[1])
        G.add_node(line.split(' ')[2].strip('\n'))
        G.add_edge(line.split(' ')[1], line.split(' ')[2].strip('\n'))
        if current_day != date_week:
            current_day = date_week
            day.append(date_week)
            weakly_con_compo.append(len(max(nx.strongly_connected_components(G),key=len)))
            strongly_con_compo.append(len(max(nx.weakly_connected_components(G),key=len)))
            density.append(nx.density(G))
            clustering.append(nx.average_clustering(G))

plt.figure()
plt.plot(day, weakly_con_compo, 'ro-')
plt.plot(day, strongly_con_compo, 'bo-')
plt.plot(day, density, 'yo-')
plt.plot(day, clustering, 'go-')
plt.xlabel('Day')
plt.ylabel('Results')
plt.show()


