class Solution:
    def isCycle(self, V, edges):
        adjlist = self.adlistfunc(V,edges)
        hasharr = set()
        
        
        for node in range(V):
            if node not in hasharr:
                if self.dfs(-1 , node , hasharr , adjlist):
                    return True
        return False
        
    def dfs(self, parent_node , current_node , hasharr , adjlist):
        hasharr.add(current_node)
        
        for x in adjlist[current_node]:
            if x!=parent_node and x not in hasharr:
                if self.dfs(current_node , x , hasharr , adjlist):
                    return True
            elif x!=parent_node and x in hasharr:
                return True
        return False;
                
           
        
    
        
        
    def adlistfunc(self, V , edges):
        adjlist = [[] for _ in range(V)]
        
        for x in edges:
            a,b = x
            adjlist[a].append(b)
            adjlist[b].append(a)
        return adjlist
        
        
        
        
    
        
