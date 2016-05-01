import data_matrix as dm
import numpy as np
#-------
from sklearn.externals import joblib
from sklearn.svm import SVR
#-------
country_whitelist = [b"USA",b"CHN",b"IDN",b"IND",b"BRA",b"PAK",b"NGA",b"BGD",b"RUS",b"JPN",b"MEX",b"PHL",b"ETH",b"VNM",b"EGY",b"ZAR",b"DEU",b"IRN",b"TUR",b"FRA",b"THA",b"GBR",b"ITA",b"TZA",b"ZAF",b"MMR",b"PRK",b"COL"]
dm.apply_country_whitelist(country_whitelist)
#-------
def get_model(X,y):
    clf = SVR(kernel='linear')
    clf.fit(X, y)
    return clf
#-------
def spike_effect_across_world(p_sc, spike_sc, spike_cc, spike_amt):
    result = {}
    # loop through countries
    for p_cc in country_whitelist:
        # Get the model
        X,y = dm.get_training_matrix(p_sc=p_sc,cc=p_cc)
        svm = get_model(X,y)
        data_2015, key_2015 = dm.get_xrow(p_sc, b"USA", 2015)
        normal_prediction = svm.predict(data_2015)[0]
        spike_X,key_2015 = dm.get_xrow_with_spike(p_sc=p_sc, p_cc=p_cc, year=2015, spike_sc=spike_sc, spike_cc=spike_cc, spike_amt=spike_amt)
        spike_prediction = svm.predict(spike_X)[0]
        result[p_cc] = spike_prediction - normal_prediction

    avg = np.sum(result[k] for k in result.keys()) / len(result.keys())
    for k in result.keys():
        result[k] = result[k] / avg

    return result    
