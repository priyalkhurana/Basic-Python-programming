
with open("file1.txt",'r+') as f1:
	words = f1.read().split()
	maxi_leng_word = max(words,key=len)
	maxleng = len(max(words,key=len))		
	print('maximum length word in the file is :',maxi_leng_word)

#Write a program to find a largest word in a file

