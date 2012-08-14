'''
Author: Scott Halgrim, halgrim.s@ghc.org
Date: 7/27/12
Functionality: Contains common math implementations.  E.g., mean, ssd
'''
import std_import as si
import math

def mean(inlist):
    '''
    Takes in list of numbers and returns their average
    >>> mean([1, 2, 3])
    2.0
    '''
    return float(sum(inlist))/float(len(inlist))

def ssd(inlist):
    '''
    Takes in list of numbers and returns their sample standard deviation
    >>> ssd([1, 2, 3])
    0.816496580928
    '''
    xbar = mean(inlist)
    diffs = [float(item)-xbar for item in inlist]
    diffsquares = [d**2 for d in diffs]
    squaremean = mean(diffsquares)
    answer = math.sqrt(squaremean)

    return answer

