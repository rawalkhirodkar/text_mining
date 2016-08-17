
import csv
sent_dict={}
relation_dict={}
country_dict={}
relation_keywords_dict={}

def read_sentences():
	#changes made to selected_indiactors, please add "no_unit" to the file at the end of population and internet users relation separated by tab
	with open('sentences.tsv','r') as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		count = 0
		for row in tsvin:
			count += 1
			key = row[0].strip()
			sent_dict[key]=[]
			sent_dict[key].append(row[1])
			sent_dict[key].append(row[2])
			sent_dict[key].append(row[3])
			
	with open('selected_indicators','r') as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		count = 0
		for row in tsvin:
			count += 1
			key = row[2].strip()
			#print(count,key)
			relation_dict[key]=[]
			relation_dict[key].append(row[0])
			relation_dict[key].append(row[1])
			relation_dict[key].append(row[3])
	
	#print(relation_dict["EG.ELC.PROD.KH"])

def read_knowledge_base():
	with open('kb-facts-train_SI.tsv','r') as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		count = 0
		for row in tsvin:
			count += 1
			key = row[0].strip() +"#"+ row[2].strip()
			#print(key)
			try:
				country_dict[key].append(row[1])
			except :
				country_dict[key]=[]
				country_dict[key].append(row[1])
			
			#print(country_dict[key])	

def keywords_relation():
	with open('keywords_relation.csv','r') as csvin:
		csvin = csv.reader(csvin)
		for row in csvin:
			key = row[1].strip()
			relation_keywords_dict[key] = []
			s = row[2]
			#print(s)
			while (len(s) > 0):
				#print("s",s)
				i = s.find(",")
				if(i == -1):
					s1 = s
					s = ""
				else:	
					s1 = s[0:i]
				#print("s1",s1)
				s = s[i+1:len(s)]
				relation_keywords_dict[key].append(s1)
		#print(row[1])
	#print(relation_keywords_dict["EN.ATM.CO2E.KT"])	

read_sentences()		
read_knowledge_base()
keywords_relation()

def find_which_relation():
	for x in sent_dict:
		l = sent_dict[x]
		sent = l[0]
		#print("")
		#print(x,sent)
		#print(sent.find("billion"))
		countlist = []
		frequency = 0
		relation = []
		for y in relation_keywords_dict:
			#print("#####################################")
			list1 = relation_keywords_dict[y]
			count = 0

			for i in list1:
				#print(sent)
				i = i .strip()
				#print("i",i[len(i)-1])
				score = int(i[len(i)-1])
				i = i[0:len(i)-1]
				sent1 = sent
				while (sent1.find(i) != -1):
					#print("Found:********",i,":",score)
					count = count + score
					#print(sent1)
					sent1 = sent1[sent1.find(i)+1:len(sent1)]
				#print(count)	
			#countlist.append(count)
			if(count > frequency):
				relation = []
				l = []
				l.append(y)
				l.append(count)
				frequency = count	
				relation.append(l)
			elif(count == frequency):	
				l = []
				l.append(y)
				l.append(count)
				frequency = count	
				relation.append(l)

		# if(relation != [] and relation[0][1]!=0):
		# 	count = 0
		# 	for i in relation:
		# 		key = i[0]			
		# 		print("TALKING:",relation_dict[i[0]][0],i[1])
		# 		count = count + 1
		# else:
		# 	print("TALKING:none")	
		# print("")
		
		#print(countlist)
	#pls read this, relation is list of list,and its list element has the code of relation it is talking about at index 0

find_which_relation()

