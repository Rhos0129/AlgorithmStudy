a, b, c=int(input()), int(input()), int(input())
arr=[0]*10

for i in str(a*b*c):
    arr[int(i)]+=1

for i in arr:
    print(i)