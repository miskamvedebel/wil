def maxStrength(nums: list[int]) -> int:
    def combinations(iterable, r):
            # combinations('ABCD', 2) --> AB AC AD BC BD CD
            # combinations(range(4), 3) --> 012 013 023 123
        pool = tuple(iterable)
        n = len(pool)
        if r > n:
            return
        indices = list(range(r))
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
            yield tuple(pool[i] for i in indices)
    def multiply(iterable):
        m = 1
        for i in iterable:
            m *= i
        return m
        
    L = len(nums)
    mx = None
    for r in range(1, L+1):
        temp = max(map(lambda m: multiply(m), combinations(iterable=nums, r=r)))
        if not mx:
            mx = temp
        elif mx < temp:
            mx = temp
    return mx

if __name__ == '__main__':

    test_cases = [
            [3,-1,-5,2,5,-9],
            [-4,-5,-4],
            [1, 2, -1],
            [1, 0, 1, 1]
        ]
    answers = [1350, 20, 2, 1]

    for i, test_case in enumerate(test_cases):
        assert answers[i] == maxStrength(nums=test_case)
