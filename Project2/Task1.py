import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
f = open("/Users/christianliu/Desktop/CSI532/project/532projectdataset.txt", "r", encoding='utf-8', errors='ignore')
for line in f:
    G.add_node(line.split(' ')[1])
    G.add_node(line.split(' ')[2])
    G.add_edge(line.split(' ')[1], line.split(' ')[2])
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
deg_uniq = sorted(dict(degree_vals).values())
print("Number of node is:",nx.number_of_nodes(G))
print("Number of edge is:",nx.number_of_edges(G))
print("Number of bidirectional edge is:",bidi_edge)
print("Min number of other addresses each email address has interacted with is:",min(deg_uniq))
print("Max number of other addresses each email address has interacted with is:",max(deg_uniq))
print("Ave number of other addresses each email address has interacted with is:",sum(deg_uniq)/len(deg_uniq) )
print("Diameter of the network is:",nx.diameter(G))

