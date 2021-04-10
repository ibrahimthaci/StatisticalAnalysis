#Statistical analysis of the book of Ismail Kadare called "Prilli thyer"
#Paola-Calvetti-Të-pafajshmit
# import PyPDF4
# from PyPDF4 import PdfFileReader
# file = open("C:/Users/Ibrahim/Downloads/IsmailKadare.pdf", 'rb')
# pdf_reader = PyPDF4.PdfFileReader(file)
# page = pdf_reader.getPage(1-100)
# print(page.extractText())
from matplotlib import pyplot as plt
from collections import Counter


# file = open("Book.txt","r",encoding='utf-8').read().lower().replace('?','').replace('.','').replace(',','').split()
# counter=Counter(file)
# print(counter)

file = open("Book.txt", "r", encoding='utf8')
inputFile = file.read().lower()
# for i in inputFile:
#     if(len(i)<3):
#         continue
#     print(i, end='') this blcok of code if we want to display words but not e i words with 1-2 lettersi

Words = inputFile.replace('.',' ').replace(',',' ').replace('!','').replace('?',' ').replace('\'',' ').replace('"',' ').replace(':',' ').replace(';',' ').split()
Sentences = inputFile.replace('?','.').replace('!','.').split('.')

letters = {'a':0,'b':0,'c':0,'ç':0,'d':0,'dh':0,'e':0,'ë':0,'f':0,'g':0,'gj':0,'h':0,'i':0,'j':0,'k':0,'l':0,'ll':0,'m':0,
           'n':0,'nj':0,'o':0,'p':0,'q':0,'r':0,'rr':0,'s':0,'sh':0,'t':0,'th':0,'u':0,'v':0,'x':0,'xh':0,'w':0,'y':0,'z':0,'zh':0, '.':0, ',':0, '?':0, '!':0}
bigrams = ['dh','gj','ll','nj','rr', 'sh', 'th', 'xh', 'zh']
vowels = ['a','e','ë','i','o', 'u', 'y']


for i in letters:
    if (i in inputFile):
        for j in bigrams:
            if (i == j):
                letters[i[0]] = letters[i[0]] - inputFile.count(i);
                letters[i[1]] = letters[i[1]] - inputFile.count(i);
                break
        letters[i] = inputFile.count(i)

# vowels_dict = {i:j for i, j in zip(vowels, [letters[i] for i in vowels])}
#print("Vowels: ")
# vowels_dict = {}
# for i in vowels:
#         print(str(i) + " -> "+str(letters[i]))
#         vowels_dict[i] = letters[i]
# plt.bar( vowels_dict.keys(),vowels_dict.values(),color='#117892')
# plt.title("Frekuenca e paraqitjes se zanoreve")
# plt.ylabel("numri i paraqitjeve")
# plt.xlabel("zanoret")
# plt.show()


# Bigrams_dict = {}
# print("\nBigrams: ")
# for i in bigrams:
#     print(str(i) + " -> " + str(letters[i]))
#     Bigrams_dict[i] = letters[i]
# plt.bar(Bigrams_dict.keys(), Bigrams_dict.values(), color='#117892')
# plt.title("Frekuenca e paraqitjes se Bigrameve")
# plt.ylabel("numri i paraqitjeve")
# plt.xlabel("Bigramet")
# plt.show()

print("\nPerseritja e shronjave tjera:")
print(letters)
for i in letters:
    print(str(i) +' -> '+ str(letters[i]))
SortLetters= Counter(letters)
topfive=SortLetters.most_common(10)
SortedLetters = dict(topfive)
print(SortedLetters)

plt.bar(SortedLetters.keys(), SortedLetters.values())
plt.title("Top 10 Letters")
plt.ylabel("Frequency")
plt.xlabel("Letters")
plt.show()

# MostUsedWords = Counter(Words)
# MostCommon=MostUsedWords.most_common(10)
# MostUsed=dict(MostCommon)
# for i in MostCommon:
#     print(i)
# plt.bar(MostUsed.keys(),MostUsed.values())
# plt.title("TOP 5 MOST USED WORDS IN TOTAL")
# plt.ylabel("WORDS FREQUENCY")
# plt.xlabel("WORDS")
# plt.show()
# print('============')
# NumberOfWords = len(Words)
# NumberOfCharacters = len(inputFile)
# NumberOfSentences = len(Sentences)
# print("Number of words " + str(NumberOfWords))
# print("Number of characters " + str(NumberOfCharacters))
# print("Number of sentences " + str(NumberOfSentences))
# print('============')
print("5 most used words with length more than 2")
# Words1=[]
# for i in Words:
#     if len(i) < 3:
#         continue
#     Words1.append(i)
# WordsCounter=Counter(Words1)
# topten=WordsCounter.most_common(10)
# topLength = dict(topten)
# for i in topten:
#     print(i)
# plt.bar(topLength.keys(),topLength.values())
# plt.title("TOP 10 MOST USED WORDS WITH LENGTH MORE THAN TWO")
# plt.ylabel("WORDS FREQUENCY")
# plt.xlabel("WORDS")
# plt.show()
# print('============')
#
# Words2 = []
# for i in Words:
#     if len(i) > 1 or i == '-' or i == '”' or i == '}' or i == ')':
#         continue
#     Words2.append(i)
# WordsCounterLetters = Counter(Words2)
# top4 = WordsCounterLetters.most_common(4)
# top4letters = dict(top4)
# print(top4letters.keys(),top4letters.values())
#
# # for i in top4:
# #     print(i)
# plt.bar(top4letters.keys(),top4letters.values())
# plt.title("TOP 4 MOST USED Letters")
# plt.ylabel("WORDS FREQUENCY")
# plt.xlabel("Letters")
# plt.show()














