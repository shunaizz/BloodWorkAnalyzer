import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
import pickle
import os

BASE_DIR = os.path.join(os.getcwd(),'ml\MlModels')

from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


class BreastCancer:
    def __init__(self):
        file = BASE_DIR + '\BC.sav'
        self.load_model = pickle.load(open(file, 'rb'))

    def result(self,data):
        result = self.load_model.predict(data)
        return result



class Diabetes:
    def __init__(self):
        file = BASE_DIR + '\diabetes.sav'
        self.load_model = pickle.load(open(file, 'rb'))

    def result(self,data):
        result = self.load_model.predict(data)
        return result


class Heart:
    def __init__(self):
        file = BASE_DIR + '\heart.sav'
        self.load_model = pickle.load(open(file, 'rb'))

    def result(self,data):
        result = self.load_model.predict(data)
        return result


class Cardio:
    def __init__(self):
        file = BASE_DIR + '\cardio.sav'
        self.load_model = pickle.load(open(file, 'rb'))

    def result(self, data):
        result = self.load_model.predict(data)
        return result