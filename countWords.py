introString =input('enter your introduction: ')
characterCount= 0
wordCount= 1
for i in introString:
    characterCount= characterCount+1
    if(i==' '):
        wordCount= wordCount+1
print('number of word in the string: ')
print(wordCount)
print('number of word in the string: ', wordCount)        
print('number of character in the string: ', characterCount)    