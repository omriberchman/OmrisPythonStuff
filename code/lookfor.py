import os

text = input("Enter your text ")
lowertext = text.lower()
word = input('insert a word to count ')
count = lowertext.count(word)
print(word+" is written "+ str(count)+" times")
os.system('pause')