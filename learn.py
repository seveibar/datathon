from sklearn.externals import joblib
from sklearn.svm import SVR
import data_matrix

def regression(table):
    clf = joblib.load('model.pkl')
    return clf.predict([table])

if __name__ == '__main__':

    #TODO format X and Y value from main

    X,y = data_matrix.get_training_matrix(p_sc=b"BX.GSR.GNFS.CD",cc=b"USA")
    clf = SVR()
    clf.fit(X[:-1], y[:-1])
    joblib.dump(clf, 'model.pkl')
    fval = data_matrix.get_feature_value(b"BX.GSR.GNFS.CD",b"USA",2009)


    print regression(X[-1]) + fval
    print regression(X[-1])
    print y[-1]
    print y
