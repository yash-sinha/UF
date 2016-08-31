import re, string
inputfile = open("script.txt")
script=inputfile.read()
script = re.sub("\[[^]]*\]", "",script)
# print script
count1 = script.count("LADY TORMINSTER:")
count2 = script.count("SIR GEOFFREY:")
#script = script.translate(None, string.punctuation)
person1=""
person2=""
script = script.split('\n')

for word in script:
	if "LADY TORMINSTER:" in word:
		person1=person1+word
	
	if "SIR GEOFFREY:" in word:
		person2=person2+word

# print person1
person1 = re.sub("LADY TORMINSTER:", "",person1)
person2 = re.sub("SIR GEOFFREY:", "",person2)
person1 = re.sub("--", ' ',person1)
person2 = re.sub("--", ' ',person2)

person1=person1.translate(None, string.punctuation)
person2=person2.translate(None, string.punctuation)

print "Person1 makes "+str(count1)+ " dialogue turns"
print "Person2 makes "+str(count2)+ " dialogue turns"
print "Person1 says "+str(len(person1.split()))+" words"
print "Person2 says "+str(len(person2.split()))+" words"
print "Person1 says "+str(round(len(person1.split())/float(count1),2))+" words on an average per turn"
print "Person2 says "+str(round(len(person2.split())/float(count2),2))+" words on an average per turn"
print "Average length of words spoken by Person1 is: "+str(round(len(re.sub(' ', '', person1))/float(len(person1.split())),2))
print "Average length of words spoken by Person2 is: "+str(round(len(re.sub(' ', '', person2))/float(len(person2.split())),2))







