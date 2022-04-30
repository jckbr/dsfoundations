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
irisData, irisTarget = shuffle(irisData, irisTarget)

kmeans = KMeans(n_clusters = 3)
kmeans.fit(irisData)
y_kmeans = kmeans.predict(irisData)

kMeansMetrics = precision_recall_fscore_support(irisTarget, y_kmeans)
print("\nkMeans (3 clusters) precision: {:.4f}".format(kMeansMetrics[0][-1]))
print("kMeans (3 clusters) recall: {:.4f}".format(kMeansMetrics[1][-1]))
print("kMeans (3 clusters) F1 Score: {:.4f}".format(kMeansMetrics[2][-1]))