while(True):
    IN = input()

    X1 = int(IN[0])
    Y1 = int(IN[2])
    X2 = int(IN[4])
    Y2 = int(IN[6])
    
    if X1 == 0 and Y1 == 0 and X2 == 0 and Y2 == 0:
        break
    print (int(1 if (abs(X1-X2)==abs(Y1-Y2) and (X1!=X2)) else (0 + ((X1!=X2)*1) + ((Y1!=Y2)*1))))
