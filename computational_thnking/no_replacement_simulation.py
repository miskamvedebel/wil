def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    ress = []
    for _ in range(numTrials):
        s = [1, 1, 1, 0, 0, 0]
        res = 0
        for _ in range(3):
            res += s.pop(random.randint(0, len(s) - 1))
        ress.append(res)

    return len(list(filter(lambda x: x == 3, ress))) / len(ress) + len(list(filter(lambda x: x == 0, ress))) / len(ress)