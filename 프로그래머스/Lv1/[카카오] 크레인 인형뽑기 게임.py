def solution(board, moves):
    answer = 0

    selected=[]
    for move in moves:
        for i in range(len(board[0])):
            target=board[i][move-1]
            if target!=0:
                board[i][move-1]=0
                if selected!=[] and selected[-1]==target:
                    answer+=1
                    selected.pop(-1)
                else:
                    selected.append(target)
                break
            else:
                pass

    return answer*2