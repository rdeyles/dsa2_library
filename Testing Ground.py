'''def test(check):
    n=4
    while len(check)<4:
        check.append(n)
        n=n+1
    print(check)

che=[7]
test(che)'''

'''import matplotlib.pyplot as mp

a=[1,2,3,4,5]

figure, axis = mp.subplots()

axis.plot(a,a, label='"a" array, plotted', c='r')  # Plot some data.

axis.scatter(a, a, label='"a" array, scattered')  # Plot some more data

axis.set_xlabel('x label')  # Add an x-label to the axes.

axis.set_ylabel('a values')  # Add a y-label to the axes.

axis.set_title("Plot vs Scatter")  # Add a title to the axes.

axis.legend()  # Add a legend

mp.show()'''

'''a="supercalifragilisticexpialidocious"
output=""
for i in range (0,10,2):
    output=output+a[0:i]
print(output)'''

import matplotlib.pyplot as mp
import networkx as nx

 

#undirected graph

 

G = nx.Graph()

 

G.add_node(1)

G.add_node(2)

 

G.add_edge(1,2)

 

nx.draw(G)

mp.show()
