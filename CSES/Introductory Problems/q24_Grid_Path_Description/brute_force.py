def fn(r,c, step,stop,vis,n):
    vis[r][c] = True
    if(r== n-1 and c==0 ):
        if step == stop:
            vis[r][c] = False
            return 1
        vis[r][c] = False
        return 0
    
    right,left,up,down = 0,0,0,0

    if(r+1 < n and vis[r+1][c]==False):
        up+=fn(r+1,c,step+1,stop,vis,n)
    if(r-1 >= 0 and vis[r-1][c]==False):
        down+=fn(r-1,c,step+1,stop,vis,n)
    if(c+1 <n and vis[r][c+1]==False):
        right+=fn(r,c+1,step+1,stop,vis,n)
    if(c-1 >=0 and vis[r][c-1]==False):
        left+=fn(r,c-1,step+1,stop,vis,n)
    
    vis[r][c]=False
    return up+down+left+right

n = int(input())
cnt = 0
vis = [[False for _ in range(n)] for _ in range(n)]
cnt = fn(0,0,0,n*n-1, vis, n)
print(cnt)