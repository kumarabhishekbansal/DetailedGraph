class Solution:
    def dfs(self,src,adj,vis,res):
        if vis[src]: return
        res.append(src)
        vis[src]=True
        ne=adj[src]
        for i in ne:
            if vis[i]==False:
                self.dfs(i,adj,vis,res)
        return res    

if __name__ == '__main__':
    t=int(input());  # test case
    while(t>0):
        # n=no. of nodes  and e=no. of edges
        n,e=map(int,input().split())
        adj=[[] for i in range(n+1)]
        vis=[False for i in range(n+1)]
        for _ in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        start_node=0
        res=[]
        ans=ob.dfs(start_node,adj,vis,res)
        # print(res,ans)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        t-=1    

