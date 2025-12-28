n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(n1,n2,n3):
    return 0 <= n1 and n1 < n and 0 <= n2 and n2 < n and 0<= n3 and n3 < n

l= []

for i in range(n):
    for j in range(n):
        
        if in_range(j,j+1,j+2):
            l.append([(i,j),(i,j+1),(i,j+2)])
        

ans = 0
        
for i in range(len(l)-1):
    for j in range(i+1,len(l)):

        if set(l[i]) & set(l[j]):
            continue

        else:
            cnt = 0


            for p1 in l[i]:

                x,y = p1[0],p1[1]

                if arr[x][y] == 1:
                    cnt += 1

            for p2 in l[j]:

                x,y = p2[0],p2[1]
                if arr[x][y] == 1:
                    cnt += 1
            
            ans = max(ans,cnt)

print(ans)


                

    

