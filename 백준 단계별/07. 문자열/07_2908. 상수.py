num1, num2=map(int, input().split())
myNum1, myNum2=int(str(num1)[::-1]), int(str(num2)[::-1])
print(max(myNum1, myNum2))