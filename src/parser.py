import pandas as pd 
import hashlib
import os
import numpy as np 
import matplotlib.pyplot as plt; plt.rcdefaults()
	
import matplotlib.pyplot as plt
from itertools import cycle
	
#from utils import logger
def file_as_bytes(file):
    with file:
        return file.read()


def plotgraph(labels1,unq1):
	k = 0 
	
	data_distri=np.zeros(len(unq1))
	for i in range(0,len(unq1)):
		for j in range(0,len(labels1)):
			if labels1[j] == unq1[i] :
				k=k+1
		data_distri[i]=k
		k = 0		
	np.save("data_distri",data_distri)	
	print(str(len(data_distri)))

	cycol = cycle('bgrcmk')
 
	#objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
	y_pos = np.arange(len(unq1))
	#performance = [10,8,6,4,2,1]
	 
	barlist=plt.bar( y_pos,data_distri, align='center', alpha=0.9)
	plt.xticks(y_pos,unq1,rotation='vertical',fontsize='8')
	plt.ylabel('Number of Sanmples')
	plt.title('Site of Origin')
	plt.title("Label vs Number of Samples of that label")
	for i in range(0,len(unq1)):
		barlist[i].set_color(next(cycol)) 
	plt.show()

	return data_distri







def extractdata(inputfile,data_directory):
	df = pd.read_csv(inputfile, sep="\t")
	files=df['file_id'].values.tolist()
	filenames=df['file_name'].values.tolist()
	data=[]
	z=0
	#----------------------------------------------------------

	file_path=data_directory+str(files[0])+"/"+str(filenames[0])
	f = open(file_path, 'r')
	x = f.readlines()
	f.close()
	feature_labels=[]
	for i in range(1,len(x)):
		read_count = x[i].split("\t")
		feature_labels.append(read_count[0])
	np.save("feature_labels",np.asarray(feature_labels))
	feature_labels=[]
	#-----------------------------------------------------------
	p=0
	for k in range(0,10):
		for j in range(0,1000):
			file_path=data_directory+str(files[(z+j)])+"/"+str(filenames[(z+j)])
			f = open(file_path, 'r')
			x = f.readlines()
			f.close()
			#print(len(x))
			feature=[]
			for i in range(1,len(x)):
				read_count = x[i].split("\t")
				#print(read_count[1])
				feature.append(read_count[1])
			data.append(feature)
		z=z+1000
		p=p+1
		print("batch->"+str(p))		
		print(np.shape(data))
		np.save("batch_"+str(p),np.asarray(data))
		data=[]


def extractLabel(inputfile):
	df = pd.read_csv(inputfile, sep="\t")
	df['diagnoses.0.site_of_resection_or_biopsy']=df['diagnoses.0.site_of_resection_or_biopsy'].fillna(0)
	one_hot=pd.get_dummies(df['diagnoses.0.site_of_resection_or_biopsy'])
	df['label'] = df['diagnoses.0.site_of_resection_or_biopsy']
	labels=df['diagnoses.0.site_of_resection_or_biopsy'].values.tolist()
	np.save("labels",np.asarray(labels))
			
	df=pd.concat([df,one_hot],axis=1)
	columns = ['label']
	unq=df.label.unique()
	print("total label:"+str(len(unq)))
	good_labels=[]
	label_ind=[]
	
	data_distri1=plotgraph(labels,unq)
	

	filtered_labels=[]
	filtered_labels_unq=[]
	for i in range(0,len(unq)):
		if(data_distri1[i]>100):
			filtered_labels_unq.append(unq[i])
	print(len(filtered_labels_unq))
	print(np.shape(filtered_labels_unq[0]))
	print(filtered_labels_unq[0])
	
	for i in range(0,len(filtered_labels_unq)):
		for j in range(0,len(labels)):
			if labels[j] == filtered_labels_unq[i]:
				filtered_labels.append(labels[j])
	print(len(filtered_labels))
	print(np.shape(filtered_labels))
	#print(filtered_labels[0])

	data_distri=plotgraph(filtered_labels,filtered_labels_unq)
	


	for i in range(0,len(unq)):
		if str(unq[i])!= "nan":
			good_labels.append(unq[i])
	print("good_labels"+str(len(good_labels)))
	np.save("classes",np.asarray(good_labels))

	#for i in range(0,len(unq)):
	#	print(str(unq[i]))
	return one_hot





if __name__ == '__main__':

	data_dir="/home/siddharth/Downloads/"
	# Input directory and label file. The directory that holds the data. Modify this when use.
	dirname = data_dir + "live_miRNA"
	label_file = data_dir + "cases_meta.tsv"
	data_file = data_dir + "files_meta.tsv"

	#output file
	outputfile = data_dir + "miRNA_matrix.csv"

	print("*************EXTRACTING DATA BATCH-WISE**************")
	# extract data
	label_df = extractLabel(label_file)
	
	print("*************EXTRACTING LABELS**************")

	data_dir1="/home/siddharth/Documents/data/"
	#data_df = extractdata(data_file,data_dir1)

	
 

