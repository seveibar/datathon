import numpy as np
import matplotlib.pyplot as plt

dat = np.load("spreadsheets.npy")
years = [str(a) for a in range(1991,2016)]

maxyear = 2012
minyear = 1991
deltay = 3

def get_xrow(p_sc, cc, yearno):
    yearno_s = yearno - 1991

    # Generate a table for this SC
    xrow = []
    # Loop through all other series codes excluding the current SC
    for sc in dat[(dat["Series Code"] != p_sc) & (dat['Country Code'] != cc)]:
        # Now we input the delta to the xrow
        xrow.append(sc[years[yearno_s - 1]] - sc[years[yearno_s - deltay - 1]])
    return np.array(xrow)

def get_yval(p_sc, cc, yearno):
    yearno_s = yearno - 1991
    p_sc_years = dat[(dat["Series Code"] == p_sc) & (dat['Country Code'] == cc)][0]
    p_sc_inc = p_sc_years[years[yearno_s - 1]] - p_sc_years[years[yearno_s - deltay - 1]]
    return p_sc_inc

def get_training_matrix(p_sc=b"SL.TLF.TOTL.FE.ZS", cc=b"USA"):

    # Loop through all the years we know this series code < maxyear
    sc_features = []
    sc_out = []
    for yearno in range(minyear + deltay, maxyear):

        xrow = get_xrow(p_sc, cc, yearno)
        sc_inc = get_yval(p_sc, cc, yearno)

        sc_features.append(xrow)
        sc_out.append(sc_inc)


    sc_features = np.array(sc_features)
    sc_out = np.array(sc_out)
    return sc_features, sc_out

def get_feature_value(p_sc, cc, year, idat=None):
    if idat is None:
        idat = dat
    return idat[(dat["Series Code"] == p_sc) & (dat['Country Code'] == cc)][0][years[year-1991]]
