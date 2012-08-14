from std_import import *
import collections

# get module logger
logger = logging.getLogger('org.ghri.util.counter_dict')

def counter_sorter(x, y):
    if x[1] == y[1]:
        return cmp(x[0], y[0])
    else:
        return cmp(y[1], x[1]) # cuz i want highest to lowest

def counterFactory():
    return 0

class CounterDict(collections.defaultdict):
    def __init__(self):
        super(CounterDict, self).__init__(counterFactory)
        return

