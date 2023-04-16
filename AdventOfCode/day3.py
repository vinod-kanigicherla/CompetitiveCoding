import sys
import string
temp = [line.strip() for line in sys.stdin]
lower_dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
higher_dict = dict()

letters_dict = dict()
for letter in lower_dict:
    lower_dict[letter] = int(lower_dict[letter])
for letter in lower_dict:
    higher_dict[letter.upper()] = lower_dict[letter] + 26

score = 0
for i in range(0, len(temp), 3):
    first,second,third = temp[i],temp[i+1],temp[i+2]
    for l in set(first).intersection(set(second)).intersection(set(third)):
        if l.isupper():
            score += higher_dict[l]
        else:
            score += lower_dict[l]

print(score)
