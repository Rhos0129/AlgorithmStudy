def solution(answers):

    # 학생들의 답 생성
    student1=[]; student2=[]; student3=[]
    for i in range(len(answers)):
        student1.append([1, 2, 3, 4, 5][i%5])
        student2.append([2, 1, 2, 3, 2, 4, 2, 5][i%8])
        student3.append([3, 3, 1, 1, 2, 2, 4, 4, 5, 5][i%10])

    # 정답 비교
    results={1:0, 2:0, 3:0}
    for i in range(len(answers)):
        if student1[i]==answers[i]:
            results[1]+=1
        if student2[i]==answers[i]:
            results[2]+=1
        if student3[i]==answers[i]:
            results[3]+=1

    # 최고점수 찾기
    answer=sorted([k for k, v in results.items() if v==max(results.values())])

    return answer