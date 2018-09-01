import math
while(True):
    IN = input().split(' ')
    w = int(IN[0])
    h = int(IN[1])
    if w == 0 and h == 0:
        break

    if (2*math.pi*h/3) <= w:
        v1 = (math.pi*(h**3))/27
    else:
        r = w/(2*math.pi)
        v1 = math.pi*(r**2)*(h-(2*r))

    r = h/(2*(math.pi+1))
    if 2*r > w:
        r = w/2
    v2 = math.pi*(r**2)*w
    print(round(max(v1,v2)*1000)/1000)
