n=int(input())
scores=[int(i) for i in input().split()]
maxScore=max(scores)

fakeScores=[]
for score in scores:
    fakeScores.append(score/maxScore*100)

print(sum(fakeScores)/n)