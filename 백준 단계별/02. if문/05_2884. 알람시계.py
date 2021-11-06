h, m = map(int, input().split())

setTime = (h * 60 + m) - 45
if setTime < 0:
    setTime += 24 * 60

setH = setTime // 60
setM = setTime % 60
print(f'{setH} {setM}')