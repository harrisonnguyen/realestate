import csv
import numpy
import re
import inflect
import en

p = inflect.engine()
f = open('realestate_vocab.txt')
vocab = f.read().split()
file = open('realestate_data.csv','r')
output = open('realestate_dtm.ldac','w')
reader = csv.DictReader(file)

#N = 10

#matrix = numpy.zeros((1,len(vocab)),dtype=int)
i = 0
for house in reader:
#house = reader.next()
	#matrix = numpy.zeros((1,len(vocab)),dtype=int)
	matrix = {}
	print "House numer %d" %i
	#if i == N:
	#	break
	description = house['descript'].split()
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
							index = vocab.index(z)
							#print index
							#matrix[0,index] += 1
							if index in matrix:
								matrix[index]+=1
							else:
								matrix[index] = 1
	#row = '%d' %numpy.sum(matrix, axis=1)
	#for k in range(0,len(vocab)):
	#	if matrix[0,k] != 0:
	#		row += ' %d:%d' %(k, matrix[0,k])
	#row += '\n'
	values = matrix.items()
	#word_count = 0
	row = ''
	temp = ''
	for items in values:
		#print items
		#word_count += items[1]
		temp += ' %d:%d' %(items[0],items[1])
	temp += '\n'
	row = '%d' %len(matrix)
	output.write(row+temp)
	i+=1
output.close()

#numpy.save('realestate_dtm',matrix)
