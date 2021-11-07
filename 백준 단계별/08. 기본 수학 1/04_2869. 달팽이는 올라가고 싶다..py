a, b, v=map(int, input().split())

days=(v-b)//(a-b)
if (v-b)%(a-b)!=0:
    days+=1
print(days)