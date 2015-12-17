import csv
import re
import inflect
import en
p = inflect.engine()

file = open('realestate_data.csv','r')
reader = csv.DictReader(file)
vocab = set()
i = 0
for row in reader:
	print "House number %d" %i
	description = row['descript'].split()
	for words in description:
		word = words.split('.')
		for x in word:
			y = x.split(',')
			for q in y:
				j = q.split('/')
				for o in j:
					k = o.split('-')
					for z in k:
						z = re.sub("[$()!1234567890&?*,.:;_]",'',z)
						z = re.sub("[^\x00-\x7F]+",'',z)
						z = re.sub("[']+",'',z)
						z = re.sub('[\"><`~[]=]+','',z)
						z = re.sub('["|{}]+','',z)
						z = re.sub('\+','',z)
						z = re.sub('~','',z)
						z = re.sub('<','',z)
						z = re.sub('>','',z)
						z = re.sub('#','',z)
						#z = re.sub("\\",'',z)
						z = re.sub('\]','',z)
						z = re.sub('\[','',z)
						z = re.sub('=','',z)
						z = re.sub('`','',z)
						z = re.sub('%','',z)
						z = z.lower()
						if not z or len(z)==1 or '@' in z:
							pass
						else:
							#print z
							#if z not in vocab:
							try:
								z = p.plural_verb(z)
							except IndexError:
								print "Dodgy string %s" %z
								continue
							try:
								z = en.verb.present(z)
							except KeyError:
								pass
							vocab.add(z)
							#print vocab
	i+=1
file.close()
file = open('realestate_vocab.txt','w')
while vocab:
	word = vocab.pop()
	print word
	file.write(word+'\n')
file.close()
