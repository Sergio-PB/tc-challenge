instances = int(input())
for _ in range(instances):
    IN = input().split(' ')
    words = int(IN[0])
    phrases = int(IN[1])

    dic = {}
    for _ in range(words):
        jp = input()
        pt = input()
        dic[jp] = pt
    for _ in range(phrases):
        line = input().split(' ')
        translated = ''
        for word in line:
            translated += (dic[word]+' ' if word in dic else word+' ')
        translated = translated[:-1]
        print (translated)
    print("")
