import re
#import csv

with open('profanity_words.csv','r+') as file:
    s = '|'.join(file.readline().split(','))

profanity = re.compile(r"\b(?:{})\b".format(s),flags=re.I)

with open('fb_data.txt','r+') as sample:
    print('{0:>9} , {1:9}'.format('Comment No','Profanity %'))
    for num,line in enumerate(sample,start=1):
        temp = line.split()
        count = len(temp)
        line = ' '.join(temp)
        print("{0:>10} , {1:.2f}%".format(num,len(profanity.findall(line))*100/count))