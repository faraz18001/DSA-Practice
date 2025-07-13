class Graph:
    def __init__(self):
        self.G={}
        
        
    def add_node(self,node):
        if node not in self.G.keys():
            self.G[node]=[]
            return True
        return False
    
    
    def add_edge(self,v1,v2):
        if v1 in self.G.keys() and v2 in self.G.keys():
            self.G[v1].append(v2)
            self.G[v2].append(v2)
            return True
        
        
    def remove_node(self,G,node ):
        if node in G.key():
            for other_node in G[node]:
                G[other_node].remove(node)
                
        
        
        
        
        
    
        