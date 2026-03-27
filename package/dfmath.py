import numpy as np

def colsum(df, col):
    tot = np.sum(df[col])
    return tot

def colavg(df, col):
    avg = np.mean(df[col])
    return avg

def maxval(df, col):
    high = np.max(df[col])
    return high

def minval(df, col):
    low = np.min(df[col])
    return low

def getstd(df, col):
    spread = np.std(df[col])
    return spread
