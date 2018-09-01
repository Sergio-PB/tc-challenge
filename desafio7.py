consultN = int(input())
scheduled = []
for _ in range(consultN):
    time = input().split(' ')
    scheduled.append((int(time[1]), int(time[0])))
scheduled.sort()

max = 1
current = 0
for next in range(consultN)[1:]:
    if scheduled[next][1] >= scheduled[current][0]: # if the next begins after I'm done
        current = next
        max += 1
print(max)
