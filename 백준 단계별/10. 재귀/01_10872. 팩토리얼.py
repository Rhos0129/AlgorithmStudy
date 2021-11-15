def factorial(n):
    def recur(n, result):
        if n <= 0:
            print(result)
            return
        else:
            result *= n
        recur(n - 1, result)

    recur(n, 1)


n = int(input())
factorial(n)