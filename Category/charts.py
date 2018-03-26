import matplotlib.pyplot as plt
from matplotlib import interactive
from os import listdir
import pandas as pd
from os.path import isfile, join
import numpy as np
import os

def file_to_dataframe(f, f1):
	#removing .png
	j = f1.index('.')
	save = f1[:j]

	#reading excelfile
	xl = pd.ExcelFile(f)
	df = xl.parse('default')
	df = xl.parse('default')
	X = list(df['concat'])
	Y = list(map(int, df['count']))
	fig = plt.figure(figsize=(20,10))
	width = .35
	ind = np.arange(len(Y))
	plt.bar(ind, Y, width = width)
	plt.xticks(ind + width/2, X)
	fig.autofmt_xdate()
	plt.title(save)
	
	fpath = os.path.join("D:\Project\Knime\Category\\bar_charts\\", save+'.png')
	#print ("fpath is", fpath)
	plt.savefig(fpath, dpi=fig.dpi)

if not os.path.exists('bar_charts'):
    os.makedirs('bar_charts')

for f in listdir("D:\Project\Knime\Category\Category\\"):
	print(f)
	file_to_dataframe(join("D:\Project\Knime\Category\Category\\", f), f)


