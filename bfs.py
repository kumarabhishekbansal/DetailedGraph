from collections import deque
class Solution:

    def reconstructPath(self,start,end,prev): # path construct from start node to end node
        path=[]
        at=e
        for _ in iter(lambda:at is not None,False):
            path.append(at)
            at=prev[at]
        path.reverse()

        if path[0]==start:return path
        return []   

    def solve(self,src,adj,n):
        q=deque([src])
        vis=[False for i in range(n)]
        vis[src]=True
        prev=[None for i in range(n)]
        bfspath=[]
        while q:
            parent=q.popleft()
            ne=adj[parent]
            bfspath.append(parent)
            for i in ne:
                if vis[i]==False:
                    q.append(i)
                    vis[i]=True
                    prev[i]=parent
        return (bfspath,prev)

    def bfs(self,adj,start,end,vertices):

        bfspath,prev=self.solve(start,adj,vertices)
        return (bfspath,self.reconstructPath(start,end,prev))

if __name__=="__main__":
    print("enter test case")
    t=int(input())
    while t>0:
        print("enter no. of vertices and edges seperated by space")
        n,e=map(int,input().split())
        adj=[[] for i in range(n)]
        
        for _ in range(e):
            print("enter src vertice and dest vertice to attach an edge between them")
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        print(" graph is ",adj);
        print();    
        ob=Solution()
        res,ans=ob.bfs(adj,0,n-1,n)
        print("bfs path is : ",res)
        print("path from start node to end node is : ",ans)
        t-=1