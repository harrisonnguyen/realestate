import csv
import numpy
import re
f = open('vocab_test.txt')
vocab = f.read().split()
file = open('realestate_data.csv','r')
reader = csv.DictReader(file)

matrix = numpy.zeros((1,len(vocab)),dtype=int)

house = reader.next()
description = house['descript'].split()
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
					index = vocab.index(z)
					matrix[0,index] += 1
print matrix
						#print vocab