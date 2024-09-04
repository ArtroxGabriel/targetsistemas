def fib(N: int) -> int:
    if N == 1:
        return 0
    if N == 2:
        return 1
    return fib(N - 1) + fib(N - 2)


def is_in_Fibonacci(X: int) -> bool:
    if X < 0:
        return False
    i: int = 1
    aux: int = fib(i)
    while aux <= X:
        if aux == X:
            return True
        i += 1
        aux = fib(i)
    return False


isTrue: bool = is_in_Fibonacci(int(input()))
if isTrue:
    print("Esta")
else:
    print("nao")
