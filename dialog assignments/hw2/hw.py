import re, string, nltk, subprocess, math
from collections import Counter
inputfile = open("script.txt")
script=inputfile.read()
script = re.sub("\[[^]]*\]", "",script)
script=script.lower()
text=script.split('\n')

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

print "Speaker 1 identifier is -> "+ sp1_identifier
print "Speaker 2 identifier is -> "+ sp2_identifier

count1 = script.count(sp1_identifier)
count2 = script.count(sp2_identifier)
script = re.sub("--", ' ',script)

person1=""
person2=""
script = script.split('\n')
count_sp1=count_sp2=0

utterance_seq=""
number_words_utterance_p1=[]
number_words_utterance_p2=[]

number_words_utterance_p1_int=[]
number_words_utterance_p2_int=[]

for word in script:
	if sp1_identifier in word:
		utterance_seq= "1 "+utterance_seq
		count_sp1=count_sp1+1
		person1=person1+word
		tempWord=len((re.sub(sp1_identifier, "",word)).split())
		number_words_utterance_p1.append(str(tempWord))
		number_words_utterance_p1_int.append(tempWord)

	
	if sp2_identifier in word:
		utterance_seq= "2 "+utterance_seq
		count_sp2=count_sp2+1
		person2=person2+word
		tempWord=len((re.sub(sp2_identifier, "",word)).split())
		number_words_utterance_p2.append(str(tempWord))
		number_words_utterance_p2_int.append(tempWord)

# print person1
person1 = re.sub(sp1_identifier, "",person1)
person2 = re.sub(sp2_identifier, "",person2)

person1=person1.translate(None, string.punctuation)
person2=person2.translate(None, string.punctuation)

w_person1=person1.split()
w_person2=person2.split()

w_person1_counts = Counter(w_person1) #counts the number each time a word appears
w_person2_counts = Counter(w_person2) #counts the number each time a word appears


common_person1= [ite for ite, it in w_person1_counts.most_common(1)]
common_person2= [ite for ite, it in w_person2_counts.most_common(1)]

total_corpus=person1+' '+ person2
w_total=total_corpus.split()
# w_total=re.findall(r'\w+', total_corpus)
w_total_counts = Counter(w_total)
common_total= [ite for ite, it in Counter(w_total_counts).most_common(1)]

bigram_corpus=nltk.bigrams(w_total)
bigram_corpus_dist = nltk.FreqDist(bigram_corpus)
common_bigrams_corpus = bigram_corpus_dist.most_common(1)

trigram_corpus=nltk.trigrams(w_total)
trigram_corpus_dist = nltk.FreqDist(trigram_corpus)
common_trigrams_corpus = trigram_corpus_dist.most_common(1)

w_seq=utterance_seq.split()
w_seq_sp1_sp2=list(nltk.bigrams(w_seq))
bigram_sp1_sp2_dist = nltk.FreqDist(w_seq_sp1_sp2)
count_sp1_sp2=0
for k,v in bigram_sp1_sp2_dist.items():
	 if k == ('1','2'):
		count_sp1_sp2=v

command = 'Rscript'
path2script = 'median.R'
cmd_median_person1 = [command, path2script] + number_words_utterance_p1
median_person1 = subprocess.check_output(cmd_median_person1, universal_newlines=True)
cmd_median_person2 = [command, path2script] + number_words_utterance_p2
median_person2 = subprocess.check_output(cmd_median_person2, universal_newlines=True)

path2script = 'mode.R'
cmd_mode_person1 = [command, path2script] + number_words_utterance_p1
mode_person1 = subprocess.check_output(cmd_mode_person1, universal_newlines=True)
cmd_mode_person2 = [command, path2script] + number_words_utterance_p2
mode_person2 = subprocess.check_output(cmd_mode_person2, universal_newlines=True)

path2script = 'sd.R'
cmd_sd_person1 = [command, path2script] + number_words_utterance_p1
sd_person1 = subprocess.check_output(cmd_sd_person1, universal_newlines=True)
cmd_sd_person2 = [command, path2script] + number_words_utterance_p2
sd_person2 = subprocess.check_output(cmd_sd_person2, universal_newlines=True)

print "Most common word in Person 1's corpus "+str(common_person1)
print "Most common word in Person 2's corpus "+str(common_person2)
print "Most common word in corpus "+str(common_total)
print "Most common bigram in corpus "+str(common_bigrams_corpus)
print "Most common trigram in corpus "+str(common_trigrams_corpus)
print "Count of utterances of speaker 1 is "+str(count_sp1)
print "Count of utterances spoken by sp2 after utterance of sp1 "+ str(count_sp1_sp2)
print "Probability that Speaker 2 will speak after Speaker 1 is "+str(float(count_sp1_sp2)/float(count_sp1))
print "Median of words spoken by Speaker 1 is "+str(median_person1)
print "Median of words spoken by Speaker 2 is "+str(median_person2)
print "Mode of words spoken by Speaker 1 is "+str(mode_person1)
print "Mode of words spoken by Speaker 2 is "+str(mode_person2)
print "Standard deviation of number of utterances of Speaker 1 from R is "+ str(sd_person1)
print "Standard deviation of number of utterances of Speaker 1 after correction of sqrt((N-1)/N): "+ str(float(sd_person1)*math.sqrt(float(len(number_words_utterance_p1)-1)/len(number_words_utterance_p1)))
print "Standard deviation of number of utterances of Speaker 2 from R is "+ str(sd_person2)
print "Standard deviation of number of utterances of Speaker 2 after correction of sqrt((N-1)/N): "+ str(float(sd_person2)*math.sqrt(float(len(number_words_utterance_p2)-1)/len(number_words_utterance_p2)))

# path2script = 'count.R'
# cmd_mode_person1 = [command, path2script] + number_words_utterance_p1
# mode_person1 = subprocess.check_output(cmd_mode_person1, number_words_utterance_p2, universal_newlines=True)

file_p1=open('./file_p1', 'w+')
file_p1.write(str(number_words_utterance_p1_int))
file_p2=open('./file_p2', 'w+')
file_p2.write(str(number_words_utterance_p2_int))
file_p2.close()
file_p2.close()

print "Histogram to be created from values provided in file_p1 for Speaker 1 and file_p2 for Speaker 2"







