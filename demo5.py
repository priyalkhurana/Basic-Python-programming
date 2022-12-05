with open('rhyme.txt','r') as f1:
    s={}
    data=f1.read()
    st=data.lower()
    line=st.split()
    for i in line:
        s[i]=line.count(i)

with open('words.txt','w+') as f2:
    for i in s:
        f2.write(i.capitalize()+'\t'+str(s[i])+'\n') 
with open('words.txt','r') as f2:
    print(f2.read())


    