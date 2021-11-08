n=int(input())
for i in range(n):
    k, n=int(input()), int(input()) # 층, 호

    dict={0:range(n+1)}
    for i in range(1, k+1):
        if dict.get(i, 0)==0:
            dict[i]=[sum(dict[i-1][:j+1]) for j in range(0, n+1)]
        if i==k:
            print(dict[k][n])
            break
