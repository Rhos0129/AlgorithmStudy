def pibonacci(n):
    sequence = [0]

    def recur(nth):
        if nth == n:
            print(sequence[n])
            return
        if nth == 0:
            sequence.append(1)
        else:
            sequence.append(sequence[-2] + sequence[-1])
        recur(nth + 1)

    recur(0)


n = int(input())
pibonacci(n)