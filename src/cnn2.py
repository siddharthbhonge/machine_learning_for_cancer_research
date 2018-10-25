from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from sklearn.svm import SVC
from keras import backend as K
from sklearn.preprocessing import OneHotEncoder

from keras.utils import np_utils
'''
if K.backend()=='tensorflow':
    K.set_image_dim_ordering("th")
import tensorflow as tf
import multiprocessing as mp

core_num = mp.cpu_count()
print(core_num)
config = tf.ConfigProto(
    inter_op_parallelism_threads=core_num,
    intra_op_parallelism_threads=core_num)
sess = tf.Session(config=config)
'''
import numpy as np

data_augmentation = False
num_classes=5
#class_names = ['zero','one']


# Convert and pre-processing
data=np.load("data.npy")
labels=np.load("labels.npy")

uni=np.unique(labels)
labels_int=[]
for i in range (0,len(labels)):
    for j in range(0, len(uni)):
        if labels[i] == uni[j]:
            labels_int.append(j)


#print(len(labels_int))
#print(len(labels))
#print(uni)
def one_hot(a, num_classes):
  return np.squeeze(np.eye(num_classes)[a.reshape(-1)])
labels_int_n=np.asarray(labels_int)
b=one_hot(labels_int_n,5)

print(data[0,0])
print(b[0,:])

batch_train1 = np.zeros(data.shape)
input_shape=batch_train1.shape[1:]

svclassifier = SVC(kernel='poly', degree=8)
svclassifier.fit(data, labels_int_n)

y_pred = svclassifier.predict(data)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(labels_int_n, y_pred))
print(classification_report(labels_int_n, y_pred))

#labels_train = np_utils.to_categorical(labels, num_classes)
#print(np.shape(labels_train))




def base_model():

    model = Sequential()
    model.add(Dense(2048, activation='relu',input_shape=input_shape))
    model.add(Dense(512, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    sgd = SGD(lr = 0.1, decay=5e-4, nesterov=True)
# Train model
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    return model
cnn_n = base_model()
cnn_n.summary()


cnn=cnn_n.fit(x=data, y=b,batch_size=1, epochs=10, verbose=1)
#validation_data=(n_test_data,labels_test)


