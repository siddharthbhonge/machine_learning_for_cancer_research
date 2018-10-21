# miRNA Sequences to predict Primary Site/Origin of Cancer

<br />The miRNA expression quantification data is used https://gdc.cancer.gov/about to predict site of origin of the disease.



## Getting Started

The CNN model is trained on Titan Xp GPU and Amazon Sagemaker.This model is based on Keras with tensorflow backend.The results are
compared to a simple SVM and Logistic Regression.

### Prerequisites

1.Python 3.6 <br />
2.Tensorflow 1.5<br />
3.Keras <br />
4.Scikit Learn<br />
5.pandas<br />


### Installing

I.Download 
Expression Quantification data: 
miRNA sequence data<br />
1.Go to the data portal https://portal.gdc.cancer.gov/repository, on the left side there are two 
tabs: Files and Cases<br />
2.Click Cases and select a disease type: Liver Hepatocellular Carcinoma<br />
3.Click Files and select Data Category: Transcriptome Profiling Data type: 
miRNA Expression Quantification<br />
Experimental Strategy:
miRNA-Seq<br />
![alt text](https://github.com/siddharthbhonge/machine_learning_for_cancer_research/blob/master/1.png)
<br />
<br />
II.Click on the Manifest download. This will download the manifest file for use with GDC data transfer tool.
<br />
III.Data transfer tool Download: https://gdc.cancer.gov/access-data/gdc-data-transfer-tool<br />
Download the version according to your OS type. <br />
Command line to downloadand unzip a OSX version:  <br />
Download: <br />

```

wget -c -t 0 https://gdc.cancer.gov/files/public/file/gdc-client_v1.3.0_OSX_x64.zip<br />
Unzip:Unzip gdc-client_v1.3.0_OSX_x64.zip<br />


Download with gdc-client../<path-to-gdc-client>/gdc-client download –m <path-to-manifest-file><br />
e.g. ./~/Downloads/gdc-client –m ~/Downloads/gdc_manifest.2018-08-23.txt<br />
```




## Running the tests

1.Run check.py for checking if all the files have been downloaded.To download remaining ones use:
```

./<path-to-gdc-client>/gdc-client download <id>
e.g. ./gdc-client download fa63ce14-b9b5-4041-9df7-3b86ba9ede16 
```

![alt text](https://github.com/siddharthbhonge/machine_learning_for_cancer_research/blob/master/3.png)

2.Use parse_file_case_id.py to extract file and case ID's for further use.<br />

3.Download the JSON format of the Data from the same website.Use parser.py for for parsing the data into labels and data.<br />
![alt text](https://github.com/siddharthbhonge/machine_learning_for_cancer_research/blob/master/2.png)
The data is converted into 10 Numpy arrays<br />


```
batch_1.npy
batch_2.npy...

batch_10.npy each of shape(1000 x 1822)(i.e 1000 samples each with 1822 features)



```
![alt text](https://github.com/siddharthbhonge/machine_learning_for_cancer_research/blob/master/4.png)

Labels are Place of origin and are one hot coded.
![alt text](https://github.com/siddharthbhonge/machine_learning_for_cancer_research/blob/master/5.png)


## Deployment


These numpy arrays are feeded in batches using generator to CNN Model.<br />






## Authors

* **Siddharth Bhonge** - *Parser /Model* - https://github.com/siddharthbhonge


## Acknowledgments

* https://github.com/yuesOctober/GDCproject/tree/yue
