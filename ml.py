import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
import pickle

print('done import')

sc = StandardScaler()


class Diabetes:
    def dai(self):
        df = pd.read_csv('diabetes.csv')
        df.head()
        x = df.drop('Outcome',axis=1)
        y = df['Outcome']

        x_train,x_test,y_train,y_test= train_test_split(x,y,shuffle=False,test_size=0.3)
        file = 'diabetes.sav'
        classifier = LogisticRegression(random_state = 0,max_iter=67)
        classifier.fit(x_train, y_train)
        pickle.dump(classifier, open(file, 'wb'))

        y_graph = []
        stat = 65
        endi = 70
        print('ready for ')
        for i in range(stat,endi):
            classifier = LogisticRegression(random_state = 0,max_iter=i)
            classifier.fit(x_train, y_train)
            y_pred = classifier.predict(x_test)
            cm = confusion_matrix(y_test, y_pred)
            #print(cm)
            acc = accuracy_score(y_test,y_pred)
            y_graph.append(acc*100)
            #print(i,':',acc*100)


        x_graph = list(range(stat,endi))
        print("Got thses results for BC so far")
        print("Highest accuracy score is:",max(y_graph),'%')
        plt.plot(x_graph,y_graph)
        plt.show()


class BreastCancer:
    def __init__(self):
        self.df = pd.read_csv('bc.csv')
        self.df.drop('id', axis=1, inplace=True)
        self.df.drop('Unnamed: 32', axis=1, inplace=True)
        self.df['diagnosis'] = self.df['diagnosis'].map({'M': 1, 'B': 0})
        self.x = self.df.drop('diagnosis', axis=1)
        self.y = self.df['diagnosis']
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, shuffle=False)
        self.x_trian = sc.fit_transform(self.x_train)
        self.x_test = sc.fit_transform(self.x_test)

    def bc(self):
        y_graph = []
        for i in range(1, 5):
            classifier = LogisticRegression(random_state=0, max_iter=i)
            classifier.fit(self.x_train, self.y_train)
            y_pred = classifier.predict(self.x_test)
            cm = confusion_matrix(self.y_test, self.y_pred)
            # print(cm)
            acc = accuracy_score(self.y_test, y_pred)
            y_graph.append(acc * 100)
            # print(i,':',acc*100)

        x_graph = list(range(1, 5))
        print("Got thses results for BC so far")
        print("Highest accuracy score is:", int(max(y_graph)), '%')
        plt.plot(x_graph, y_graph)
        plt.show()

    def dump(self,num,file):
        classifier = LogisticRegression(random_state=0, max_iter=num)
        classifier.fit(self.x_train, self.y_train)
        pickle.dump(classifier, open(file, 'wb'))


class Heart:
    def __init__(self):
        self.df = pd.read_csv('heart.csv')
        #print('df head',self.df.head())
        self.x = self.df.drop('target', axis=1)
        self.y = self.df['target']
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, shuffle=False, test_size=0.2)
        self.x_train = sc.fit_transform(self.x_train)
        self.x_test = sc.fit_transform(self.x_test)

    def heart(self):
        y_graph = []
        endi = 50
        classifier = KNeighborsClassifier(n_neighbors=2, metric='minkowski', p=1)
        classifier.fit(self.x_train, self.y_train)
        y_pred = classifier.predict(self.x_test)
        cm = confusion_matrix(self.y_test, y_pred)
        print('cm',cm)
        acc = accuracy_score(self.y_test, y_pred)
        print('ass',acc)
        return (cm,acc)
        for i in range(1, endi):
            classifier = LogisticRegression(random_state=0, max_iter=i)
            classifier.fit(self.x_train, self.y_train)
            y_pred = classifier.predict(self.x_test)
            cm = confusion_matrix(self.y_test, y_pred)
            # print(cm)
            acc = accuracy_score(self.y_test, y_pred)
            y_graph.append(acc * 100)
            # print(i,':',acc*100)

        x_graph = list(range(1, endi))
        print("Got thses results for BC so far")
        print("Highest accuracy score is:", int(max(y_graph)), '%')
        plt.plot(x_graph, y_graph)
        plt.show()

    def dump(self,file):

        classifier = KNeighborsClassifier(n_neighbors=2, metric='minkowski', p=1)
        classifier.fit(self.x_train, self.y_train)
        pickle.dump(classifier, open(file,'wb'))

    def load(self,file):
        self.load_model = pickle.load(open(file, 'rb'))
        result = self.load_model.score(self.x_test,self.y_test)
        print(result)

    def predict(self,data):
        #a = self.load_model.pr
        pass



class Cardio:
    def __init__(self):
        df = pd.read_csv('cardio.csv')
        #df.drop('id',axis=1,inplace=True)
        print(df.head())
        x = df.drop('cardio',axis = 1)
        y = df['cardio']
        x_train, x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=0.2, shuffle=False)
        sc = StandardScaler()
        self.x_train = sc.fit_transform(x_train)
        self.x_test = sc.fit_transform(x_test)


    def dump(self,file):
        classifier = LogisticRegression(random_state=0, max_iter=7)
        classifier.fit(self.x_train, self.y_train)
        pickle.dump(classifier, open(file, 'wb'))




"""

load_model = pickle.load(open(file, 'rb'))
result = load_model.score(x_test,y_test)
print(result)
"""

if __name__ == "__main__":
    a = Cardio()
    a.dump('cardio.sav')
    pass