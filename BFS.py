import matplotlib.pyplot as mp
import networkx as nx
from collections import deque
#from collections import deque
#def bfs(G,s)
#    q=deque()
G=nx.random_labeled_rooted_tree(10)
nx.draw(G,with_labels=True)
mp.show()

source=0
seen = set()
seen.add(source)
q=deque()
q.append(source)

while q:
    node=q.popleft()
    print(node)
    for neighbour in G[node]:
        if neighbour not in seen:
            seen.add(neighbour)
            q.append(neighbour)

