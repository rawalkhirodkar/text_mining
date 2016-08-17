import csv
list1=[]
with open('selected_indicators','rb') as tsvin:
	tsvin = csv.reader(tsvin, delimiter='\t')

	for row in tsvin:
		list1.append(row)