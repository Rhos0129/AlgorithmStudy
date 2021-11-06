string=input().lower()
arr=[0]*26
for s in string:
    arr[ord(s)-97]+=1

result=chr(arr.index(max(arr))+97).upper()
if max(arr) in arr[arr.index(max(arr))+1:]:
    result='?'
print(result)