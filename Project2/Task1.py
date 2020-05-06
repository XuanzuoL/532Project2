import networkx as nx
import matplotlib as plt
import time

G = nx.DiGraph()
f = open("/Users/christianliu/Desktop/CSI532/project/532projectdataset.txt", "r", encoding='utf-8', errors='ignore')
for line in f:
    date_week = time.strftime("%A", time.gmtime(int(line.split(' ')[0]) / 1000))
    if date_week != "Sunday" or date_week != "Saturday":
        G.add_node(line.split(' ')[1])
        G.add_node(line.split(' ')[2].strip('\n'))
        G.add_edge(line.split(' ')[1], line.split(' ')[2].strip('\n'))
    # print(line.split(' ')[2])
bidi_edge = 0
visited_edge = []
for i in G.nodes():
    visited_edge.append(i)
    for j in G.nodes():
        if G.has_edge(i,j):
            if j not in visited_edge:
                bidi_edge += 1

degree_vals = G.degree()
in_degree_vals = G.in_degree()
out_degree_vals = G.out_degree()
deg_uniq = sorted(dict(degree_vals).values())
deg_hist = [list(dict(degree_vals).values()).count(x) for x in deg_uniq]

in_deg_uniq = sorted(dict(in_degree_vals).values())
in_deg_hist = [list(dict(in_degree_vals).values()).count(x) for x in in_deg_uniq]

out_deg_uniq = sorted(dict(out_degree_vals).values())
out_deg_hist = [list(dict(out_degree_vals).values()).count(x) for x in out_deg_uniq]

plt.figure()
plt.loglog(deg_uniq, deg_hist, 'ro-')
plt.loglog(in_deg_uniq, in_deg_hist, 'go-')
plt.loglog(out_deg_uniq, out_deg_hist, 'yo-')
plt.xlabel('Degree')
plt.ylabel('Number of nodes')
plt.show()

print("Number of node is:",nx.number_of_nodes(G))
print("Number of edge is:",nx.number_of_edges(G))
print("Number of bidirectional edge is:",bidi_edge)
print("Min number of other addresses each email address has interacted with is:",min(deg_uniq))
print("Max number of other addresses each email address has interacted with is:",max(deg_uniq))
print("Ave number of other addresses each email address has interacted with is:",sum(deg_uniq)/len(deg_uniq) )
print("Diameter of the network is:",nx.diameter(G))

