while(True):
    phrase = input().split(' ')
    if phrase[0] == '*':
        break
    
    ok = True
    letter = phrase[0][0].lower()
    for word in phrase:
        if word[0].lower() != letter:
            ok = False
            break
    print ('Y' if ok else 'N')
