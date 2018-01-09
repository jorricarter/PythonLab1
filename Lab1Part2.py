#todo get input
currentPhrase = input("If you provide me with words, I will convert them into a camelCase variable name.\n")
#todo separate by word
#found .title @stackoverflow while looking for way to make all lowercase
wordList = currentPhrase.title().split()
#todo all lowercase start with uppercase
#found .title() to acheive this
#todo first letter of first word should be lower case
wordList[0] = wordList[0].lower()
#todo join words into single word
newName = ''.join(wordList)
#todo print to screen
print (newName)
