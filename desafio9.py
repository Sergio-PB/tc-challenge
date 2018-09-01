# def weight(item, extWeight):
#     if type(item) == str:
#         return extWeight
#     else:
#         return [weight(item[0], extWeight*2), weight(item[1], extWeight*3), extWeight]
#
# for _ in range(int(input())):
#     postfix = input()
#     position = 0
#     nested = []
#     for letter in postfix:
#         if ord(letter)<90: # uppercase
#             nested[position-2] = [nested[position-2], nested[position-1], letter]
#             nested.pop()
#             position -= 1
#         else:
#             nested.insert(position, letter)
#             position += 1
#     weightedList = weight(nested[0], 1)
#     unnestedWeight = unnest(weightedList)
#     unnestedTerms = unnest(nested)
#     print(unnestedTerms)
#     print(unnestedWeight)

for _ in range(int(input())):
    postfix = input()
    if postfix == '':
        postfix = input()
    nested = []
    position = 0
    for letter in postfix:
        if ord(letter)<90:
            nested[position-2] = [nested[position-2], nested[position-1], letter]
            nested.pop()
            position -= 1
        else:
            nested.insert(position, letter)
            position += 1
    queued = ''
    while(nested != []):
        subNested = []
        for term in nested:
            if type(term)==list:
                queued = term[2] + queued
                subNested.append(term[0])
                subNested.append(term[1])
            else:
                queued = term + queued
        nested = subNested
    print(queued)
