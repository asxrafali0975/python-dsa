class Solution:
    def isCyclic(self, V, edges):
        adjlist = self.adlistfunc(V,edges)
        start_node_hasharr  = set()
        path_hasharr = set()
        
        for node in range(V):
            if node not in start_node_hasharr:
                if self.dfs( node , start_node_hasharr ,path_hasharr ,adjlist ):
                    return True
        return False
        
        
    def dfs(self, current_node , start_node_hasharr ,path_hasharr ,adjlist):
        start_node_hasharr.add(current_node)
        path_hasharr.add(current_node)
        
        for x in adjlist[current_node]:
            if x not in start_node_hasharr:
                if self.dfs(x , start_node_hasharr ,path_hasharr ,adjlist):
                    return True
            elif x in path_hasharr:
                return True
                    
        
        path_hasharr.discard(current_node)          
        return False
        
        

        
    def adlistfunc(self, V , edges):
        adjlist = [[] for _ in range(V)]
        
        for x in edges:
            a,b = x
            adjlist[a].append(b)
            
        return adjlist
        
