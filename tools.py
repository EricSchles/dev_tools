import pandas as pd
import numpy
import scipy as sp
from scipy import stats
import math

def isnan(elem):
    if type(elem) != type(float()): return False
    return math.isnan(elem)

def has_integer(person):
    return any([elem.isdigit() for elem in person])

SECONDS_PER_DAY = float(86400)

def get_median(arr):
    return numpy.median(numpy.array(arr))

#interquartile range: http://stackoverflow.com/questions/27472330/how-should-the-interquartile-range-be-calculated-in-python
def get_iqr(arr):
    a = numpy.array(arr)
    iqr25th = numpy.percentile(a,25)
    iqr75th = numpy.percentile(a,75)
    iqr = iqr75th - iqr25th
    return iqr,iqr25th,iqr75th

def describe(times):
    s = sp.array(times)
    return stats.describe(s)

def sort_by_key(listing,sort_by):
    """
    Expects a list of dictionaries
    Returns a list of dictionaries sorted by the associated key
    """
    keys = []
    translate = {}
    for ind,elem in enumerate(listing):
        key = elem[sort_by]
        translate[key] = ind
        keys.append(key)
    keys.sort()
    new_ordering = [translate[key] for key in keys]
    return [listing[i] for i in new_ordering]

