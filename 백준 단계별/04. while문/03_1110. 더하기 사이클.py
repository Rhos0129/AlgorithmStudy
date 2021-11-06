firstNum=input()
tmp=firstNum
cnt=0
while True:
    if cnt!=0 and firstNum==tmp:
        print(cnt)
        break
    a=int(tmp)//10 # 10의 자리
    b=int(tmp)%10 # 1의 자리
    tmp=str(b*10+(a+b)%10)
    cnt+=1