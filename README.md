# miRNA Sequences to predict Primary Site/Origin of Cancer

The miRNA expression quantification data is used https://gdc.cancer.gov/about
-
data to predict site of origin of the disease.


## Getting Started

The CNN model is trained on Titan Xp GPU and Amazon Sagemaker.This model is based on Keras with tensorflow backend.The results are
compared to a simple SVM and Logistic Regression.

### Prerequisites

1.Python 3.6 
2.Tensorflow 1.5
3.Keras 
4.Scikit Learn
5.pandas


### Installing

I.Download 
Expression Quantification data: 
miRNA sequence data
1.Go to the data portal https://portal.gdc.cancer.gov/repository, on the left side there are two 
tabs: Files and Cases
2.Click Cases and select a disease type: Liver Hepatocellular Carcinoma
3.Click Files and select Data Category: Transcriptome Profiling Data type: 
miRNA Expression Quantification
Experimental Strategy:
miRNA-Seq
![alt text](https://drive.google.com/open?id=1vDlxzowPLaTKG4gRopcDEOhCOpG9nTu8)

II.Click on the Manifest download. This will download the manifest file for use with GDC data transfer tool.

III.Data transfer tool Download: https://gdc.cancer.gov/access-data/gdc-data-transfer-tool
Download the version according to your OS type. 
Command line to downloadand unzip a OSX version:  
Download: 
wget -c -t 0 https://gdc.cancer.gov/files/public/file/gdc-client_v1.3.0_OSX_x64.zip
Unzip:Unzip gdc-client_v1.3.0_OSX_x64.zi

Download with gdc-client../<path-to-gdc-client>/gdc-client download –m <path-to-manifest-file>
e.g. ./~/Downloads/gdc-client –m ~/Downloads/gdc_manifest.2018-08-23.txt




## Running the tests

1.Run check.py for checking if all the files have been downloaded.To download remaining ones use:
./<path-to-gdc-client>/gdc-client download <id>
e.g. ./gdc-client download fa63ce14-b9b5-4041-9df7-3b86ba9ede16 

2.Use parse_file_case_id.py to extract file and case ID's for further use.

3.download the JSON format of the Data from the same website.Use parser.py for for parsing the data into labels and data.
The data is converted into 10 Numpy arrays


```
batch_1.npy
batch_2.npy...

batch_10.npy each of shape(1000 x 1822)(i.e 1000 samples each with 1822 features)



```
Labels are Place of origin and are one hot coded.


## Deployment


These numpy arrays are feeded in batches using generator to CNN Model.




## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

