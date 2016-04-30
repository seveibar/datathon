from sklearn.externals import joblib
from sklearn.svm import SVR

def regression(y_table):
    #TODO figure out how x_table is being sent to me and possibly format it
    clf = joblib.load('model.pkl')
    return clf.predict([y_table])

if __name__ == '__main__':

    #TODO format X and Y value from main
    #X = [[0.6,0.5 , 0.4], [0.7, 0.9,0.7], [0.8,1.4,1.2]]
    #y=[100,120,130]
    clf = SVR()
    clf.fit(X, y)
    joblib.dump(clf, 'model.pkl')
    print classify(y)
