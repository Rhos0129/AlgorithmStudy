def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_list = list(skill) # 리스트 초기화
        for s in skill_tree:
            # 배울 스킬이 스킬트리에 있지만 그 스킬이 skill_list의 첫 선행스킬이 아니라면 다음 스킬트리로 이동
            if s in skill and s != skill_list.pop(0):
                break
        else: # 배울 스킬과 스킬트리의 순서가 일치하여 skill_list가 빈리스트가 되어가 뒷부분만 남았을 경우
            answer += 1

    return answer
