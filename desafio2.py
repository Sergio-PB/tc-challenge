case = 0
while(True):
    IN = input().split(' ')
    N = IN[0]
    Q = IN[1]
    if N == '0' and Q == '0':
        break
    case += 1
    print("CASE# "+str(case)+":")
    marbles = []
    positions = {}
    for _ in range(int(N)):
        number = int(input())
        marbles.append(number)
    marbles.sort()
    p = 1
    for marble in marbles:
        if marble not in positions:
            positions[marble] = p
        p += 1
    for _ in range(int(Q)):
        query = int(input())
        if query in positions:
            print (str(query) + " found at " + str(positions[query]))
        else:
            print (str(query) + " not found")
