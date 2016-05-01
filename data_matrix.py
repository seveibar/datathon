import numpy as np
import matplotlib.pyplot as plt

dat = np.load("spreadsheets.npy")
years = [str(a) for a in range(1991,2030)]

maxyear = 2015
minyear = 2006
maxdeltay = 2

# Removes countries not on whitelist
def apply_country_whitelist(whitelist):
    global dat
    newdat = []
    for c in whitelist:
        for d in dat[dat['Country Code'] == c]:
            newdat.append(d)
    dat = np.array(newdat, dtype=dat.dtype)
    

# Gets the X row, this is a super long row that contains all the delta slopes
def get_xrow(p_sc, cc, yearno):
    yearno_s = yearno - 1991

    # Generate a table for this SC
    xrow = []
    key = []
    # Loop through all other series codes excluding the current SC
    for sc in dat[(dat["Series Code"] != p_sc) | (dat['Country Code'] != cc)]:
        # Now we input the delta to the xrow
        for deltay in range(1,maxdeltay+1):
            xrow.append(sc[years[yearno_s - 1]] - sc[years[yearno_s - deltay - 1]])
            key.append(np.array([
                    sc["Series Code"],
                    sc["Country Code"],
                    years[yearno_s - 1],
                    years[yearno_s - deltay - 1]
                    ], dtype='S32'))
    return np.array(xrow), np.array(key)

# Same as get_xrow, but injects a spike
def get_xrow_with_spike(p_sc=None, p_cc=None, year=None, spike_sc=None, spike_cc=None, spike_amt=None):
    yearno_s = year - 1991
    # Generate a table for this SC
    xrow = []
    key = []
    # Loop through all other series codes excluding the current SC
    for sc in dat[(dat["Series Code"] != p_sc) | (dat['Country Code'] != p_cc)]:
        # Now we input the delta to the xrow
        for deltay in range(1,maxdeltay+1):
            if sc["Series Code"] == spike_sc and sc["Country Code"] == spike_cc:
                xrow.append((sc[years[yearno_s - 1]] + spike_amt) - sc[years[yearno_s - deltay - 1]])
            else:
                xrow.append(sc[years[yearno_s - 1]] - sc[years[yearno_s - deltay - 1]])
            key.append(np.array([
                    sc["Series Code"],
                    sc["Country Code"],
                    years[yearno_s - 1],
                    years[yearno_s - deltay - 1]
                    ], dtype='S32'))
    return np.array(xrow), np.array(key)

# Gets a single value for the y vector which is the "solution" matrix
# Takes a SC/Country that is being predicted and a year to get the increase in the SC for
def get_yval(p_sc, cc, yearno):
    yearno_s = yearno - 1991
    p_sc_years = dat[(dat["Series Code"] == p_sc) | (dat['Country Code'] == cc)][0]
    p_sc_inc = p_sc_years[years[yearno_s]] - p_sc_years[years[yearno_s - 1]]
    return p_sc_inc
    
def get_training_matrix(p_sc=b"SL.TLF.TOTL.FE.ZS", cc=b"USA"):

    # Loop through all the years we know this series code < maxyear
    sc_features = []
    sc_out = []
    
    # loop through all possible delta years
    for yearno in range(minyear + maxdeltay, maxyear):

        xrow,_ = get_xrow(p_sc, cc, yearno)
        sc_inc = get_yval(p_sc, cc, yearno)

        sc_features.append(xrow)
        sc_out.append(sc_inc)
        

    sc_features = np.array(sc_features)
    sc_out = np.array(sc_out)
    return sc_features, sc_out

# Get the value of a feature at a specific year
def get_feature_value(p_sc, cc, year, idat=None):
    if idat is None:
        idat = dat
    return idat[(dat["Series Code"] == p_sc) & (dat['Country Code'] == cc)][0][years[year-1991]]



# Adds a predicted year to the data using a list of corresponding series codes, country codes and 
# predicted values- this turns out to be a bit tricky
# def add_predicted_year(sc,cc,p_vals):
#     pass