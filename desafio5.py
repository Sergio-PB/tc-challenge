while(True):
    IN = input().split(' ')
    competitors = int(IN[0])
    problems = int(IN[1])
    if(competitors == 0 and problems == 0):
        break

    tests = [1, 1, 1, 1]
    times_solved = [0] * problems
    for _ in range(competitors):
        inp = input().split(' ')
        try:
            solved = [int(i) for i in inp]
        except:
            solved = [int(i) for i in inp[:-1]] # empty char in the end
        soma = 0
        for s in range(len(solved)):
            val = solved[s]
            times_solved[s] += val
            soma += val
        if soma == problems: #somebody solved everything
            tests[0] = 0
        elif soma == 0:
            tests[3] = 0 #somebody solved nothing
    for t in times_solved:
        if t == 0: # a test was not solved by someone
            tests[1] = 0
        elif t == competitors: # a test was solved by everyone
            tests[2] = 0
    print(sum(tests))
