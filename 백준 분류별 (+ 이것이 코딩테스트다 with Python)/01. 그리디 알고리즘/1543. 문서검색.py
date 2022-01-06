page=input()
keyword=input()

cnt=0;
while True:
    idx = page.find(keyword)
    if idx==-1:
        print(cnt)
        break

    page = page[idx + len(keyword):]
    cnt += 1