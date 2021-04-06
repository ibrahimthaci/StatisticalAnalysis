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
#     print(i, end='') this blcok of code if we want to display words but not e i words with 1-2 letters

Words = inputFile.replace('.',' ').replace(',',' ').replace('!','').replace('?',' ').replace('\'',' ').replace('"',' ').replace(':',' ').replace(';',' ').split()
Sentences = inputFile.replace('?','.').replace('!','.').split('.')
print("Most Used words on total")
MostUsedWords = Counter(Words)
MostCommon=MostUsedWords.most_common(5)
MostUsed=dict(MostCommon)
for i in MostCommon:
    print(i)
plt.bar(MostUsed.keys(),MostUsed.values())
plt.title("TOP 5 MOST USED WORDS IN TOTAL")
plt.ylabel("WORDS FREQUENCY")
plt.xlabel("WORDS")
plt.show()
print('============')
NumberOfWords = len(Words)
NumberOfCharacters = len(inputFile)
NumberOfSentences = len(Sentences)
print("Number of words " + str(NumberOfWords))
print("Number of characters " + str(NumberOfCharacters))
print("Number of sentences " + str(NumberOfSentences))
print('============')
print("5 most used words with length more than 2")
Words1=[]
for i in Words:
    if len(i) < 3:
        continue
    Words1.append(i)
WordsCounter=Counter(Words1)
topten=WordsCounter.most_common(10)
topLength = dict(topten)
for i in topten:
    print(i)
plt.bar(topLength.keys(),topLength.values())
plt.title("TOP 10 MOST USED WORDS")
plt.ylabel("WORDS FREQUENCY")
plt.xlabel("WORDS")
plt.show()
print('============')

Words2 = []
for i in Words:
    if len(i) > 1 or i == '-' or i == '”' or i == '}' or i == ')':
        continue
    Words2.append(i)
WordsCounterLetters = Counter(Words2)
top4 = WordsCounterLetters.most_common(4)
top4letters = dict(top4)
print(top4letters.keys(),top4letters.values())

# for i in top4:
#     print(i)
plt.bar(top4letters.keys(),top4letters.values())
plt.title("TOP 4 MOST USED Letters")
plt.ylabel("WORDS FREQUENCY")
plt.xlabel("Letters")
plt.show()


# me kriju ni varg ne ri si ma nalt te zbrazet
# ni loop me kusht nese osht a e i o u per zanore qe mi marr mi bo apend
#e masanej ne couter
#
#
WordsLetters = inputFile.split()
print(WordsLetters)










