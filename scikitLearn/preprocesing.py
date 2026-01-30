import os
import numpy as np
from sklearn import preprocessing
os.system("cls")

sample_data = np.array([[2.1, -1.9, 5.5],
                        [-1.5, 2.4, 3.5],
                        [0.5, -7.9, 5.6],
                        [5.9, 2.3, -5.8]])
print(sample_data)
print()
# print(sample_data.sha pe, " (baris, kolom)") # menampilkan dimensi dari dataset

# binarization
preprocessor = preprocessing.Binarizer(threshold=0.5) # nilai threshold yang <= 0.5 akan jadi 0
pinarised_data = preprocessor.transform(sample_data)
print(pinarised_data)
print()

# scalling
preprocessor2 = preprocessing.MinMaxScaler(feature_range=(0, 1))
#cara pertama scalling
preprocessor2.fit(sample_data)
scaled_data = preprocessor2.transform(sample_data)
print(scaled_data)
print()
# cara kedua scalling
scaled_data = preprocessor2.fit_transform(sample_data) # yang ini fit dan transform jadi satu
print(scaled_data)
print()

# L1 Normalisation: least absolute deviations
l1_normalized_data = preprocessing.normalize(sample_data, norm='l1') # l1 akan berasosiasi yang mengenakan least deviations
print(l1_normalized_data)
print()

# l2 Normalisation: least squars
l2_normalized_data = preprocessing.normalize(sample_data, norm='l2')
print(l2_normalized_data)
print()