import numpy
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from tensorflow.python.keras import models
from keras.layers import Dense
from sklearn.utils import shuffle
from sklearn.cluster import KMeans

irisData, irisTarget = load_iris(return_X_y = True)
print(irisData)
irisData = StandardScaler().fit_transform(irisData)
irisTarget = OneHotEncoder(sparse = False).fit_transform(irisTarget.reshape(len(irisTarget), 1))
print("Loaded, standard scaled, and one-hot encoded iris data\n")

X_train, X_test, y_train, y_test = train_test_split(irisData, irisTarget, train_size = 0.8, random_state = 9)
print("Split data into 80% train, 20% test\n")

nnModel = models.Sequential()
nnModel.add(Dense(10, input_dim = 4, activation = 'relu'))
nnModel.add(Dense(9, activation = 'relu'))
nnModel.add(Dense(8, activation = 'relu'))
nnModel.add(Dense(7, activation = 'relu'))
nnModel.add(Dense(3, activation = 'softmax'))
nnModel.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
print("Created neural network\n")

neuralTrained = nnModel.fit(X_train, y_train, epochs = 100, batch_size = 32)
print("Trained neural network with train data\n")

testPred = nnModel.predict(X_test)
pred = list()
for i in range(len(testPred)):
    pred.append(numpy.argmax(testPred[i]))
test = list()
for i in range(len(testPred)):
    test.append(numpy.argmax(y_test[i]))
print("Predicted and converted data using inverse one-hot encoding\n")

print("NN model predicted values:", pred)
print("Actual values:            ", test)

accuScore = accuracy_score(test, pred)
print("NN model accuracy: {:.4f}".format(accuScore))