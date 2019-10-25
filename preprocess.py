import numpy as np

def standardize(x):
    mean = np.mean(x, axis=0)
    std = np.std(x, axis=0)
    centered_data = x - mean
    std_data = centered_data/std
    return std_data, mean, std

def fit_standardize(x, mean_stand, std_stand):
    centered_data = (x - mean_stand)/std_stand
    return centered_data

def remove_constant_col(x):
    const_col = (x.std(0)==0)
    x_process = x[:,~const_col]
    return x_process, const_col

def fit_remove_constant_col(x, const_col):#for the test part
    x_process = x[:, ~const_col]
    assert (x_process.std(0)==0).sum() == 0
    return x_process

def get_categorical_masks(x):
    return {
        0: (x[:,22] == 0),
        1: (x[:,22] == 1),
        2: (x[:,22] == 2),
        3: (x[:,22] == 3)
    }

def replaceNaNsWithMedian(tx):
    tx_replaced = tx
    for i in range(tx.shape[1]): #for each column compute median
        median = np.median(tx[:, i][tx[:, i] > -998.0])
        tx_replaced[:, i][tx[:, i] < -998.0] = median #and replace with column median
    return tx_replaced
