str = 'Hydroblocks components and antiblocking systems (ABS)'
str1 = 'Hydroblocks components and antiblocking systems (ABS)'

string = str.replace(u'\xa0', u' ')
print(str1 == string)

print(set(str1) ^ set(string))

