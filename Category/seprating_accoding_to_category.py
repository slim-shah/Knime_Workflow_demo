import pandas as pd
from operator import itemgetter
from pandas import ExcelWriter
import openpyxl
import re


def List_to_dataframe(v):
	df = pd.DataFrame(v,columns=['concat', 'count', 'month', 'mon_val'])
	df.drop('month', axis=1, inplace = True)
	df.drop('mon_val', axis=1, inplace = True)
	return df
def Dataframe_to_file(k, df):
	k = re.sub('[^A-Za-z0-9]+', ' ', k)
	df.columns = ['concat', 'count']
	writer = ExcelWriter(str(k) + '.xlsx')
	df.to_excel(writer,'default', index=False)
	writer.save()

xl = pd.ExcelFile("Rest1.xlsx")
#print(xl.sheet_names)
df = xl.parse('default')
df.drop('Unnamed: 5', axis=1, inplace=True)
df.columns = ['concat', 'count', 'category', 'month', 'year']
df.drop('year', axis=1, inplace = True)
#print(df.head())
Dict ={}
Mapping ={'January':1, 'February':2, 'March':3, 'April':4,'May':5, 'June':6, 'July':7,'August':8, 'September':9,'October':10, 'November':11, 'December':12}
i=0
for index,row in df.iterrows():
	Temp = list()
	#print(str(row[0]) + " " + str(row[1])+ " " + str(row[2]) +  " " + str(row [3]) )
	#print(row[0])
	k = list((row[0]).split(','))
	#print(k[-2]+","+k[-1])
	Temp.append(k[-2]+","+k[-1])
	Temp.append(row[1])
	Temp.append(row[3])
	try:
		Temp.append(Mapping[k[-2]])
	except:
		print(row)
		exit(0)
	if row[2] in Dict:
		Dict[row[2]].append(Temp)
	else:
		Dict[row[2]] = []
		Dict[row[2]].append(Temp)

for k,v in Dict.items():
	print(k)
	v.sort(key=itemgetter(3))
	df1 = List_to_dataframe(v)
	Dataframe_to_file(k, df1)

	



	