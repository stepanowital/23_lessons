def fib(n):
    index = 0
    prev = 0
    current = 1
    while index < n:
        index += 1
        if index < 3:
            yield index - 1
            continue
    res = current + prev
    prev = current
    current = res
    yield res
