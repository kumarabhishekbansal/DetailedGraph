class Solution:
    def findComponent(self,count,component,adj,vis,n):
        for i in range(n+1):
            if vis[i]==False:
                count+=1
                self.dfs(i,adj,vis,count,component)
        return (count,component)
            
    def dfs(self,src,adj,vis,count,component):
        vis[src]=True
        component[src]=count
        ne=adj[src]
        for i in ne:
            if vis[i]==False:
                self.dfs(i,adj,vis,count,component)

if __name__=="__main__":
    print("enter test case")
    t=int(input())
    while t>0:
        print("enter no. of vertices and edges seperated by space")
        n,e=map(int,input().split())
        adj=[[] for i in range(n+1)]
        vis=[False for i in range(n+1)]
        component=[-1 for i in range(n+1)]
        count=-1;
        for _ in range(e):
            print("enter src vertice and dest vertice to attach an edge between them")
            u,v=map(int,input().split())
            adj[u].append(v)
        print(" graph is ",adj);
        print();    
        ob=Solution()
        ans=ob.findComponent(count,component,adj,vis,n)
        print("final result : ",ans)
        t-=1