alphabet='a b c d e f g h i j k l m n o p q r s t u v w x y z'
alphabet2='x y z a b c d e f g h i j k l m n o p q r s t u v w'
dictionary=dict(zip(alphabet,alphabet2))
dictionary

word=input('enter a word')
word=[ch for ch in word]
#
new_word=[]
for i in range(0,len(word)):
	new_word.append(dictionary[word[i]])
print(new_word)
#

alphabet3='x y z a b c d e f g h i j k l m n o p q r s t u v w'
alphabet4='a b c d e f g h i j k l m n o p q r s t u v w x y z'
dict2=dict(zip(alphabet3,alphabet4))
back_word=[]

for i in range(0, len(new_word)):
	back_word.append(dict2[new_word[i]])
print(back_word)
