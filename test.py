import numpy as np
import networkx as nx
from GK_WL import GK_WL

if __name__ == '__main__':

    # g1 = nx.Graph([(1, 2), (2, 3), (1, 3)]) # BUG!
    # g2 = nx.Graph([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)]) # BUG!
    g1 = nx.Graph([(0, 1), (1, 2), (0, 2)])
    g2 = nx.Graph([(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])
    
    gk = GK_WL()

    print gk.compare(g1, g2)
    print gk.compare_normalized(g1, g2)
    print gk.compare_list([g1, g2])
    print gk.compare_list_normalized([g1, g2])
    
    
