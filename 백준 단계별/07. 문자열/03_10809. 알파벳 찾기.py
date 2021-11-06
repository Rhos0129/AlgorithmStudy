string=input()
arr=[chr(i) for i in range(97, 123)]

for i in arr:
    print(string.find(i), end=' ')