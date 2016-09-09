import re, string
inputfile = open("script.txt")
script=inputfile.read()
# We are removing special effects like [laugh],etc in square brackets using regex before analysing script.
text = script.split('\n')
utt=0
for item in text:
	if len(item) is not 0:
		utt=utt+1
		sp1_identifier=''.join(item)
		position = sp1_identifier.index(':')
		sp1_identifier=sp1_identifier[:position+1]
		break
newUtt=0
for item in text:
	if len(item) is not 0:
		newUtt=newUtt+1
		if newUtt is not utt:
			utt=utt+1
			sp2_identifier=''.join(item)
			position = sp2_identifier.index(':')
			sp2_identifier=sp2_identifier[:position+1]
			break
		
script = re.sub("\[[^]]*\]", "",script)
count1 = script.count("sp1_identifier")
count2 = script.count("sp2_identifier")
utterances = script.splitlines()
speaker1=""
speaker2=""
for uttr in utterances:
	if sp1_identifier in uttr:
		speaker1=speaker1+uttr
	if sp2_identifier in uttr:
		speaker2=speaker2+uttr
		
# We are separating the utterance spoken by speaker 1 and 2 using variable utterance1 and utterance2
# we have taken word as "you" and counters of utterances containing or not containing word for 1 and 2 are taken respectively. 

utterance1 = speaker1.split(sp1_identifier)
countContainingWord1 = 0
countNotContainingWord1 = 0
for utterance in utterance1:
	if " you " in utterance:
		countContainingWord1 = countContainingWord1 + 1
		
	if " you " not in utterance and "" != utterance:
		countNotContainingWord1 = countNotContainingWord1 + 1
		

utterance2 = speaker2.split(sp2_identifier)
countNotContainingWord2 = 0
countContainingWord2 = 0
for utterance in utterance2:
	if " you " not in utterance and "" != utterance:
		countNotContainingWord2 = countNotContainingWord2 + 1
		
	if " you " in utterance and "" != utterance:
		countContainingWord2 = countContainingWord2 + 1
    

# Based on the counts generated above and contegency table

print "number of utterances of speaker1 "+str(count1)
print "number of utterances of speaker2 "+str(count2)
print "number of utterances of speaker1 having word you "+str(countContainingWord1)
print "number of utterances of speaker2 having word you "+str(countContainingWord2)
print "number of utterances of speaker1 not having word you "+str(countNotContainingWord1)
print "number of utterances of speaker2 not having word you "+str(countNotContainingWord2)
print "P(u is from Speaker 1) is "+ str(round(float(count1)/float(count1+count2),2))
print "P(u is from Speaker 2) is "+ str(round(float(count2)/float(count1+count2),2))
print "P(u contains "" you "" | u is from Speaker 1)" + str(float(countContainingWord1)/float(count1))
print "P(u contains "" you "" | u is from Speaker 2)" + str(float(countContainingWord2)/float(count2))
print "P(u being from Speaker 1 | u contains "" you "")" + str(float(countContainingWord1)/float(countContainingWord1+countContainingWord2))
print "P(u being from Speaker 1 | u does not contain "" you "")" + str(float(countNotContainingWord1)/float(countNotContainingWord1+countNotContainingWord2))
print "P(u being from Speaker 2 | u contains "" you "")" + str(float(countContainingWord2)/float(countContainingWord1+countContainingWord2))

		
