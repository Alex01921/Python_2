import os
fhand = open('1.txt', 'r')
# fhand = open('C:\\Users\\hp india\\Desktop\\newsample.txt', 'r')
content = fhand.read()
content = content.split('\n')
content.sort()
fhand = open('write11.txt', 'w')
# fhand = open('C:\\Users\\hp india\\Desktop\\newsamplewrite.txt', 'w')
for word in content:
    fhand.write(word + '\n')
fhand.close()
# 1.txt
