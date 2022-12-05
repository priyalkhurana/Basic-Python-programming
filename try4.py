str="mary elizabeth smith"
leng=str.split()
str1=" "
for i in range (len(leng)-1):
    str=leng[i]
    str1=str1+(str[0].upper()+'.')
str1=str1+leng[-1].title()
print(str1)