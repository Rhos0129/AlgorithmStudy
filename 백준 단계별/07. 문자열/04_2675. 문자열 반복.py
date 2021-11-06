n=int(input())
for i in range(n):
    n, string=input().split()
    for s in string:
        print(s*int(n), end='')
    print()