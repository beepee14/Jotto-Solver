import os.path
from itertools import product
def scoreCal(word,guess):
	temp_c=0
	temp_b=0
	randomList1=[]
	randomList2=[]
	for i in range(len(word)):
		if word[i]==guess[i]:
			temp_b=temp_b+1
		else:
			randomList1.append(guess[i])
			randomList2.append(word[i])
	randomString1="".join(randomList1)
	randomString2="".join(randomList2)
	for i in range(len(randomString1)):
		if randomString2.find(randomString1[i])!=-1:
			temp_c=temp_c+1
	return temp_b,temp_c

if os.path.isfile('dic.txt'):
	f=open('dic.txt','r')
	dictionary=[temp for temp in f.readline().split()]
	a,b=map(int, raw_input().split())
	guess=dictionary[0]
	dictionary=dictionary[1:]
	temp=[]
	for word in dictionary:
		temp_b,temp_c=scoreCal(word,guess)
		if temp_c==a and temp_b==b:
			temp.append(word)
	dictionary=temp
	n=len(dictionary[0])
	if len(dictionary)<=1000:
		scoreSet=[temp for temp in range(n+1)]
		p=product(scoreSet,repeat=2)
		maxi=0
		guess2=0
		for guessedWord in dictionary:
			mapValue={scoreTuple:0 for scoreTuple in p}
			for word in dictionary:
				temp_b,temp_c=scoreCal(word,guessedWord)
				for scoreTuple in p:
					if scoreTuple[0]==temp_b and scoreTuple[1]==temp_c:
						mapValue[scoreTuple]=1+mapValue[scoreTuple];
			mini=100000
			for scoreTuple in p:
				if mapValue[scoreTuple]<mini:
					mini=mapValue[scoreTuple]
			if mini>=maxi:
				maxi=mini
				guess2=guessedWord
		for i in range(len(dictionary)):
			if dictionary[i]==guess2:
				tempVal=dictionary[0]
				dictionary[0]=guess2
				dictionary[i]=tempVal
	f=open('dic.txt','w')
	for i in range(len(dictionary)):
		f.write(dictionary[i]+" ")
	print(dictionary[0])
else:
	fo=open('dictionary.txt','r')
	dictionary=[temp for temp in f.readline().split()]
	n,t= map(int,raw_input().split())
	modified=[]
	for temp in dictionary:
		if len(temp)==n:
			modified.append(temp)
	f=open('dic.txt','w')
	for i in range(len(modified)):
		f.write(modified[i]+" ")
	print(modified[0])


