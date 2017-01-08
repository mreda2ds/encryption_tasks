from collections import deque

h0 = 0b01100111010001010010001100000001
h1 = 0b11101111110011011010101110001001
h2 = 0b10011000101110101101110011111110
h3 = 0b00010000001100100101010001110110
h4 = 0b11000011110100101110000111110000

#list to store words
words = []

#Function to Convert Word to Binary------------------------------------
def wordTobin(word):
    return ''.join(format(ord(c), '08b') for c in word)
# End of Converting Word to binary-------------------------------------

# Function to divide the word------------------------------------------
def divdeword(word, length):
    dividedwords = []
    for i in range(0, len(word), length):
        dividedwords.append(word[0 + i:length + i])
    return dividedwords
#End of dividing words-------------------------------------------------

#rotating the words----------------------------------------------------
def rotateword(word,shift):
    wordrotated = deque(word)
    wordrotated.rotate(shift)
    wordrotated = ''.join(wordrotated)
    return wordrotated
# End of rotating word-------------------------------------------------

#Start of the App------------------------------------------------------
word = input()
wordInbinary = wordTobin(word)
print('Word in Binary ', wordInbinary)
wordSize = len(wordInbinary)
wordSizeInbinary = bin(wordSize)[2:].zfill(64)

#Adding on to the right of the word-----------------------------------
wordInbinary += '1'
print('1 Added ', wordInbinary)

# Appending the zeros-------------------------------------------------
print('Length of word ', len(wordInbinary))
counter = 0
while len(wordInbinary) < (448 % 512):
    wordInbinary += '0'
    counter += 1
print(wordInbinary)
#End of adding Zeros--------------------------------------------------

print('counter of Zeros ', counter)
print('length of word before adding size', len(wordInbinary))
print("word size in binary ", wordSizeInbinary)

#Adding the word size-------------------------------------------------
wordInbinary += str(wordSizeInbinary)
print('word after adding size',wordInbinary)
print('final length of word ', len(wordInbinary))

#divide word into 32 words--------------------------------------------
words = divdeword(wordInbinary, 32)

#printing words-------------------------------------------------------
for x in range(0, len(words), 1):
    print('word ' + str(x) + ' ' + words[x] + '\n')
#End of dividing and printing the first 16 word-----------------------

#XOR Long string
def myxor(wrdx,wrdy,wrdk,wrdm):
    return ''.join(str(ord(x)^ord(y)^ord(k)^ord(m)) for x, y, k, m in zip(wrdx, wrdy, wrdk, wrdm))

#Creating 80 word
for i in range(16,80):
    #print(wordTobin(words[i-3]) ^ wordTobin(words[i-8]))
    words.append(rotateword(myxor(words[i-3],words[i-8],words[i-14],words[i-16]), -1))
    #words[i] = rotateword((bin(words[i-3]) ^ bin(words[i-8]) ^ bin(words[i-14]) ^ bin(words[i-16])), -1)
    print("word " + str(i) +': '+ words[i])
input()
#Function 1


#Function 2


#Function 3


#Function 4


#End of App
