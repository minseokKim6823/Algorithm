import sys
input=sys.stdin.readline
_dict1={}
_dict2={}
A,B=map(int,input().split())
k=0
for i in range(A):
    T=input()
    word=T.replace("\n", "")
    k+=1
    _dict1[word]=k
    _dict2[k]=word
for i in range(B):
    word=str(input())
    word = word.replace("\n", "")
    if word.isdecimal():
        print(_dict2[int(word)])
    else:
        print(_dict1[word])

'''
25
Raichu
3
Pidgey
Kakuna
'''

'''
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu

25
Raichu
3
Pidgey
Kakuna
'''