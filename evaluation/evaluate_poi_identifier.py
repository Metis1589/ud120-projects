#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

### it's all yours from here forward!
from sklearn import tree
clf = tree.DecisionTreeClassifier()
classifier = clf.fit(features_train, labels_train)
prediction = clf.predict(features_test, labels_test)

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

print precision_score(labels_test, prediction)
print recall_score(labels_test, prediction)

print len(prediction), len(labels_train), len(labels_test)

# print(clf.score(features_test, labels_test))





