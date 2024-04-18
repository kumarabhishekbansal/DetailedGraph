if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        print(V);
        print(type(V));
        print(E);
        print(type(E));
        adj = [[] for i in range(V)]
        print(adj);
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        print(adj);    
       