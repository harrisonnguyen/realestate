import csv
import re

file = open('realestate_data.csv','r')
reader = csv.DictReader(file)
vocab = set()
for row in reader:
	description = row['descript'].split()
	for words in description:
		word = words.split('.')
		for x in word:
			y = x.split(',')
			for q in y:
				k = q.split('/')
				for z in k:
					z = re.sub("[()!1234567890&*-,.:;_-]",'',z)
					z = re.sub("[^\x00-\x7F]+",'',z)
					z = re.sub("[']+",'',z)
					z = z.lower()
					if not z or len(z)==1:
						pass
					else:
						#if z not in vocab:
						print z
						vocab.add(z)
						#print vocab
file.close()
file = open('realestate_vocab.txt','w')
while vocab:
	word = vocab.pop()
	print word
	file.write(word+'\n')
file.close()
