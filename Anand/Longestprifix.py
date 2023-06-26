def HighestVowels(words):
    maxVowelCount = 0
    wordWithMaxVowel = None

    for word in words:
        vowelCount = 0
        for char in word:
            if char.lower() in ('aeiou'):
                vowelCount = vowelCount+1

        if vowelCount>maxVowelCount:
            maxVowelCount = vowelCount
            wordWithMaxVowel = (word)


    return wordWithMaxVowel

words = ["banana","apple","mango","is","ds",'qwsdt']
callling = HighestVowels(words)
print(callling)

'''
banana = 3
apple = 2
mango = 2
is = 1
ds = 0
qwsdt = 0

'aeiou'
'''
'''
apple, application, applicant, coapplicant,appliances, app
'''

# output : app``

def longestPrefix(words):
    if not words:
        return("list is empty")
    
    words.sort()

    # wordss = []
    # for word in words:
    #     word = list(word)
    #     word.sort()
    #     word = ''.join(word)
    #     wordss.append(word)
    

    prefix = ""
    for i in range(len(words[0])):
        if (words[0][i]) == words[-1][i]:
            prefix = prefix + (words[0][i])
        else:
            break

    return prefix

words = ['apple', 'application', 'applicant','appliances', 'app']
print("longest prefix word is, ",longestPrefix(words))